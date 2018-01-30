# Simple-Matrix-python
A lightweight module for simple Matrix operation. Simple and easy to use.  
轻量级的简单矩阵处理模块，使用起来比较方便。  

+ English Documentation [Jump](#english-documentation)
+ 简体中文使用指南 [转到](#简体中文使用指南)

***

# English Documentation

Thanks for checking this module.  
It's my first one. Hopefully it's useful for you.  
**1 Class** and **20 functions** are in this module,  
which will help you with basic opreations on Matrixs.  

>Please remember: All numbers of rows and columns start from ZERO.
>So a matrix 'A' with m rows and n columns,
>the last item should be 'A\[m-1\]\[n-1\]'.

Here are introductions for all functions:  

## Index

+ Matrix Building
    + **Generator:** [sm_gen()](#generator)
    + Complementor: [sm_cons()](#complementor)
+ Single Matrix Basic Opreation
    + **Deep copy**: [sm_copy()](#deep-copy)
    + Legality check: [sm_check()](#legality-check)
    + Number check: [sm_numcheck()](#number-check)
    + Convert to numbers: [sm_number()](#convert-to-numbers)
    + Convert to strings: [sm_str()](#convert-to-strings)
    + **Negative all elements**: [sm_negative()](#negative-all-elements)
    + Absolute value: [sm_abs()](#absolute-value)
+ Single Matrix Operation
    + **Matrix transpose**: [sm_trans()](#matrix-transpose)
    + Matrix conjugate: [sm_conj()](#matrix-conjugate)
    + Matrix conjugate transpose: [sm_con_trans()](#matrix-conjugate-transpose)
    + **Determinant**: [sm_det()](#determinant)
    + **Inverse Matrix** : [sm_inverse()](#inverse-Matrix)
    + **Algebraic Remainder**: [sm_alge()](#algebraic-Remainder)
+ Class Smartix()
    + OO Legality check: [Smatrix()](#oo-legality-check)
    + Clean Matrix: [Smatrix().clean()](#clean-matrix)
    + OO Legality check: [Smatrix().check()](#oo-legality-check-1)
    + OO Number check: [Smatrix().numcheck()](#oo-number-check)
    + **Print by rows**: [Smatrix().view()](#print-by-rows)
    + OO Negative all elements: [Smatrix().negative()](#oo-Negative-all-elements)
    + **Rotate**: [: [Smatrix().rotate()](#rotate)
    + Transpose: [Smatrix().trans()](#transpose)
    + Conjugate: [Smatrix().conj()](#conjugate)
    + Conjugate transpose: [Smatrix().con_trans()](#conjugate-transpose)
    + OO Determinant: [Smatrix().det()](#oo-determinant)
    + Inverse: [Smatrix().inverse()](#inverse)
    + **Find a segment of a certain length in the matrix (Gomoku system)**: [Smatrix().find()](#find-a-segment-of-a-certain-length-in-the-matrix)
    + **Matrix trace**: [Smatrix()trace()](#matrix-trace)
+ Multiple Matrix Operation
    + **Sum All**: [sm_sum()](#sum-all)
    + Subtraction: [sm_minus()](#subtraction)
    + **Multiplication with matrixs and numbers**: [sm_multis()](#multiplication-with-matrixs-and-numbers)
    + Multiply: [sm_multi_mm()](#multiply)
    + Multiply with number: [sm_multi_mn()](#multiply-with-number)

***

## Matrix Building

#### Generator
```python
def sm_gen(row: int = 1, colume: int = 1, items=0, unit=False, eye=False):
```
+ row - Number of row, for A(m\*n) you need set to m
+ colume - Number of colume, for A(m\*n) you need set to n
+ items - For filling
+ unit
    + True - Generate a unit matrix: row\*row
+ eye
    + True - Ditto
Return a new matrix(list).

#### Complementor
```python
def sm_cons(matrix, items=0, echo=0):
```
+ matrix - A matrix need to be complement. For example:\[\[1,2\],\[1\]\]
+ items - For filling
+ echo
    + True - Tell you are running complementor
Return a new matrix(list).

***

## Single Matrix Basic Opreation

#### Deep copy
```python
def sm_copy(matrix):
```
Deep copy, just use it whenever you need change original matrix.  
Return a new matrix(list).

#### Legality check
```python
def sm_check(matrix):
```
Check if every rows are in same length.  
If True, return a tuple as (row, column), you can use as bool.  

#### Number check
```python
def sm_numcheck(matrix):
```
Check if all items are numbers. Run a sm_check() automatically.   
Return True or false.  

#### Convert to numbers
```python
def sm_number(matrix, force=False):
```
+ force
    + True - Letters and '' will be 0
Return a new matrix(list).

#### Convert to strings
```python
def sm_str(matrix):
```
Return a new matrix(list).

#### Negative all elements
```python
def sm_negative(matrix):
```
Return a new matrix(list).

#### Absolute value
```python
def sm_abs(matrix):
```
Return a new matrix(list).

***

## Single Matrix Operation

#### Matrix transpose
```python
def sm_trans(matrix):
```
Exchange lines and columns.  
Return a new matrix(list).

#### Matrix conjugate
```python
def sm_conj(matrix):
```
Return a new matrix(list).

#### Matrix conjugate transpose
```python
def sm_con_trans(matrix):
```
Return a new matrix(list).

#### Determinant
```python
def sm_det(matrix, force=False):
```
+ force
    + True - opreat even low != column
    + False - only opreat when low == column
Return a number.

#### Inverse Matrix
```python
def sm_inverse(matrix):
```
Return a new matrix(list).

#### Algebraic Remainder
```python
def sm_alge(matrix, row:int , colume:int):
```
+ row - the row should be ignored
+ colume - the colume should be ignored
Return a number.

***

## Class Smartix()

#### OO Legality check 
```python
class Smatrix:
def __init__(self, matrix, allnumber=False):
```
+ allnumber
    + True - run sm_numcheck()
    + False - only sm_check()

#### Clean Matrix
```python
def clean(self, items=0, echo=False):
```
+ items - clean with this
+ echo
    + True - tell you it's cleaned
Return a new matrix(list).

#### OO Legality check 1
```python
def check(self):
```
Same function as sm_check().

#### OO Number check
```python
def numcheck(self):
```
Same function as sm_numbercheck().

#### Print by rows
```python
def view(self):
```
Just pring, no return.

#### OO Negative all elements
```python
def negative(self):
```
Same function as sm_negative().

#### Rotate
```python
def rotate(self, method='exchange', step: int=1, force=False):
```
+ method
    + exchange - Exchange rows and columns
    + ex | transpose | tr - Ditto
    + clockwise - Rotate in clockwise direction
    + clock - Ditto
    + mirrorrow - mirror in horizontal direction
    + mr | mh | mirror - Ditto
    + mirrorcolume - mirror in vertical direction
    + mc | mv - Ditto
+ step - How many times to run
+ force
    + True - If unsuccessful, an error will be asserted
Return a new matrix(list).

#### Transpose
```python
def trans(self):
```
Same function as sm_trans().

#### Conjugate
```python
def conj(self):
```
Same function as sm_conj().

#### Conjugate transpose
```python
def con_trans(self):
```
Same function as sm_con_trans().

#### OO Determinant
```python
def det(self):
```
Same function as sm_det().

#### Inverse
```python
def inverse(self):
```
Same function as sm_inverse().

#### Find a segment of a certain length in the matrix
```python
def find(self, string:str='', length=2, direct='all', echo=False):
```
Try to fin a segment that repeats, such as \['4','4','4'\] in any direction!
+ string - The single string, can be a number
+ length - How many times repeats
+ direct
    + all - All direction
    + a - Ditto
    + row - Only search in rows - Priority: 0 (hightest)
    + r - Ditto
    + colume - Only search in columes - Priority: 1
    + c - Ditto
    + rowcolume - Only search in rows and columes
    + rc | cr - Ditto
    + oblique - Only search in oblique direction
        + the \\ - Priority: 2
        + the / - Priority: 3 (lowest)
    + o - Ditto
+ echo
    + False - Return True if find one
    + True - Return (row, column) as the start point of first match

You should know a game called Gobang,  
this function can be used to determine the outcome.  
Of course, Othello is also ok.

#### Matrix trace
```python
def trace(self):
```
Return a number.

***

## Multiple Matrix Operation

#### Sum All
```python
def sm_sum(\*matrixs, force=False):
```
+ matrixs - can be two or more matrixs
+ force
    + True - Set '' or SPACE to 0
Error occurs with violated algorithm.  
Return a new matrix(list).

#### Subtraction
```python
def sm_minus(matrix_1, matrix_2, force=False):
```
+ matrixs_1 - first matrix
+ matrixs_2 - second matrix
+ force
    + True - Set '' or SPACE to 0
Error occurs with violated algorithm.  
Return a new matrix(list).

#### Multiplication with matrixs and numbers
```python
def sm_multis(\*matrixs_or_numbers, force=False):
```
+ matrixs - can be two or more matrixs and numbers
+ force
    + True - Set '' or SPACE to 0
Error occurs with violated algorithm.  
Return a new matrix(list, even only one number).

#### Multiply
```python
def sm_multi_mm(matrix_1, matrix_2):
```
+ matrixs_1 - first matrix
+ matrixs_2 - second matrix
Error occurs with violated algorithm. Use sm_number() if you need.  
Return a new matrix(list, even only one number).

#### Multiply with number
```python
def sm_multi_mn(matrix, number):
```
+ matrixs_1 - first matrix
+ matrixs_2 - anumber
Use sm_number() if you need.  
Return a new matrix(list).

***

# 简体中文使用指南

感谢查看，这是我的第一个模块，希望可以为你带来方便。  
本模块包含**1个类**和20个**函数**，包含了矩阵运算的一些基本功能。  

>特别注意：所有行号(row)和列号(column)都从0开始。
>即对于m行n列的行列式A，所有元素应该是A(0,0)到A(m-1,n-1)

以下是介绍和使用方式：(加粗的表示是个人常用的)

## 目录

+ 矩阵建设函数
    + **生成任意矩阵:** [sm_gen()](#生成任意矩阵)
    + 补全矩阵: [sm_cons()](#补全矩阵)
+ 单矩阵基本处理
    + **深度拷贝**: [sm_copy()](#深度拷贝)
    + 合法性检查: [sm_check()](#合法性检查)
    + 数字检查: [sm_numcheck()](#数字检查)
    + 所有元素转换为数字: [sm_number()](#所有元素转换为数字)
    + 所有元素转换为字符: [sm_str()](#所有元素转换为数字)
    + **所有元素加负号**: [sm_negative()](#所有元素加负号)
    + 所有元素绝对值: [sm_abs()](#所有元素绝对值)
+ 处理单个矩阵的函数
    + **矩阵转置**: [sm_trans()](#矩阵转置)
    + 矩阵共轭: [sm_conj()](#矩阵共轭)
    + 矩阵共轭转置: [sm_con_trans()](#矩阵共轭转置)
    + **行列式运算**: [sm_det()](#行列式运算)
    + **逆矩阵** : [sm_inverse()](#逆矩阵)
    + **代数余子式**: [sm_alge()](#代数余子式)
+ 类Smartix下的函数
    + 面向对象并检查合法性: [Smatrix()](#面向对象并检查合法性)
    + 清空矩阵: [Smatrix().clean()](#清空矩阵)
    + 检查合法性: [Smatrix().check()](#检查合法性)
    + 数字检查: [Smatrix().numcheck()](#数字检查)
    + **按行列输出到屏幕:** [Smatrix().view()](#按行列输出到屏幕)
    + 所有元素加负号: [Smatrix().negative()](#所有元素加负号)
    + **任意旋转**: [: [Smatrix().rotate()](#任意旋转)
    + 转置: [Smatrix().trans()](#转置)
    + 共轭: [Smatrix().conj()](#共轭)
    + 共轭转置: [Smatrix().con_trans()](#共轭转置)
    + 行列式运算: [Smatrix().det()](#行列式运算)
    + 逆矩阵: [Smatrix().inverse()](#逆矩阵)
    + **在矩阵里查找某方向某长度的片段**(五子棋系统): [Smatrix().find()](#在矩阵里查找某方向某长度的片段)
    + **矩阵的迹**: [Smatrix()trace()](#矩阵的迹)
+ 处理多个矩阵的函数
    + **多矩阵求和**: [sm_sum()](#多矩阵求和)
    + 两矩阵相减: [sm_minus()](#两矩阵相减)
    + **可包含纯数字的多矩阵相乘**: [sm_multis()](#可包含纯数字的多矩阵相乘)
    + 两矩阵相乘: [sm_multi_mm()](#两矩阵相乘)
    + 矩阵和数字相乘: [sm_multi_mn()](#矩阵和数字相乘)

***

## 矩阵建设函数

#### 生成任意矩阵
<span id = "cn_sm_gen"></span>  
```python
def sm_gen(row: int = 1, colume: int = 1, items=0, unit=False, eye=False):
```
+ row - 行数
+ colume - 列数
+ items - 用于填充的元素
+ unit
    + True - 生成单位矩阵（仅参考row）
+ eye
    + True - 生成单位矩阵（和unit相同）
返回新矩阵（列表）。

#### 补全矩阵
<span id = "cn_sm_cons"></span>  
```python
def sm_cons(matrix, items=0, echo=0):
```
+ matrix - 不全的矩阵，比如最后一行缺一个元素
+ items - 用于填充的元素
+ echo
    + True - 提示你运行了本函数
返回新矩阵（列表）。

***

## 单矩阵基本处理

#### 深度拷贝
<span id = "cn_sm_copy"></span>  
```python
def sm_copy(matrix):
```
深度拷贝这个矩阵，在你修改原矩阵的时候需要调用。  
返回新矩阵（列表）。

#### 合法性检查
<span id = "cn_sm_check"></span>  
```python
def sm_check(matrix):
```
检查每行的长度是否相等。  
如果是，返回行数和列数（元组），也可以用做True。  
如果否，返回False。

#### 数字检查
<span id = "cn_sm_numcheck"></span>  
```python
def sm_numcheck(matrix):
```
检查元素是否全部为数字，包含了一个合法性检查(sm_check(matrix))。  
返回True或False。

#### 所有元素转换为数字
<span id = "cn_sm_number"></span>  
```python
def sm_number(matrix, force=False):
```
+ force
    + True - 将非数字元素转换为0
返回新矩阵（列表）。

#### 所有元素转换为字符
<span id = "cn_sm_str"></span>  
```python
def sm_str(matrix):
```
返回新矩阵（列表）。

#### 所有元素加负号
<span id = "cn_sm_negative"></span>  
```python
def sm_negative(matrix):
```
返回新矩阵（列表）。

#### 所有元素绝对值
<span id = "cn_sm_abs"></span>  
```python
def sm_abs(matrix):
```
返回新矩阵（列表）。

***

## 处理单个矩阵的函数

#### 矩阵转置
<span id = "cn_sm_trans"></span>  
```python
def sm_trans(matrix):
```
交换行和列。  
返回新矩阵（列表）。

#### 矩阵共轭
<span id = "cn_sm_conj"></span>  
```python
def sm_conj(matrix):
```
返回新矩阵（列表）。

#### 矩阵共轭转置
<span id = "cn_sm_con_trans"></span>  
```python
def sm_con_trans(matrix):
```
返回新矩阵（列表）。

#### 行列式运算
<span id = "cn_sm_det"></span>  
```python
def sm_det(matrix, force=False):
```
+ force
    + True - 即便行列不相等也进行运算
    + False - 仅行列相等时运算
返回数字。

#### 逆矩阵
<span id = "cn_sm_inverse"></span>  
```python
def sm_inverse(matrix):
```
矩阵求逆。
返回新矩阵（列表）。

#### 代数余子式
<span id = "cn_sm_alge"></span>  
```python
def sm_alge(matrix, row:int , colume:int):
```
+ matrix - 用于处理的矩阵
+ row - 求余子式的元素的所在行号
+ colume - 求余子式的元素的所在列号
返回数字。

***

## 类Smartix下的函数

#### 面向对象并检查合法性
<span id = "cn_Smatrix"></span>  
```python
class Smatrix:
def __init__(self, matrix, allnumber=False):
```
+ allnumber
    + True - 强制进行一次sm_numcheck()数字检查
    + False - 只进行sm_check()合法性检查

#### 清空矩阵
<span id = "cn_clean"></span>  
```python
def clean(self, items=0, echo=False):
```
+ items - 返回的矩阵仅包含这个元素
+ echo
    + True - 告知你运行了这个函数
返回新矩阵（列表）。

#### 检查合法性
<span id = "cn_check"></span>  
```python
def check(self):
```
同函数sm_check()。

#### 数字检查
<span id = "cn_numcheck"></span>  
```python
def numcheck(self):
```
同函数sm_numbercheck()。

#### 按行列输出到屏幕
<span id = "cn_view"></span>  
```python
def view(self):
```
将矩阵按照行列打印出来。
无输出。

#### 所有元素加负号
<span id = "cn_negative"></span>  
```python
def negative(self):
```
同函数sm_negative()。

#### 任意旋转
<span id = "cn_rotate"></span>  
```python
def rotate(self, method='exchange', step: int=1, force=False):
```
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

#### 转置
<span id = "cn_trans"></span>  
```python
def trans(self):
```
同函数sm_trans()。

#### 共轭
<span id = "cn_conj"></span>  
```python
def conj(self):
```
同函数sm_conj()。

#### 共轭转置
<span id = "cn_con_trans"></span>  
```python
def con_trans(self):
```
同函数sm_con_trans()。

#### 行列式运算
<span id = "cn_det"></span>  
```python
def det(self):
```
同函数sm_det()。

#### 逆矩阵
<span id = "cn_inverse"></span>  
```python
def inverse(self):
```
同函数sm_inverse()。

#### 在矩阵里查找某方向某长度的片段
<span id = "cn_find"></span>  
```python
def find(self, string:str='', length=2, direct='all', echo=False):
```
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

#### 矩阵的迹
<span id = "cn_trace"></span>  
```python
def trace(self):
```
计算矩阵的迹。
返回数字。

***

## 处理多个矩阵的函数

#### 多矩阵求和
<span id = "cn_sm_sum"></span>  
```python
def sm_sum(\*matrixs, force=False):
```
+ matrixs - 接受的矩阵，可以为2个以上
+ force
    + True - 矩阵内的空格和字母会被作为0强制处理
输入的矩阵不符合相加规则会出错。  
返回新矩阵（列表）。

#### 两矩阵相减
<span id = "cn_sm_minus"></span>  
```python
def sm_minus(matrix_1, matrix_2, force=False):
```
+ matrixs_1 - 作为被减数的矩阵
+ matrixs_2 - 作为减数的矩阵
+ force
    + True - 矩阵内的空格和字母会被作为0强制处理
输入的矩阵不符合相加规则会出错。  
返回新矩阵（列表）。

#### 可包含纯数字的多矩阵相乘
<span id = "cn_sm_multis"></span>  
```python
def sm_multis(\*matrixs_or_numbers, force=False):
```
+ matrixs - 接受的矩阵或数字，可以为2个以上
+ force
    + True - 矩阵内的空格和字母会被作为0强制处理
输入的矩阵不符合相乘规则会出错。  
返回新矩阵（列表，即便是相乘得到数字，也会返回1x1的列表）。

#### 两矩阵相乘
<span id = "cn_sm_multi_mm"></span>  
```python
def sm_multi_mm(matrix_1, matrix_2):
```
+ matrixs_1 - 作为被乘数的矩阵
+ matrixs_2 - 作为乘数的矩阵
输入的矩阵不符合相乘规则会出错，不能出现非数字，如需要请主动调用sm_number()。  
返回新矩阵（列表，即便是相乘得到数字，也会返回1x1的列表）。

#### 矩阵和数字相乘
<span id = "cn_sm_multi_mn"></span>  
```python
def sm_multi_mn(matrix, number):
```
+ matrixs_1 - 作为被乘数的矩阵
+ matrixs_2 - 作为乘数的数字
矩阵里不能出现非数字，如需要请主动调用sm_number()。  
返回新矩阵（列表）
