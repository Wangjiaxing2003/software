# 用vue+flask实现前后端分离计算器

| 这个作业属于哪个课程 | [ https://bbs.csdn.net/forums/ssynkqtd-05](https://bbs.csdn.net/forums/ssynkqtd-05) |
| :------------------- | :----------------------------------------------------------- |
| 这个作业要求在哪里   | [ https://bbs.csdn.net/topics/617377308](https://bbs.csdn.net/topics/617377308) |
| 这个作业的目标       | 实现前后端分离计算器                                         |
| 其他参考文献         | 无                                                           |

## 0.PSP表格

| PSP                                     | Personal Software Process Stages        | 预估耗时（分钟） | 实际耗时（分钟） |
| :-------------------------------------- | :-------------------------------------- | :--------------- | :--------------- |
| Planning                                | 计划                                    | 30               | 30               |
| • Estimate                              | • 估计这个任务需要多少时间              | 30               | 30               |
| Development                             | 开发                                    | 1400             | 1160             |
| • Analysis                              | • 需求分析 (包括学习新技术）            | 60               | 50               |
| • Design Spec                           | • 生成设计文档                          | 60               | 75               |
| • Design Review                         | • 设计复审                              | 30               | 45               |
| • Coding Standard                       | • 代码规范 (为目前的开发制定合适的规范) | 30               | 20               |
| • Design                                | • 具体设计                              | 40               | 30               |
| • Coding                                | • 具体编码                              | 1000             | 800              |
| • Code Review                           | • 代码复审                              | 60               | 60               |
| • Test                                  | • 测试（自我测试，修改代码，提交修改）  | 120              | 80               |
| Reporting                               | 报告                                    | 110              | 80               |
| • Test Repor                            | • 测试报告                              | 30               | 20               |
| • Size Measurement                      | • 计算工作量                            | 20               | 15               |
| • Postmortem & Process Improvement Plan | • 事后总结, 并提出过程改进计划          | 60               | 45               |
|                                         | 合计                                    | 1540             | 1270             |

## 1.成品展示

### 1.基础计算器功能

#### （1）基础运算

![](E:\video\cal_1.gif)

#### （2）清零回退

![](E:\video\cal_2.gif)

#### （3）错误提示

![](E:\video\cal_3.gif)

#### （4）历史记录

![](E:\video\cal_4.gif)

### 2.利率计算器

#### （1）计算存款和贷款利息

![](E:\video\cal_6.gif)

### 3.扩展功能

#### （1）前端修改存贷款利息

![](E:\video\cal_7.gif)

#### （2）科学计算器

![](E:\video\cal_5.gif)

#### （3）按钮切换计算器模式

![](E:\video\cal_8.gif)

## 2.设计实现过程

### 1.前端

前端不采用上次第一次作业时候的前端代码,这次同样是使用html+css+js实现,但不同的是采用Vue框架,设计出计算器界面图并给每个按钮添加点击事件,同时设置科学计算器切换利率计算器效果,在前端科学计算器显示历史记录和利率计算器计算利息和修改利率,通过axios向后端请求和修改数据.

### 2.后端

后端采用python的flask框架中的request来与前端的接口对接,对前端的数据请求进行处理.

### 3.数据库

数据库使用SQLite数据库,SQLite是一个进程内的轻量级嵌入式数据库，它的数据库就是一个文件，实现了自给自足、无服务器、零配置的、事务性的SQL数据库引擎。在python中，使用sqlite3创建数据库的连接.

## 3.关键代码说明

### 1.前端

1.前端采用axios框架与后端进行通信

![image-20231020233606384](C:\Users\王嘉星\AppData\Roaming\Typora\typora-user-images\image-20231020233606384.png)

2.前端计算器的切换采用vue框架自带的v-show来显示和隐藏界面,设置点击事件,当点击时便切换界面

界面:

![image-20231020233724281](C:\Users\王嘉星\AppData\Roaming\Typora\typora-user-images\image-20231020233724281.png)

切换事件:

![image-20231020233836785](C:\Users\王嘉星\AppData\Roaming\Typora\typora-user-images\image-20231020233836785.png)

### 2.后端

1.SQLite数据库初始化

![image-20231020234025762](C:\Users\王嘉星\AppData\Roaming\Typora\typora-user-images\image-20231020234025762.png)

2.数据库创建指令定义以及各个方法api设置,并且创建了一组URL路由规则，用于处理HTTP请求

![image-20231020234518957](C:\Users\王嘉星\AppData\Roaming\Typora\typora-user-images\image-20231020234518957.png)

## 4.心路历程和收获

​	这次作业最重要的点是后端部分,一开始以为后端很难,但事实上也很简单,可能是因为作业需要学习的后端部分并不多或者很简单,通过这次使用Vue框架对前端进行开发,感觉自己上次开发的计算器不堪入目.

​	总之,通过这次机会略懂了一点Vue框架和flask框架,写的过程并不是一帆风顺,通过不断测试和询问别人,最后效果感觉还可以.