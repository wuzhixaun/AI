

# {"Document(id='f821beca-d91f-42a5-abdb-bf8e65b9b564', metadata={}, page_content='人工智能在制造业的应用。')": 0, "Document(id='d9d8c92b-2716-453d-b504-c5434e06403b', metadata={}, page_content='人工智能在医疗诊断中的应用。')":0}

aa = {'{"lc": 1, "type": "constructor", "id": ["langchain", "schema", "document", "Document"], "kwargs": {"id": "85a70265-4081-4fdc-a25b-e60e8478fd79", "page_content": "\\u4eba\\u5de5\\u667a\\u80fd\\u5728\\u5236\\u9020\\u4e1a\\u7684\\u5e94\\u7528\\u3002", "type": "Document"}}': 0.06612021857923497, '{"lc": 1, "type": "constructor", "id": ["langchain", "schema", "document", "Document"], "kwargs": {"id": "1712b4aa-ac54-4a73-81f9-a77cd3459229", "page_content": "\\u4eba\\u5de5\\u667a\\u80fd\\u5728\\u533b\\u7597\\u8bca\\u65ad\\u4e2d\\u7684\\u5e94\\u7528\\u3002", "type": "Document"}}': 0.06452452301209573, '{"lc": 1, "type": "constructor", "id": ["langchain", "schema", "document", "Document"], "kwargs": {"id": "bf7edd2d-ae9e-4ac1-b3cf-f08c0e47956d", "page_content": "\\u4eba\\u5de5\\u667a\\u80fd\\u5982\\u4f55\\u5f71\\u54cd\\u672a\\u6765\\u5c31\\u4e1a\\u5e02\\u573a\\u3002", "type": "Document"}}': 0.06585580821434867, '{"lc": 1, "type": "constructor", "id": ["langchain", "schema", "document", "Document"], "kwargs": {"id": "a7d26918-27c8-4934-a76a-888ba88d94ee", "page_content": "\\u4eba\\u5de5\\u667a\\u80fd\\u5728\\u91d1\\u878d\\u98ce\\u9669\\u7ba1\\u7406\\u4e2d\\u7684\\u5e94\\u7528\\u3002", "type": "Document"}}': 0.047619047619047616, '{"lc": 1, "type": "constructor", "id": ["langchain", "schema", "document", "Document"], "kwargs": {"id": "bbfafa01-f5b3-4da7-9368-ae684c7158c0", "page_content": "\\u4eba\\u5de5\\u667a\\u80fd\\u5982\\u4f55\\u63d0\\u5347\\u4f9b\\u5e94\\u94fe\\u6548\\u7387\\u3002", "type": "Document"}}': 0.016129032258064516}

for i in aa.items():
    print(i[1])

bb = sorted(aa.items(), key=lambda x: x[1], reverse=True)
print(bb)


