# 上课笔记

##如何获得 OpenAI API Key？

OpenAI 官方直连 (开发者，或 plus 会员)
https://platform.openai.com/docs/quickstart
Azure OpenAI Service (企业申请)
https://learn.microsoft.com/zh-cn/azure/ai-services/openai/
OpenAI API 中转 (民间方案)
https://www.openai-hk.com/docs/


## OpenAI环境变量


### Windows 导入环境变量

```powershell
#HK代理环境，不需要科学上网(价格便宜、有安全风险，适合个人开发调试)
setx OPENAI_BASE_URL "https://api.openai-hk.com/v1"
setx OPENAI_API_KEY "hk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#官方环境，需要科学上网(价格高、安全可靠，适合个人企业生产部署)
setx OPENAI_BASE_URL "https://api.openai.com/v1"
setx OPENAI_API_KEY "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

注意：每次执行完，需要重启PyCharm才能生效
```

### Mac 导入环境变量

```bash
#HK代理环境，不需要科学上网
export OPENAI_BASE_URL='https://api.openai-hk.com/v1'
export OPENAI_API_KEY='hk-mjgq4s100005250287bfc02d4748d618ada353b0fee8ab4b'

#官方环境，需要科学上网
export OPENAI_API_KEY='https://api.openai.com/v1'
export OPENAI_API_KEY='sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```
[env.dev](..%2F..%2F2.OpenAI%20%BF%AA%B7%A2%2Fbak%2Fenv.dev)
## Apifox和Postman
### 下载地址
Apifox：https://www.apifox.com/   (推荐)
Postman：https://www.postman.com/
对比：https://blog.csdn.net/ufrontend/article/details/140460531

### OpenAI接口文档
官方文档：https://platform.openai.com/docs/api-reference/chat/create
中文文档：https://apifox.com/apidoc/shared-012b355c-5a9e-4b61-aeca-105d78dc51d5?pwd=jkai
导入到apifox：导入OpenAI.apifox.json 或者页面克隆，自动生成python代码
导入到posfman：导入OpenAI.postman.json

##开发环境
### 安装 Python (v3.12.4)
https://www.python.org/downloads/ 
### 安装 PyCharm Community Edition 2024
https://www.jetbrains.com/pycharm/download 
### PyCharm 配置Python Interpreter
https://blog.csdn.net/maiya_yayaya/article/details/131549166
### 使用PyCharm 实现Chat Completions Api 简单Request调用
