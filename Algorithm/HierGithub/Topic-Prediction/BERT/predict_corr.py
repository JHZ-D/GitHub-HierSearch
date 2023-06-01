import subprocess
import os
import pandas as pd
import json
import csv
i = 0
with open('llist.json', 'r') as f:
    llist = json.load(f)
with open('pybert/output/predict/repo_labels.json', 'r') as f:
    repo_labels = json.load(f)

i = 53
with open(f'pybert/output/predict/{i}/predict.txt', 'r') as f:
    lines = f.readlines()
# testdf = pd.read_csv(f'pybert/dataset/{i}', header=0)
df = pd.read_csv(f'pybert/dataset/predict/{i}/test.csv', header=0)
ids = df[df.columns[0]]
repos = df[df.columns[1]]
contents = df[df.columns[2]]
header = df.columns.tolist()
evaldf = pd.read_csv(f'pybert/dataset/{i}/test_eval.csv', header=0)

datalist = {}
for j, line in enumerate(lines):
    predict = line.split(',')
    dataline = df.loc[j].tolist()
    k = 1
    p = predict[k]
    # for k, p in enumerate(predict):
    thre = evaldf.at[k, 'thresh']
    if float(p) >= thre:
        id = int(ids[j])
        if id in repo_labels.keys():
            repo_labels[id].append({i:k})
        else:
            repo_labels[id] = [{i:k}]


i = 60
with open(f'pybert/output/predict/{i}/predict.txt', 'r') as f:
    lines = f.readlines()
# testdf = pd.read_csv(f'pybert/dataset/{i}', header=0)
df = pd.read_csv(f'pybert/dataset/predict/{i}/test.csv', header=0)
ids = df[df.columns[0]]
repos = df[df.columns[1]]
contents = df[df.columns[2]]
header = df.columns.tolist()
evaldf = pd.read_csv(f'pybert/dataset/{i}/test_eval.csv', header=0)

datalist = {}
for j, line in enumerate(lines):
    predict = line.split(',')
    dataline = df.loc[j].tolist()
    k = 1
    p = predict[k]
    thre = evaldf.at[k, 'thresh']
    if float(p) >= thre:
        if k in datalist.keys():
            datalist[k].append(dataline)
        else:
            datalist[k] = [dataline]
        id = str(ids[j])
        repo_labels[id].remove({ "60": 1 })
k = 1
v = datalist[k]
totestdf = pd.DataFrame(v, columns=header)
tdir = 72
if not os.path.exists(f'pybert/dataset/predict/{tdir}'):
    os.mkdir(f'pybert/dataset/predict/{tdir}')
    with open(f'pybert/dataset/{tdir}/train.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headline = next(reader)
    tarlabels = headline[3:]
    with open(f'pybert/dataset/predict/{tdir}/labels.txt', 'w') as f:
        f.write('\n'.join(tarlabels))
totestdf.to_csv(f'pybert/dataset/predict/{tdir}/test.csv', index=False)

i = 72
cmd = f'python run_bert.py --do_predict --do_lower_case --data_name predict/{i} --resume_path pybert/output/checkpoints/{i}/bert'
process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
with open(f'pybert/output/predict/{i}/predict.txt', 'r') as f:
    lines = f.readlines()
# testdf = pd.read_csv(f'pybert/dataset/{i}', header=0)
df = pd.read_csv(f'pybert/dataset/predict/{i}/test.csv', header=0)
ids = df[df.columns[0]]
repos = df[df.columns[1]]
contents = df[df.columns[2]]
header = df.columns.tolist()
evaldf = pd.read_csv(f'pybert/dataset/{i}/test_eval.csv', header=0)


for j, line in enumerate(lines):
    predict = line.split(',')
    dataline = df.loc[j].tolist()
    for k, p in enumerate(predict):
        thre = evaldf.at[k, 'thresh']
        if float(p) >= thre:
            id = int(ids[j])
            if id in repo_labels.keys():
                repo_labels[id].append({i:k})
            else:
                repo_labels[id] = [{i:k}]



# for i in range(74):
#     if not os.path.exists(f'pybert/dataset/predict/{i}'):
#         print("no dataset:", i)
#         continue
#     if not os.path.exists(f'pybert/output/predict/{i}/predict.txt'):
#         cmd = f'python run_bert.py --do_predict --do_lower_case --data_name predict/{i} --resume_path pybert/output/checkpoints/{i}/bert'
#         process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
#         output, error = process.communicate()
#     with open(f'pybert/output/predict/{i}/predict.txt', 'r') as f:
#         lines = f.readlines()
#     # testdf = pd.read_csv(f'pybert/dataset/{i}', header=0)
#     df = pd.read_csv(f'pybert/dataset/predict/{i}/test.csv', header=0)
#     ids = df[df.columns[0]]
#     repos = df[df.columns[1]]
#     contents = df[df.columns[2]]
#     header = df.columns.tolist()
#     evaldf = pd.read_csv(f'pybert/dataset/{i}/test_eval.csv', header=0)
    
#     datalist = {}
#     for j, line in enumerate(lines):
#         predict = line.split(',')
#         dataline = df.loc[j].tolist()
#         for k, p in enumerate(predict):
#             thre = evaldf.at[k, 'thresh']
#             if float(p) >= thre:
#                 if str(i) in llist.keys() and str(k) in llist[str(i)].keys():
#                     if k in datalist.keys():
#                         datalist[k].append(dataline)
#                     else:
#                         datalist[k] = [dataline]
#                 else:
#                     id = int(ids[j])
#                     if id in repo_labels.keys():
#                         repo_labels[id].append({i:k})
#                     else:
#                         repo_labels[id] = [{i:k}]
#     for k, v in datalist.items():
#         totestdf = pd.DataFrame(v, columns=header)
#         tdir = llist[str(i)][str(k)]
#         if not os.path.exists(f'pybert/dataset/predict/{tdir}'):
#             os.mkdir(f'pybert/dataset/predict/{tdir}')
#             with open(f'pybert/dataset/{tdir}/train.csv', newline='') as csvfile:
#                 reader = csv.reader(csvfile)
#                 headline = next(reader)
#             tarlabels = headline[3:]
#             with open(f'pybert/dataset/predict/{tdir}/labels.txt', 'w') as f:
#                 f.write('\n'.join(tarlabels))
#         totestdf.to_csv(f'pybert/dataset/predict/{tdir}/test.csv', index=False)
#     print('------------------------')
for k, v in repo_labels.items():
    if not isinstance(k, int):
        print(k, v)
with open('pybert/output/predict/repo_labels_corr.json', 'w') as f:
    json.dump(repo_labels, f, indent=1)
    