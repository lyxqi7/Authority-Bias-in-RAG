import json
models = ['gemma','llama2:7b','llama2:13b', 'mistral', 'vicuna:7b']
# models = ['llama2:7b']
result = 'result/'
for model in models:
    print(f'Model: {model}')
    file_path1_result = result+model+'/SQuADTrainAlias.jsonl'
    file_path2_result = result+model+'/SQuADTrainCorpus.jsonl'
    file_path3_result = result+model+'/SQuADTrainTypeSwap.jsonl'
    if result=='result/'and model == 'llama2:7b':
        model = 'gpt_answer'
   

    print("Corpus:")
    num = [0, 0, 0, 0, 0, 0]
    with open(file_path2_result, "r") as file_handle:
        file_handle.readline()
        for line in file_handle:
            data = json.loads(line)
            answer = data[model]
            fake_answer = data['gold_answers'][0]['text']
            true_answer = data['origin_answer']
            kind = data['num']
            if fake_answer in answer and true_answer in answer:
                num[kind * 3 + 2] += 1
                continue
            if fake_answer in answer:
                num[kind * 3 + 1] += 1
                continue
            if true_answer in answer:
                num[kind * 3 + 0] += 1
                continue
            num[kind * 3 + 2] += 1

    print(num)
    u_f_total= num[0]+num[1]+num[2]
    e_f_total= num[3]+num[4]+num[5]
    
    u_f = num[1]/u_f_total*100
    e_f = num[4]/e_f_total*100
    # print((round(u_f,2)+round(e_f,2))/2)
    print(round(u_f,2))
    print(round(e_f,2))
