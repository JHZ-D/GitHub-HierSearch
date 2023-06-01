import subprocess
import os
import pandas as pd
import json
import csv
# df = pd.read_csv("pybert/dataset/evaluation/0/test.csv")
# df.insert(1, "repo", "")
# df.to_csv("pybert/dataset/evaluation/0/test.csv", index=False)
for i in range(74):
    if not os.path.exists(f'pybert/output/evaluation/{i}/predict.txt'):
        if not os.path.exists(f'pybert/dataset/evaluation/{i}'):
            os.rename(f'pybert/dataset/evaluation/{i-1}', f'pybert/dataset/evaluation/{i}')
            os.system(f'cp pybert/dataset/predict/{i}/labels.txt pybert/dataset/evaluation/{i}/labels.txt')
        cmd = f'python run_bert.py --do_predict --do_lower_case --data_name evaluation/{i} --resume_path pybert/output/checkpoints/{i}/bert'
        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
    
    print('------------------------')
