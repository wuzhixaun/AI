from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"))


def get_completion(table_structures, sql_requirements, model="qwen-plus"):
    instruction = """
    你是⼀位专业的SQL编写⼯程师,可以根据表结构和⽤⼾输⼊，⽣成SQL语句。
    """

    examples = """
    表结构如下：
    orders (
    id INT PRIMARY KEY NOT NULL,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    STATUS INT NOT NULL CHECK (STATUS IN (0, 1, 2)), -- 确保订单状态在
    0, 1, 2之间
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    pay_time TIMESTAMP NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
    );
    customers (
    id INT PRIMARY KEY NOT NULL, -- 主键，不允许为空
    customer_name VARCHAR(255) NOT NULL, -- 客⼾名，不允许为空
    email VARCHAR(255) UNIQUE, -- 邮箱，唯⼀
    register_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 注册时间，默认
    为当前时间
    );
    products (
        id INT PRIMARY KEY NOT NULL, -- 主键，不允许为空
        product_name VARCHAR(255) NOT NULL, -- 产品名称，不允许为空
        price DECIMAL(10,2) NOT NULL -- 价格，不允许为空
    );
    ⽤⼾需求：
    哪个⽤⼾消费最⾼？消费多少？
    ⽣成的SQL：
    SELECT customer_id, SUM(price) AS total_spent FROM orders GROUP BY
    customer_id ORDER BY total_spent DESC LIMIT 1;
    """

    prompt = f"""
    {instruction}
    ⽰例：
    {examples}
    表结构如下：
    {table_structures}
    ⽤⼾输⼊：
    {sql_requirements}
    """

    print(prompt)

    messages = [{"role": "user", "content": prompt}]

    res = client.chat.completions.create(model=model, messages=messages)
    return res.choices[0].message.content



# streamlit 界面
st.title("SQL语句生成助手")

# 获取⽤⼾输⼊的表结构数量
num_tables = st.number_input("请输⼊你需要填写的表结构数量",min_value=1, max_value=10, step=1)

# 创建⽤于填写表结构的输⼊框
table_structures = ""
for i in range(num_tables):
    table_structure = st.text_area(f"请输⼊表结构 {i + 1}:")
    table_structures += table_structure + "\n"

# 获取⽤⼾输⼊的SQL要求
sql_requirements = st.text_area("请输⼊你的SQL要求:")

if st.button("提交"):
    if all(table_structures) and sql_requirements: # 检查是否所有的表结构和SQL需求都已经填写
        sql_code = get_completion(table_structures, sql_requirements)
        st.success(sql_code)
    else:
        st.warning("请确保所有的表结构和SQL需求都已经填写")
