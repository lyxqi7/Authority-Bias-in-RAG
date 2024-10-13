import gzip
import json
import os
import requests
in_put = 'datasets/original/SQuADTrain.json'
out_put = 'data.csv'
file_path1 = 'datasets/substitution-sets/SQuADTrainAlias.jsonl'
file_path2 = 'datasets/substitution-sets/SQuADTrainCorpus.jsonl'
file_path3 = 'datasets/substitution-sets/SQuADTrainTypeSwap.jsonl'
file_path = 'wikidata/entity_info.json.gz'

with open(file_path1, 'r') as file:
    alias = file.readlines()
 
Alias_lines = len(alias)
with open(file_path2, 'r') as file:
    Co = file.readlines()
 
Co_lines = len(Co)
with open(file_path3, 'r') as file:
    TS = file.readlines()
 
TS_lines = len(TS)
file_path1_general = 'general/SQuADTrainAliasGeneral.jsonl'
file_path2_general = 'general/SQuADTrainCorpusGeneral.jsonl'
file_path3_general = 'general/SQuADTrainTypeSwapGeneral.jsonl'
process_log = 'log/process.log'
error_log = 'log/error.log'
plog = open(process_log, 'a+')
elog = open(error_log, 'a+')
plog.write(f"Alias:{Alias_lines}")
print(f"Alias:{Alias_lines}")

alias = []


def general(uid, text):
    prompt=f'Please rewrite the text I sent to you, changing the wording as much as possible without changing the original meaning of the sentence and all the information. Please note that your reply should only contain the rewritten content, and no other prompt words should appear. The text: {text}'
    data = {
    "model": "llama2",
    "prompt": prompt,
    "stream": False
    }
    try:
        response = requests.post("http://localhost:11434/api/generate", json=data)
        re = json.loads(response.text)
    except:
        elog.write(str(uid))
        print(str(uid))
    return (re["response"])
    #return call_llm_api(text, "gpt-3.5-turbo", 0.0, 256, openai_client=openai_client)

num=0
with open(file_path1, "r") as file_handle:
    with open(file_path1_general, "w") as outf:
        outf.write(file_handle.readline())
        for line in file_handle:
            data = json.loads(line)
            pair = {'id': data['original_example'], 'answer': data['gold_answers'][0]['text'], 'query': data['query']}
            new = data
            new['context_general'] = general(data['uid'],data['context'])
            json.dump(new, outf)
            outf.write("\n")
            num+=1
            if num % 100 == 0:
                plog.write(str(num))
                print(str(num))
            #alias.append(pair)

plog.write(f"Corpus:{Co_lines}")
print(f"Corpus:{Co_lines}")
num=0
with open(file_path2, "r") as file_handle:
    with open(file_path2_general, "w") as outf:
        outf.write(file_handle.readline())
        for line in file_handle:
            data = json.loads(line)
            pair = {'id': data['original_example'], 'answer': data['gold_answers'][0]['text'], 'query': data['query']}
            new = data
            new['context_general'] = general(data['uid'],data['context'])
            json.dump(new, outf)
            outf.write("\n")
            num+=1
            if num % 100 == 0:
                plog.write(str(num))
                print(str(num))
            #corpus.append(pair)

plog.write(f"TypeSwap:{TS_lines}")
print(f"TypeSwap:{TS_lines}")
num=0
with open(file_path3, "r") as file_handle:
    with open(file_path3_general, "w") as outf:
        outf.write(file_handle.readline())
        for line in file_handle:
            data = json.loads(line)
            pair = {'id': data['original_example'], 'answer': data['gold_answers'][0]['text'], 'query': data['query']}
            new = data
            new['context_general'] = general(data['uid'],data['context'])
            json.dump(new, outf)
            outf.write("\n")
            num+=1
            if num % 100 == 0:
                plog.write(str(num))
                print(str(num))
