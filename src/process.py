import gzip
import json
origin = 'datasets/normalized/SQuADTrain.jsonl.gz'
file_path1 = 'datasets/substitution-sets/SQuADTrainAlias.jsonl'
file_path2 = 'datasets/substitution-sets/SQuADTrainCorpus.jsonl'
file_path3 = 'datasets/substitution-sets/SQuADTrainTypeSwap.jsonl'
file_path1_general = 'general/SQuADTrainAliasGeneral.jsonl'
file_path2_general = 'general/SQuADTrainCorpusGeneral.jsonl'
file_path3_general = 'general/SQuADTrainTypeSwapGeneral.jsonl'
file_path1_experiment = 'experiment/SQuADTrainAlias.jsonl'
file_path2_experiment = 'experiment/SQuADTrainCorpus.jsonl'
file_path3_experiment = 'experiment/SQuADTrainTypeSwap.jsonl'
log='log2.log'
log_file = open(log, "a+")

num = 0

with gzip.open(origin, "rb") as file_handle:
    file_handle.readline()
    entry = file_handle.readline()
    with open(file_path3_general, "r") as general_file:
        with open(file_path3_experiment, "w") as outf:
            outf.write(general_file.readline())
            for line in general_file:
                general = json.loads(line)
                id = general['original_example']
                while entry:
                    if type(entry) == dict:
                        pass
                    else:
                        entry = json.loads(entry)
                    if entry['uid'] == id:
                        general['origin_answer'] = entry['gold_answers'][0]['text']
                        general['origin_context'] = entry['context']
                        json.dump(general, outf)
                        outf.write("\n")
                        break
                    else:
                        entry = file_handle.readline()
                num += 1
                if num % 100 == 0:
                    log_file.write(f'{num}\n')
                    log_file.flush()