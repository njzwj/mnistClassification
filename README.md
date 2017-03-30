机器学习入门101 对MNIST进行分类

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
