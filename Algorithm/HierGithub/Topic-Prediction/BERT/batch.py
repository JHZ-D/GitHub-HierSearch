import subprocess
import os
for i in range(72, -1, -1):
    cmds = [f'python run_bert.py --do_data --data_name {i}', f'python run_bert.py --do_train --save_best --do_lower_case --epochs 30 --train_batch_size 16 --eval_batch_size 16 --data_name {i}  --n_gpu 0', f'python run_bert.py --do_test --do_lower_case --data_name {i}']
    for cmd in cmds:
        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print('setp:', i)
        if not os.path.exists(f'pybert/output/output/{i}'):
            os.mkdir(f'pybert/output/output/{i}')
        with open(f'pybert/output/output/{i}/log.txt', 'a') as f:
            f.write(output.decode())
            f.write('\n------------------------\n')
            if error:
                f.write(error)
        # print(output.decode())
        # print(error)
        print('------------------------')