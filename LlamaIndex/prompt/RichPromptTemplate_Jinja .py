from llama_index.core.prompts import RichPromptTemplate



template = RichPromptTemplate(
    """
{% chat role="system" %}
给定一个列表，包含图片和文本, 请尽你所能回答这个问题.
{% endchat %}

{% chat role="user" %}
{% for image_path, text in images_and_texts %}
这是一些文本: {{ text }}
这是一张图片:
{{ image_path | image }}
{% endfor %}
{% endchat %}
"""
)

messages = template.format_messages(
    images_and_texts=[
        ("page_1.jpg", "文件的第一页数据"),
        ("page_2.jpg", "文件的第二页数据"),
    ]
)
print(messages)