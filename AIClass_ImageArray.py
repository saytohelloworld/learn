from PIL import Image
import numpy as np


def getImgArr(imgUrl):
    """
    获取图像矩阵数据
    :param imgUrl: 图像路径
    :return: 图像矩阵<ndarray>
    """

    img = Image.open(imgUrl)
    imgArr = np.array(img)

    return imgArr


def loadImgArr(imgArrUrl):
    """
    加载图像矩阵数据文件
    :param imgArrUrl: 图像矩阵文件路径
    :return: 图像矩阵<ndarray>
    """

    return np.load(imgArrUrl)


def saveImgArr(imgUrl, fileName):
    """
    保存图像矩阵数据到文件
    :param imgUrl: 图像路径
    :param fileName: 保存后的文件名
    """

    imgArr = getImgArr(imgUrl)
    np.save(fileName, imgArr)

    print('已保存图像矩阵到 %s.npy 文件' % fileName)


def convImgArr(imgArrUrl):
    """
    转换图像矩阵数据为图像对象
    :param imgArrUrl: 图像矩阵数据文件路径
    """

    imgArr = loadImgArr(imgArrUrl)
    img = Image.fromarray(imgArr)
    img.show()


if __name__ == "__main__":
    saveImgArr('a.jpg', 'a_arr')
    convImgArr('a_arr.npy')