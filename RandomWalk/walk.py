from random import choice
import numpy as np


class IrregularPatch:
    """一个生成随机数漫步的类"""

    # patch_size 表示每个斑块的大小
    def create_multi_patch_small(self, image, num):
        for i in range(0, num):
            patch_size = np.random.randint(1, 15)
            image = self.create_one_patch(image, patch_size)
        return image

    def create_multi_patch_regular(self, image, num):
        for i in range(0, num):
            patch_size = np.random.randint(16, 70)
            image = self.create_one_patch(image, patch_size)
        return image

    def create_multi_patch_big(self, image, num):
        for i in range(0, num):
            patch_size = np.random.randint(71, 140)
            image = self.create_one_patch(image, patch_size)
        return image

    # 计算随机漫步的所有点
    def create_one_patch(self, image, patch_size):
        h, w = image.shape[0], image.shape[1]

        # 记录每次漫步时原点坐标，每漫步一次数组+1
        x_lab = []
        y_lab = []

        # 随机选取一点作为起始坐标
        x_lab.append(np.random.randint(5, h - 5))
        y_lab.append(np.random.randint(5, w - 5))

        # 随机漫步的步数等于斑块的像素点个数
        steps = patch_size
        count = 0
        while count < steps:
            # 决定前进方向以及前进的距离
            x_direction = choice([1, -1])
            x_distance = 1
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = 1
            y_step = y_direction * y_distance

            # 拒绝原地不动
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点X和Y的值
            next_x = x_lab[-1] + x_step
            next_y = y_lab[-1] + y_step

            # 边界限制不能超出范围
            if ((0 < next_x < h and 0 < next_y < w) and
                (0 < next_x - 1 < h and 0 < next_y - 1 < w) and
                (0 < next_x + 1 < h and 0 < next_y + 1 < w)):

                # 每一次漫步的风格，围绕原点进行随机填充，随机填充的个数随机的
                # 由于个数不同，每次漫步的风格是不同的
                loop = np.random.randint(0, 9)

                for index in range(0, loop):

                    # 填充的位置坐标
                    index = np.random.randint(0, 9)

                    if index == 0:
                        if self.is_not_white(image, next_x, next_y):
                            image[next_x, next_y] = 255
                            count = count + 1
                    elif index == 1:
                        if self.is_not_white(image, next_x - 1, next_y - 1):
                            image[next_x - 1, next_y - 1] = 255
                            count = count + 1
                    elif index == 2:
                        if self.is_not_white(image, next_x - 1, next_y):
                            image[next_x - 1, next_y] = 255
                            count = count + 1
                    elif index == 3:
                        if self.is_not_white(image, next_x - 1, next_y + 1):
                            image[next_x - 1, next_y + 1] = 255
                            count = count + 1
                    elif index == 4:
                        if self.is_not_white(image, next_x, next_y - 1):
                            image[next_x, next_y - 1] = 255
                            count = count + 1
                    elif index == 5:
                        if self.is_not_white(image, next_x, next_y + 1):
                            image[next_x, next_y + 1] = 255
                            count = count + 1
                    elif index == 6:
                        if self.is_not_white(image, next_x + 1, next_y - 1):
                            image[next_x + 1, next_y - 1] = 255
                            count = count + 1
                    elif index == 7:
                        if self.is_not_white(image, next_x + 1, next_y):
                            image[next_x + 1, next_y] = 255
                            count = count + 1
                    elif index == 8:
                        if self.is_not_white(image, next_x + 1, next_y + 1):
                            image[next_x + 1, next_y + 1] = 255
                            count = count + 1

                x_lab.append(next_x)
                y_lab.append(next_y)

        return image

    def is_not_white(self, image, y, x):
        pixel = image[y, x]
        if all(pixel == [255, 255, 255]):
            return False
        else:
            return True
