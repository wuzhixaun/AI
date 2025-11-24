from transformers import BertTokenizer

#加载字典和分词工具

token = BertTokenizer.from_pretrained("bert-base-chinese")
# print(token)

sents = ["东西不错，不过有人不太喜欢镜面的，我个人比较喜欢，总之还算满意。",
         "房间不错,只是上网速度慢得无法忍受,打开一个网页要等半小时,连邮件都无法收。另前台工作人员服务态度是很好，只是效率有得改善。",
         "看了一半就看不下去了，后半本犹豫几次都放下没有继续看的激情，故事平淡的连个波折起伏都没有，职场里那点事儿也学得太模糊，没有具体描述，而且杜拉拉就做一个行政而已，是个人都会做的没有技术含量的工作 也能描写的这么有技术含量 真是为难作者了本来冲着畅销排行第一买来看看，觉得总不至于大部分人都没品味吧？结果证明这个残酷的事实，一本让人如同嚼蜡的“畅销书”......"]

#批量编码句子
out = token.batch_encode_plus(
    batch_text_or_text_pairs=[sents[0],sents[2]],
    add_special_tokens=True,
    #当句子长度大于max_lenght时，截断
    truncation=True,
    #一律补0到max_length长度
    padding="max_length",
    max_length=50,
    #可取值为tf,pt,np,默认为返回list
    return_tensors=None,
    #返回attention_mask
    return_attention_mask=True,
    return_token_type_ids=True,
    return_special_tokens_mask=True,
    #返回offsets_mapping 标识每个词的起止位置，这个参数只能BertTokenizerFast使用
    # return_offsets_mapping=True,
    #返回length长度
    return_length=True
)

#input_ids 就是编码后的词
#token_type_ids第一个句子和特殊符号的位置是0，第二个句子的位置1
#special_tokens_mask 特殊符号的位置是1，其他位置是0
#length
# print(out)

for k,v in out.items():
    print(k,":",v)

#解码文本数据
print(token.decode(out["input_ids"][0]),token.decode(out["input_ids"][1]))