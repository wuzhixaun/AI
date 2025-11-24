from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # 从我们的env⽂件中加载出对应的环境变量

# 创建OpenAI客户端
client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"))


# 零样本提示的优势：

# 1．无需任务特定训练：模型可以直接根据提示完成任务，无需针对每个任务进行专门训练。

# 2. 灵活性高：适用于多种任务类型，包括分类、生成、翻译、推理等。
# 3. 易于使用：用户只需提供清晰的提示，即可获得结果。

# 注意事项：

# 。 提示设计：提示的清晰度和具体性会直接影响模型的表现。

# 。 模型能力：零样本提示的效果依赖于模型本身的预训练质量和规模。

# • 任务复杂度：对于非常复杂或专业性强的任务，可能需要少量样本（Few-Shot）或微调（Fine-Tuning）来提升效果。

# 提示词
prompt = """
将文本分为中性，负面、正面
文本：我认为这家餐馆的菜品一般
"""

# 在上面的提示中，我们没有想模型提供任何示例-这就是零样本能力作用
def get_completion(prompt,model="qwen-plus"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content



print(get_completion(prompt))