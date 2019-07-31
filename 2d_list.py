#coding:utf-8
"""
问题
定义一个20*5的二维数组，用来存储某班级20位学员的5门课的成绩；这5门课按存储顺序依次为：core C++，coreJava，Servlet，JSP和EJB。
（1）循环给二维数组的每一个元素赋0~100之间的随机整数。
（2）按照列表的方式输出这些学员的每门课程的成绩。
（3）要求编写程序求每个学员的总分，将其保留在另外一个一维数组中。
（4）要求编写程序求所有学员的某门课程的平均分。
"""

#使用numpy来做二维数组
import numpy as np

score = np.random.randint(100,size=(20,5))
#查看所有的函数dir(np.random)
#help(np.random.randint)

#求每一行的汇总值
total = score.sum(axis=1)
#求每一列的平均值
mean = score.mean(axis=0)