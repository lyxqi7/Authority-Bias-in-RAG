import json
file1 = 'experiment/SQuADTrainAlias.jsonl'
file2 = 'experiment/SQuADTrainCorpus.jsonl'
file3 = 'experiment/SQuADTrainTypeSwap.jsonl'
file4 = 'experiment_continue2/SQuADTrainAlias.jsonl'
file5 = 'experiment_continue2/SQuADTrainCorpus.jsonl'
file6 = 'experiment_continue2/SQuADTrainTypeSwap.jsonl'

files= [file1,file2,file3,file4,file5,file6]

for file in files:
    [None, 'DATE','NUMERIC','PERSON','ORGANIZATION','LOCATION']
    total=[0,0,0,0,0,0,0]
    with open(file, "r") as file_handle:
        file_handle.readline()
        for line in file_handle:
            try:
                entry = json.loads(line)
            except:
                print('error')
                continue
            if len(entry['gold_answers']) == 0:
                continue
            if entry['gold_answers'][0]['answer_type'] == None:
                total[0] += 1
            elif entry['gold_answers'][0]['answer_type'] == 'DATE':
                total[1] += 1
            elif entry['gold_answers'][0]['answer_type'] == 'NUMERIC':
                total[2] += 1
            elif entry['gold_answers'][0]['answer_type'] == 'PERSON':
                total[3] += 1
            elif entry['gold_answers'][0]['answer_type'] == 'ORGANIZATION':
                total[4] += 1
            elif entry['gold_answers'][0]['answer_type'] == 'LOCATION':
                total[5] += 1
            else:
                total[6] += 1
    print(file)
    total[6] = total[0] + total[1]+total[2]+total[3]+total[4]+total[5]
    print(total)