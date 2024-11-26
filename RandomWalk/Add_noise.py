import cv2
import os
from walk import IrregularPatch
import time


def syn_noise(img_path, save_path):
    for filename in os.listdir(img_path):
        print(filename)
        path = os.path.join(img_path, filename)
        img = cv2.imread(path)

        # 小斑块
        # rw = IrregularPatch()
        # num = 0
        # img_noise = rw.create_multi_patch_small(img, num)

        # 中斑块
        rw = IrregularPatch()
        num = 0
        img_noise = rw.create_multi_patch_regular(img, num)

        # 大斑块
        # rw = IrregularPatch()
        # num = 0
        # img_noise = rw.create_multi_patch_big(img, num)


        cv2.imwrite(os.path.join(save_path, filename), img_noise)


if __name__ == '__main__':
    img_path = r""
    save_path = r''

    try:
        os.makedirs(save_path)
    except OSError:
        pass
    tic = time.time()
    syn_noise(img_path, save_path)
    toc = time.time()
    print('This  time {:.7f}'.format(toc - tic))
    elapsed_time = toc - tic
    output_file = 'walk_execution_time.txt'
    with open(output_file, 'a') as f:  # 使用 'a' 模式，追加写入
        f.write('This epoch take time {:.7f} seconds\n'.format(elapsed_time))