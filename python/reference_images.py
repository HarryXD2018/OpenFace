import os
import subprocess

reference_image_path = '/home/zhanghaoxian/chenhejia/reference_expressions'


if __name__ == '__main__':
    os.environ['OMP_NUM_THREADS'] = '1'
    os.environ['VECLIB_MAXIMUM_THREADS'] = '1'

    subprocess.run(
        [
            '/home/zhanghaoxian/chenhejia/code/OpenFace/build/bin/FeatureExtraction', 
            '-fdir', reference_image_path,
            '-out_dir', reference_image_path,
            '-au_static'
        ]
    )




