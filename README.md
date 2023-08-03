# GET_COMMON_QQ_GROUP_MEMBERS
这份代码用于获取两个QQ群的公共成员

## Usage
# 1.修改配置文件

找到`config.py`文件，修改其中的信息

![Alt text](image-7.png)
(1)其中`User-Agent`在你的浏览器开发者工具(f12)中获取
![Alt text](image-2.png)
![Alt text](image-1.png)
![Alt text](image-3.png)
![Alt text](image-4.png)



(2)cookie在你的浏览器开发者工具(f12)中获取
首先进入[QQ群官网](https://qun.qq.com/),点击右上角登录
打开f12,按照(1)中的步骤获取cookie

![Alt text](image-5.png)

(3)按照(1)中的步骤获取`bkn`,填入config中
![Alt text](image-8.png)

找到     ![Alt text](image-9.png)

![Alt text](image-10.png)

![Alt text](image-11.png)

![Alt text](image-12.png)

(4)将两个群的qq号填入`Group_Id1`和`Group_Id2`中

# 2.运行
```bash 
python main.py

```
或使用其它IDE运行, 如pycharm或VScode

