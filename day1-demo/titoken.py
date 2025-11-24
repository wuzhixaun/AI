import tiktoken
from openai import OpenAI

gpt_model = "gpt-4"
encoder = tiktoken.encoding_for_model(gpt_model)

client  = OpenAI()

def count_token(text):
    # 统计token
    encoder.encode(text)
    token = encoder.encode(text)
    return len(token)

def main():
    # 初始化聊天
    messages = [
        {"role": "system", "content": "you are a helpful assistant"},
    ]


    print("开始聊天吧，输入exit退出")

    total_token = 0


    while True:
        # 获取用户输入
        user_input = input("You: ")

        if user_input == "exit":
            break

        # 添加用户输入到消息列表
        messages.append({"role": "user", "content": user_input})

        # 统计token
        user_token = count_token(user_input)

        total_token += user_token

        completion = client.chat.completions.create(
            model= gpt_model,
            messages= messages,
            max_tokens=150,
            temperature=0.7,
            top_p=1,
            n=1
        )

        # 获取机器人回复
        assistant_message = completion.choices[0].message.content.strip()

        # 添加机器人回复到消息列表
        messages.append({"role": "assistant", "content": assistant_message})

        # 统计token
        assistant_token = count_token(assistant_message)
        total_token += assistant_token

        # 输入用户输入和机器人回复
        print(f"Assistant: {assistant_message}")

        # 输出token
        print(f"用户tokens数:{user_token}，机器人tokens数：{assistant_token}，总tokens数：{total_token}")


if __name__ == "__main__":
    main()