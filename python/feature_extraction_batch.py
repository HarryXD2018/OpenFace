import os
from argparse import ArgumentParser
import subprocess
import shutil


def printGr(s):
    print("\033[92m{}\033[00m" .format(s))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-s", "--src", type=str, default='/ytech_data_ssd/backup_ssd_v2/upload/AR场景手势组/说话人视频裁剪/0228')
    parser.add_argument("-t", "--tgt", type=str, default='/ytech_data_ssd/m2v/zhanghaoxian/chenhejia/processed/1000H/0228')
    parser.add_argument("-f", "--fps", type=int, default=None)
    parser.add_argument("--total_process", type=int, default=1)
    parser.add_argument("--process_id", type=int, default=0)
    args = parser.parse_args()

    files = []
    for root, _, filenames in os.walk(args.src):
        for filename in filenames:
            if filename.endswith('.mp4'):
                file_path = os.path.join(root, filename)
                files.append(file_path)

    print(f'total {len(files)}')
    file_list = sorted(files)

    if args.total_process > 1:
        assert args.process_id <= args.total_process-1
        num_samples_per_process = len(file_list) // args.total_process
        if args.process_id == args.total_process-1:
            file_list = file_list[args.process_id * num_samples_per_process:]
        else:
            file_list = file_list[args.process_id * num_samples_per_process : (args.process_id+1) * num_samples_per_process]

    for idx, file in enumerate(file_list):
        printGr(f'{idx}/{len(file_list)}, \t {file}')

        save_file = file.replace(args.src, args.tgt)
        file_name = os.path.basename(file)
        save_folder = os.path.join(os.path.dirname(save_file), file_name[:-4])

        if os.path.exists(save_folder+'.csv'):
            continue
            
        subprocess.run(
            [
                'python', 'feature_extraction.py',
                '-v', file,
                '-s', save_folder
            ],
            stdout=subprocess.PIPE
        )
        # print(save_folder)
        # print(os.path.join(save_folder, file_name[:-4]+'.csv'))
        # print(save_folder+'.csv')
        try:
            shutil.copy(os.path.join(save_folder, file_name[:-4]+'.csv'), save_folder+'.csv')
        except FileNotFoundError:
            pass
        shutil.rmtree(save_folder)
        # break
