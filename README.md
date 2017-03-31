机器学习入门101 对MNIST进行分类

# 学习目标

+ 熟悉工作环境，并掌握这种处理数据的方法，提高使用工具的效率。
+ 简单了解MNIST的分类工作，并尝试多种参数比较训练结果的区别。

环境：Windows 10 64bit, anaconda
数据下载地址[http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)

**2017-3-31** 使用SVM One-vs-Rest对MNIST分类。(y属于{0, 1, 2}，因为电脑太慢所以只对1、2和非12分类了)
```
training...
[LibSVM].
Warning: using -h 0 may be faster
*
optimization finished, #iter = 1780
obj = -1803.101360, rho = -5.956705
nSV = 2396, nBSV = 2266
...*.*
optimization finished, #iter = 4065
obj = -3637.538415, rho = -2.994585
nSV = 4609, nBSV = 4315
*
optimization finished, #iter = 743
obj = -645.850630, rho = 3.779122
nSV = 940, nBSV = 851
Total nSV = 6873
done.
accuracy:  97.99
```

**2017-03-31 02** 用LinearSVM重新训练了一下。原来sklearn的SVC没有one-vs-the-rest功能，每次训练直接训练45个模型(n-1)*n/2。LinearSVC有ovr，不过最终结果似乎比SVC差一些。这次将LinearSVC的训练结果直接保存到`./dump/default.m`内了，可以使用`joblib`直接载入使用。
```
accuracy: 91.16
```
