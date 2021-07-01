## 项目说明

项目通过TF2.0来构建卷积神经网络实现字符识别。

### 项目的配套文章

回头有空我会把项目的大概原理写成文章发我的[博客](https://zlxt.gitee.io/)上。

---

## 文件夹说明

1. CNN_Train 中是CNN模型训练文件
2. Fuse_NoGUI_ver01 中是我完成的程序初版，没有程序界面，但是源码思路阅比较清晰，易于阅读。
3. Fuse_GUI_ver01 中是有GUI的版本，运行起来好看点，但源码不易于阅读。

## 运行环境

各软件的版本是：

> Python 3.7
>
> TF2.0
>
> OpenCV
>
> QT
>
> Python对应的库

#### CNN模型训练文件

在使用时需要先下载对应的训练图片集。一共有两个，一个是标准[MINST数据集](https://zlxt.lanzoui.com/icwotob)，另外一个是[我自己手写收集的训练集](https://zlxt.lanzoui.com/icwottg)。如果需要收集自己的手写数字图片，可以使用Collect_Pictures.py。

运行前，代码需要修改图像的路径。

#### Fuse_NoGUI_ver01

推荐阅读这个版本的源码，思路清晰明了，没有GUI界面程序来干扰思路。

#### Fuse_GUI_ver01

不推荐这个版本的源码，引入GUI不仅加大了程序的难度，也多了与图像处理和深度学习无关的程序。

