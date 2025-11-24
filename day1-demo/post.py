from dotenv import load_dotenv
import os

str2 = "jjja"

print(str2.lstrip("j"))


# 将.env文件中的环境变量加载到系统中
load_dotenv()

# 访问环境变量
db_name = os.getenv("DATA_BASE_NAME")
print(db_name)