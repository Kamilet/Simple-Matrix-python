# Simple-Matrix-python
A lightweight module for simple Matrix operation. Simple and easy to use.  
轻量级的简单矩阵处理模块，使用起来比较方便。

+ English Documentation [Jump](#en)
+ 简体中文使用指南 [跳转](#cn)

***

# English Documentation
<span id = "en"> </span>  

***

# 简体中文使用指南
<span id = "cn"> </span>  
感谢查看，这是我的第一个模块，希望可以为你带来方便。  
本模块包含**1个类**和20个**函数**，包含了矩阵运算的一些基本功能。  

>特别注意：所有行号(row)和列号(column)都从0开始。
>即对于m行n列的行列式A，所有元素应该是A(0,0)到A(m-1,n-1)

以下是介绍和使用示例：(加粗的表示是个人常用的)
## 目录
+ 矩阵建设函数
    + **生成任意矩阵:** [sm_gen()](#cn_sm_gen)
    + 补全矩阵: [sm_cons()](#cn_sm_cons)
+ 单矩阵基本处理
    + **深度拷贝**: [sm_copy()](#cn_sm_copy)
    + 合法性检查: [sm_check()](#cn_sm_check)
    + 数字检查: [sm_numcheck()](#cn_sm_numcheck)
    + 所有元素转换为数字: [sm_number()](#cn_sm_number)
    + 所有元素转换为字符: [sm_str()](#cn_sm_str)
    + **所有元素加负号**: [sm_negative()](#cn_sm_negative)
    + 所有元素绝对值: [sm_abs()](#cn_sm_abs)
+ 处理单个矩阵的函数
    + **矩阵转置**: [sm_trans()](#cn_sm_trans)
    + 矩阵共轭: [sm_conj()](#cn_sm_conj)
    + 矩阵共轭转置: [sm_con_trans()](#cn_sm_con_trans)
    + **行列式运算**: [sm_det()](#cn_sm_det)
    + **逆矩阵** : [sm_inverse()](#cn_sm_inverse)
    + **代数余子式**: [sm_alge()](#cn_sm_alge)
+ 类Smartix下的函数
    + 面向对象并检查合法性: [Smatrix()](#cn_Smatrix)
    + 清空矩阵: [Smatrix().clean()](#cn_clean)
    + 检查合法性: [Smatrix().check()](#cn_check)
    + 数字检查: [Smatrix().numcheck()](#cn_numcheck)
    + **按行列输出到屏幕:** [Smatrix().view()](#cn_view)
    + 所有元素加负号: [Smatrix().negative()](#cn_negative)
    + **任意旋转**: [: [Smatrix().rotate()](#cn_rotate)
    + 转置: [Smatrix().trans()](#cn_trans)
    + 共轭: [Smatrix().conj()](#cn_conj)
    + 共轭转置: [Smatrix().con_trans()](#cn_con_trans)
    + 行列式运算: [Smatrix().det()](#cn_det)
    + 逆矩阵: [Smatrix().inverse()](#cn_inverse)
    + **在矩阵里查找某方向某长度的片段**(五子棋系统): [Smatrix().find()](#cn_find)
    + **矩阵的迹**: [Smatrix()trace()](#cn_trace)
+ 处理多个矩阵的函数
    + **多矩阵求和**: [sm_sum()](#cn_sm_sum)
    + 两矩阵相减: [sm_minus()](#cn_sm_minus)
    + **可包含纯数字的多矩阵相乘**: [sm_multis()](#cn_sm_multis)
    + 两矩阵相乘: [sm_multi_mm()](#cn_sm_multi_mm)
    + 矩阵和数字相乘: [sm_multi_mn()](#cn_sm_multi_mn)

***

## 矩阵建设函数

### 生成任意矩阵
<span id = "cn_sm_gen"> </span>  
''' python
def sm_gen(row: int = 1, colume: int = 1, items=0, unit=False, eye=False):
'''
+ row - 行数
+ colume - 列数
+ items - 用于填充的元素
+ unit
    + True - 生成单位矩阵（仅参考row）
+ eye
    + True - 生成单位矩阵（和unit相同）
返回新矩阵（列表）。

### 补全矩阵
<span id = "cn_sm_cons"> </span>  
''' python
def sm_cons(matrix, items=0, echo=0):
'''
+ matrix - 不全的矩阵，比如最后一行缺一个元素
+ items - 用于填充的元素
+ echo
    + True - 提示你运行了本函数
返回新矩阵（列表）。

***

## 单矩阵基本处理

### 深度拷贝
<span id = "cn_sm_copy"> </span>  
''' python
def sm_copy(matrix):
'''
深度拷贝这个矩阵，在你修改原矩阵的时候需要调用。  
返回新矩阵（列表）。

### 合法性检查
<span id = "cn_sm_check"> </span>  
''' python
def sm_check(matrix):
'''
检查每行的长度是否相等。  
如果是，返回行数和列数（元组），也可以用做True。
如果否，返回False。

### 数字检查
<span id = "cn_sm_numcheck"> </span>  
''' python
def sm_numcheck(matrix):
'''
检查元素是否全部为数字，包含了一个合法性检查(sm_check(matrix))。  
返回True或False。

### 所有元素转换为数字
<span id = "cn_sm_number"> </span>  
''' python
def sm_number(matrix, force=False):
'''
+ force
    + True - 将非数字元素转换为0
返回新矩阵（列表）。

### 所有元素转换为字符
<span id = "cn_sm_str"> </span>  
''' python
def sm_str(matrix):
'''
返回新矩阵（列表）。

### 所有元素加负号
<span id = "cn_sm_negative"> </span>  
''' python
def sm_negative(matrix):
'''
返回新矩阵（列表）。

### 所有元素绝对值
<span id = "cn_sm_abs"> </span>  
''' python
def sm_abs(matrix):
'''
返回新矩阵（列表）。

***

## 处理单个矩阵的函数

### 矩阵转置
<span id = "cn_sm_trans"> </span>  
''' python
def sm_trans(matrix):
'''
交换行和列。
返回新矩阵（列表）。

### 矩阵共轭
<span id = "cn_sm_conj"> </span>  
''' python
def sm_conj(matrix):
'''
返回新矩阵（列表）。

### 矩阵共轭转置
<span id = "cn_sm_con_trans"> </span>  
''' python
def sm_con_trans(matrix):
'''
返回新矩阵（列表）。

### 行列式运算
<span id = "cn_sm_det"> </span>  
''' python
def sm_det(matrix, force=False):
'''
+ force
    + True - 即便行列不相等也进行运算
    + False - 仅行列相等时运算
返回数字。

### 逆矩阵
<span id = "cn_sm_inverse"> </span>  
''' python
def sm_inverse(matrix):
'''
矩阵求逆。
返回新矩阵（列表）。

### 代数余子式
<span id = "cn_sm_alge"> </span>  
''' python
def sm_alge(matrix, row:int , colume:int):
'''
+ matrix - 用于处理的矩阵
+ row - 求余子式的元素的所在行号
+ colume - 求余子式的元素的所在列号
返回数字。

***

## 类Smartix下的函数

### 面向对象并检查合法性
<span id = "cn_Smatrix"> </span>  
''' python
class Smatrix:
def __init__(self, matrix, allnumber=False):
'''
+ allnumber
    + True - 强制进行一次sm_numcheck()数字检查
    + False - 只进行sm_check()合法性检查

### 清空矩阵
<span id = "cn_clean"> </span>  
''' python
def clean(self, items=0, echo=False):
'''
+ items - 返回的矩阵仅包含这个元素
+ echo
    + True - 告知你运行了这个函数
返回新矩阵（列表）。

### 检查合法性
<span id = "cn_check"> </span>  
''' python
def check(self):
'''
同函数sm_check()。

### 数字检查
<span id = "cn_numcheck"> </span>  
''' python
def numcheck(self):
'''
同函数sm_numbercheck()。

### 按行列输出到屏幕
<span id = "cn_view"> </span>  
''' python
def view(self):
'''
将矩阵按照行列打印出来。
无输出。

### 所有元素加负号
<span id = "cn_negative"> </span>  
''' python
def negative(self):
'''
同函数sm_negative()。

### 任意旋转
<span id = "cn_rotate"> </span>  
''' python
def rotate(self, method='exchange', step: int=1, force=False):
'''
+ method
    + exchange - 转置，交换横纵
    + ex 或 transpose 或 tr - 同上
    + clockwise - 顺时针旋转
    + clock - 同上
    + mirrorrow - 沿着行方向翻转，即水平翻转
    + mr 或 mh 或 mirror - 同上
    + mirrorcolume - 沿着列方向翻转，即垂直翻转
    + mc 或 mv - 同上
+ step - 旋转执行多少次
+ force
    + True - 如果旋转执行失败（如或输入不合法）报错
返回新矩阵（列表）。

### 转置
<span id = "cn_trans"> </span>  
''' python
def trans(self):
'''
同函数sm_trans()。

### 共轭
<span id = "cn_conj"> </span>  
''' python
def conj(self):
'''
同函数sm_conj()。

### 共轭转置
<span id = "cn_con_trans"> </span>  
''' python
def con_trans(self):
'''
同函数sm_con_trans()。

### 行列式运算
<span id = "cn_det"> </span>  
''' python
def det(self):
'''
同函数sm_det()。

### 逆矩阵
<span id = "cn_inverse"> </span>  
''' python
def inverse(self):
'''
同函数sm_inverse()。

### 在矩阵里查找某方向某长度的片段五子棋系统
<span id = "cn_find"> </span>  
''' python
def find(self, string:str='', length=2, direct='all', echo=False):
'''
将矩阵看作一个棋盘，在棋盘上寻找“连珠”的元素。
找到一个后或找不到函数将返回结束。
+ string - 被寻找的元素，为空则寻找任意连续出现的元素
+ length - 元素的长度，五子棋的话设置为5
+ direct
    + all - 在全部方向寻找
    + a - 同上
    + row - 仅在行里寻找 - 优先级：0（最高）
    + r - 同上
    + colume - 仅在列里寻找 - 优先级：1
    + c - 同上
    + rowcolume - 仅在行和列里寻找
    + rc 或 cr - 同上
    + oblique - 仅在斜方向寻找
        + 左上到右下 \\ - 优先级：2
        + 右上到左下 / - 优先级：3（最低）
    + o - 同上
+ echo
    + False - 返回True（找到）或False
    + True - 如果找到，返回连续元素起点的坐标（靠上的）
可以作为五子棋判断胜负的函数。

### 矩阵的迹
<span id = "cn_trace"> </span>  
''' python
def trace(self):
'''
计算矩阵的迹。
返回数字。

***

## 处理多个矩阵的函数

### 多矩阵求和
<span id = "cn_sm_sum"> </span>  
''' python
def sm_sum(\*matrixs, force=False):
'''
+ matrixs - 接受的矩阵，可以为2个以上
+ force
    + True - 矩阵内的空格和字母会被作为0强制处理
输入的矩阵不符合相加规则会出错。
返回新矩阵（列表）。

### 两矩阵相减
<span id = "cn_sm_minus"> </span>  
''' python
def sm_minus(matrix_1, matrix_2, force=False):
'''
+ matrixs_1 - 作为被减数的矩阵
+ matrixs_2 - 作为减数的矩阵
+ force
    + True - 矩阵内的空格和字母会被作为0强制处理
输入的矩阵不符合相加规则会出错。
返回新矩阵（列表）。

### 可包含纯数字的多矩阵相乘
<span id = "cn_sm_multis"> </span>  
''' python
def sm_multis(\*matrixs_or_numbers, force=False):
'''
+ matrixs - 接受的矩阵或数字，可以为2个以上
+ force
    + True - 矩阵内的空格和字母会被作为0强制处理
输入的矩阵不符合相乘规则会出错。
返回新矩阵（列表，即便是相乘得到数字，也会返回1x1的列表）。

### 两矩阵相乘
<span id = "cn_sm_multi_mm"> </span>  
''' python
def sm_multi_mm(matrix_1, matrix_2):
'''
+ matrixs_1 - 作为被乘数的矩阵
+ matrixs_2 - 作为乘数的矩阵
输入的矩阵不符合相乘规则会出错，不能出现非数字，如需要请主动调用sm_number()。
返回新矩阵（列表，即便是相乘得到数字，也会返回1x1的列表）。

### 矩阵和数字相乘
<span id = "cn_sm_multi_mn"> </span>  
''' python
def sm_multi_mn(matrix, number):
'''
+ matrixs_1 - 作为被乘数的矩阵
+ matrixs_2 - 作为乘数的数字
矩阵里不能出现非数字，如需要请主动调用sm_number()。
返回新矩阵（列表）
