import tiktoken
from openai import OpenAI

gpt_model = "gpt-4"
encoder = tiktoken.encoding_for_model(gpt_model)

client = OpenAI()

# 限制token数
MAX_TOKENS = 8

# 最大响应TOKEN数
MAX_RESPONSE_TOKENS = 6


def count_token(text):
    encoder.encode(text)
    tokens = encoder.encode(text)
    return len(tokens)


def manage_token_limit(messages):
    current_token = count_token(messages)
    if current_token > (MAX_TOKENS - MAX_RESPONSE_TOKENS):
        print(f"当前会话token数量为{current_token}，已经超过限制{MAX_TOKENS - MAX_RESPONSE_TOKENS}，请重新输入")
        return False
    return True

def get_gpt_response(messages):
    completion = client.chat.completions.create(
        model=gpt_model,
        messages=messages,
        max_tokens=MAX_RESPONSE_TOKENS,
        temperature=0.7,
        top_p=1,
        n=1
    )
    return completion.choices[0].message.content.strip()



def main():
    messages = []

    print("Chat with GPT-4. Type 'exit' to end the conversation.")


    total_token = 0

    while True:
        # 获取用户输入
        user_input = input("You: ")
        if user_input == "exit":
            break

        # 添加用户输入到消息列表
        messages.append({"role": "user", "content": user_input})

        if not manage_token_limit(user_input):
            continue

        assistant_message = get_gpt_response(messages)

        print(f"GPT-4: {assistant_message}")

        # 添加机器人回复到消息列表
        messages.append({"role": "assistant", "content": assistant_message})

        # 统计token
        assistant_token = count_token(assistant_message)
        total_token += assistant_token

        # 输入用户输入和机器人回复
        print(f"Assistant: {assistant_message}")

if __name__ == "__main__":
    main()
