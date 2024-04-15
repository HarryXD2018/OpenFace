import os
import argparse
import subprocess

if __name__ == '__main__':
    os.environ['OMP_NUM_THREADS'] = '1'
    os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
#     export OMP_NUM_THREADS=1
# export VECLIB_MAXIMUM_THREADS=1

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--video", type=str)
    parser.add_argument("-s", "--save", type=str)
    args = parser.parse_args()

    os.makedirs(args.save, exist_ok=True)
    subprocess.run(
        [
            '/home/zhanghaoxian/chenhejia/code/OpenFace/build/bin/FeatureExtraction', 
            '-f', args.video,
            '-out_dir', args.save
        ]
    )



