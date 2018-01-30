#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
A lightweight module for handling Matrix.
Built For Real Number.
Plural actually available, but complete test haven't done...
All items should be numbers or letters in matrix.
Please use Numpy for more complex situation!
'''

# ########################## Instruction ################################
# put it in your floder and use like this:
# from sMartix import *
# then you can use it! simple :)

# ########################## Information ################################
# bug report: https://github.com/Kamilet/Simple-Matrix-python
# document: https://github.com/Kamilet/Simple-Matrix-python#cn_sm_gen
# email: hi@kmailet.cn

__author__ = 'Kamilet <hi@kamilet.cn>'
__version__ = '0.8a'  # lastchanged: 2018-01-06
__all__ = ['sm_gen', 'sm_cons', 'sm_copy', 'Smatrix', 'sm_numcheck',
           'sm_check', 'sm_negative', 'sm_abs', 'sm_number', 'sm_str',
           'sm_trans', 'sm_conj', 'sm_con_trans', 'sm_det', 'sm_inverse',
           'sm_alge', 'sm_sum', 'sm_minus', 'sm_multis',
           'sm_multi_mm', 'sm_multi_mn']


# -------------------------------------------------------
# Handle with single matrix
# -------------------------------------------------------


def sm_gen(row: int = 1, colume: int = 1, items=0, unit=False, eye=False):
    '''Generate a matrix with row and colume,
    items can be numbers or string (can't calculate)
    set unit=True or eye=True to generate a unit matrix with row: sm_gen(row, eye=True)'''
    if unit or eye:
        matrix = sm_gen(row, row, items=0)
        for i in range(row):
            matrix[i][i] = 1
    else:
        matrix = [None] * row
        for _r in range(row):
            matrix[_r] = [items] * colume
    return matrix


def sm_cons(matrix, items=0, echo=0):
    '''Construct a matrix, for example:
    if matrix is [[1,2],[1]], would return [[1,2],[1,items]]
    the first row and colume must exist
    and any item like '' will be items'''
    if echo:
        print('Your matrix will be full filled by:', items)
    _row = len(matrix)
    _colume = len(matrix[0])
    new_matrix = sm_gen(_row, _colume, items)
    for _r in range(0, _row):
        for _c in range(0, _colume):
            try:
                new_matrix[_r][_c] == matrix[_r][_c]
            except:
                pass
    return new_matrix


def sm_copy(matrix):
    '''perform a deep copy for matrix'''
    _row = len(matrix)
    _colume = len(matrix[0])
    new_matrix = sm_gen(_row, _colume)
    for _r in range(_row):
        for _c in range(_colume):
            new_matrix[_r][_c] = matrix[_r][_c]
    return new_matrix


def sm_numcheck(matrix):
    '''Check is matrix is legal.
    And all items must be number.'''
    if not sm_check(matrix):
        return False
    _colume = len(matrix[0])
    for items in matrix:
        for _c in range(_colume):
            try:
                _temp = eval(str(items[_c]))
            except NameError:
                return False
            except TypeError:  # new for plural, wrong input will cause Eror
                pass
    return True


def sm_check(matrix):
    '''Check if the row and colume >=1
    Check if all row has same length'''
    try:
        _row = len(matrix)
        _colume = len(matrix[0])
        if _colume:
            for items in matrix:
                if len(items) != _colume:
                    return False
            return _row, _colume
        else:
            return False
    except IndexError:
        return False


def sm_negative(matrix):
    '''Set every numbers to -(number)'''
    if sm_numcheck(matrix):
        new_matrix = sm_copy(matrix)
        new_matrix = sm_number(new_matrix)
        for _r in range(len(new_matrix)):
            for _c in range((len(new_matrix[0]))):
                new_matrix[_r][_c] *= -1
        return new_matrix
    else:
        assert False, 'Error: Your matrix is not all numbers'


def sm_abs(matrix):
    '''set every numbers to abs(number)'''
    if sm_numcheck(matrix):
        new_matrix = sm_copy(matrix)
        new_matrix = sm_number(new_matrix)
        for _r in range(len(new_matrix)):
            for _c in range((len(new_matrix[0]))):
                new_matrix[_r][_c] = abs(new_matrix[_r][_c])
        return new_matrix
    else:
        assert False, 'Error: Your matrix is not all numbers'


def sm_number(matrix, force=False):
    '''set every numbers to numbertype
    set force=True will replace letters and '' with 0'''
    new_matrix = sm_copy(matrix)
    for _r in range(len(new_matrix)):
        for _c in range((len(new_matrix[0]))):
            try:
                new_matrix[_r][_c] = eval(str(new_matrix[_r][_c]))
            except NameError:
                assert force, 'Error: Your matrix is not all numbers!\n\
You can try to use force=True for argument in function like:sm_number(matrix, force).'
                new_matrix[_r][_c] = 0
            except TypeError:  # new for plural, wrong input will cause Eror
                pass
    return new_matrix


def sm_str(matrix):
    '''set every items to string type'''
    new_matrix = sm_copy(matrix)
    for _r in range(len(new_matrix)):
        for _c in range((len(new_matrix[0]))):
            new_matrix[_r][_c] = str(new_matrix[_r][_c])
    return new_matrix


def sm_trans(matrix):
    '''Transpose'''
    _row, _colume = sm_check(matrix)
    new_matrix = sm_gen(_colume, _row)
    for _r in range(_row):
        for _c in range(_colume):
            new_matrix[_c][_r] = matrix[_r][_c]
    return new_matrix


def sm_conj(matrix):
    '''Conjugation'''
    _row, _colume = sm_check(matrix)
    new_matrix = sm_gen(_row, _colume)
    for _r in range(_row):
        for _c in range(_colume):
            if matrix[_r][_c].imag != 0:
                new_matrix[_r][_c] = matrix[_r][
                    _c].real - matrix[_r][_c].imag * 1j
            else:
                new_matrix[_r][_c] = matrix[_r][_c].real
    return new_matrix


def sm_con_trans(matrix):
    '''Conjugation transpose'''
    _row, _colume = sm_check(matrix)
    new_matrix = sm_gen(_colume, _row)
    for _r in range(_row):
        for _c in range(_colume):
            if matrix[_r][_c].imag != 0:
                new_matrix[_c][_r] = matrix[_r][
                    _c].real - matrix[_r][_c].imag * 1j
            else:
                new_matrix[_c][_r] = matrix[_r][_c].real
    return new_matrix


def sm_det(matrix):
    '''Determinant, return a number'''
    _row, _colume = sm_check(matrix)
    _det = 0
    if not _row == _colume or not sm_numcheck(matrix):
        assert False, 'Error: Your matrix is illegal for Det(A)'
    if _row == 1 and _colume == 1:
        return matrix[0][0]
    else:
        _det = 0
        for i in range(_row):
            n = [[row[a] for a in range(_row) if a != i] for row in matrix[1:]]
            _det += matrix[0][i] * sm_det(n) * (-1) ** (i % 2)
        return _det


def sm_inverse(matrix):
    '''Inverse matrix'''
    _row, _colume = sm_check(matrix)
    if _row != _colume or not sm_numcheck(matrix):
        assert False, 'Error: Your matrix is illegal for Inverse(A)'
    _det = sm_det(matrix)
    if _det == 0:
        assert False, 'Error: Your matrix is illegal for Inverse(A)'
    new_matrix = sm_gen(_row, _colume)
    for _r in range(_row):
        for _c in range(_colume):
            new_matrix[_c][_r] = sm_alge(matrix, _r, _c) / _det
    return new_matrix


def sm_alge(matrix, row: int, colume: int):
    '''algebraic cofactor'''
    _row, _colume = sm_check(matrix)
    new_matrix = sm_gen(_row-1, _colume-1)
    _rownum = list(range(_row))
    _columenum = list(range(_colume))
    del _rownum[row]
    del _columenum[colume]
    for _r in range(_row-1):
        for _c in range(_colume-1):
            new_matrix[_r][_c] = matrix[_rownum[_r]][_columenum[_c]]
    return sm_det(new_matrix) * (-1) ** (row+colume)


class Smatrix:
    '''handdel a single matrix'''

    def __init__(self, matrix, allnumber=False):
        '''an error check will run automaticlly'''
        self.matrix = matrix
        _check = sm_check(matrix)
        if _check:
            self.colume = _check[1]  # len(matrix)
            self.row = _check[0]  # len(matrix[0])
        else:
            assert False, 'Error: Your matrix is illegal'
        if allnumber and not sm_numcheck(matrix):
            assert False, 'Error: Your matrix is illegal'

    def clean(self, items=0, echo=False):
        '''clear a matrix with 0 as defult'''
        if echo:
            print('Your items in matrix has been replaced with:', items)
        return sm_gen(self.row, self.colume, items)

    def check(self):
        '''Check if the row and colume >=1
        Check if all row has same length'''
        return sm_check(self.matrix)

    def numcheck(self):
        '''Check is matrix is legal.
        And all items must be number.'''
        return sm_numcheck(self.matrix)

    def view(self):
        '''view the matrix'''
        for item in self.matrix:
            print(item)

    def negative(self):
        '''Set every numbers to -(number)'''
        return sm_negative(self.matrix)

    def rotate(self, method='exchange', step: int=1, force=False):
        '''rotate a matrix, set strp to act serveral tiems, set method to:
        - transpose:(or exchange | or ex | or tr) exchange rows and columes
        - clockwise:(or clock) rotate it in clockwise
        - mirrorrow:(or mr | or mh | or mirror) mirror in horizontal direction
        - mirrorcolume:(or mc | or mv) mirror in vertical
        set force=True will assert Error when no opreation happened'''
        new_matrix = sm_copy(self.matrix)
        if method in ['transpose', 'exchange', 'ex', 'tr']:
            step %= 2
            while step:
                step -= 1
                new_matrix = sm_gen(self.colume, self.row, '')
                # _row and _colume here for new_matrix
                for _row in range(self.colume):
                    for _colume in range(self.row):
                        new_matrix[_row][_colume] = self.matrix[_colume][_row]
        elif method == 'clockwise' or method == 'clock':
            step %= 4
            while step:
                step -= 1
                o_colume = len(new_matrix[0])
                o_row = len(new_matrix)
                o_matrix = new_matrix
                new_matrix = sm_gen(o_colume, o_row, '')
                for _row in range(o_colume):
                    for _colume in range(o_row):
                        new_matrix[_row][_colume] = o_matrix[
                            o_row - _colume - 1][_row]
        elif method in ['mirrorrow', 'mr', 'mh', 'mirror']:
            step %= 2
            while step:
                step -= 1
                for _row in range(self.row):
                    new_matrix[_row] = new_matrix[_row][::-1]
        elif method in ['mirrorcolume', 'mc', 'mv']:
            step %= 2
            while step:
                step -= 1
                for line in range(0, self.row // 2):
                    new_matrix[line], new_matrix[self.row - line - 1] =\
                        new_matrix[self.row - line - 1], new_matrix[line]
        elif force:
            assert False, 'Error: rotate(method={}, step={})'.format(
                method, step)
        return new_matrix

    def trans(self):
        '''transpose, same as rotate(matrix, transpose)'''
        return sm_trans(self.matrix)

    def conj(self):
        '''Conjugation'''
        return sm_conj(self.matrix)

    def con_trans(self):
        '''Conjugation transpose, transpose for plural'''
        return sm_con_trans(self.matrix)

    def det(self):
        '''Determinant'''
        return sm_det(self.matrix)

    def inverse(self):
        '''Inverse matrix'''
        return sm_inverse(self.matrix)

    def find(self, string: str='', length=2, direct='all', echo=False):
        '''scan the matrix and find a cut with given length.
        set string to:
        - any string: scan for it
        - '': scan for a cut in that length
        set direct to:
        - all:(as defult, or a) scan in every direction
        - row:(or r) only scan in row
        - colume:(or c) only scan in colume
        - rowcolume:(or cr, or rc) scan in row and colume
        - oblique:(or o) scan in oblique
        set echo to:
        - False:(as defult) will return True is exist
        - True: will return the first match as [row1,colume1]
                means the match start at [row1,colume1]
        about priority:
        from hight to low : row - colume - oblique(\) - oblique(/)
        from [0,0] to [m-1,n-1]
        '''
        string = str(string)
        _row = len(self.matrix)
        _colume = len(self.matrix[0])
        new_matrix = sm_str(self.matrix)
        if (_row < length and direct in ['all', 'a', 'row', 'r', 'oblique', 'o', 'rc', 'cr'])\
           or (_colume < length and direct in ['all', 'a', 'colume', 'c', 'oblique', 'o', 'rc', 'cr']):
            assert False, 'Length of cut cannot longer than length of scan area!'
        if direct in ['all', 'a', 'row', 'r', 'rc', 'cr']:
            # scan in row
            # 纯行扫描
            for _r in range(_row):
                for _scan in range(_colume - length + 1):
                    if string != '' and string != new_matrix[_r][_scan]:
                        continue
                    for _i in range(1, length):
                        flag = True
                        if new_matrix[_r][_scan:_scan+length][_i] != new_matrix[_r][_scan]:
                            flag = False
                            break
                    if flag:
                        if echo:
                            return _r, _scan
                        else:
                            return True
        if direct in ['all', 'a', 'colume', 'c', 'rc', 'cr']:
            # scan in colume
            for _r in range(_row - length + 1):
                for _scan in range(_colume):
                    if string != '' and string != new_matrix[_r][_scan]:
                        continue
                    for _i in range(1, length):
                        flag = True
                        if new_matrix[_r + _i][_scan] != new_matrix[_r - 1][_scan]:
                            flag = False
                            break
                    if flag:
                        if echo:
                            return _r, _scan
                        else:
                            return True
        if direct in ['all', 'a', 'oblique', 'o']:
            # scan in oblique
            # direction \ first
            for _r in range(_row - length + 1):
                for _c in range(_colume - length + 1):
                    if string != '' and string != new_matrix[_r][_c]:
                        continue
                    for _i in range(1, length):
                        flag = True
                        if new_matrix[_r + _i][_c + _i] != new_matrix[_r][_c]:
                            flag = False
                            break
                    if flag:
                        if echo:
                            return _r, _c
                        else:
                            return True
            # direction / second
            # sure can put \ and / in same cycle, but too hard to read
            # especially when we need check flag and echo
            for _r in range(_row - length + 1):
                for _c in range(length - 1, _colume):
                    if string != '' and string != new_matrix[_r][_c]:
                        continue
                    for _i in range(1, length):
                        flag = True
                        if new_matrix[_r + _i][_c - _i] != new_matrix[_r][_c]:
                            flag = False
                            break
                    if flag:
                        if echo:
                            return _r, _c
                        else:
                            return True
        return False

    def trace(self):
        '''return the trace, only for square matrix'''
        _trace = 0
        sm_numcheck(self.matrix)
        for _cr in range(len(self.matrix)):
            trace += self.matrix[_cr][_cr]
        return trace

# -------------------------------------------------------
# Handle with multiple matrixs
# -------------------------------------------------------


def sm_sum(*matrixs, force=False):
    ''' sum all given matrixs
    set force=True to ignore '' and letters
    use sm_negative() to minus anyone'''
    _row = len(matrixs[0])
    _colume = len(matrixs[0][0])
    new_matrix = sm_number(matrixs[0], force)
    for _item in matrixs[1:]:
        if len(_item) != _row or len(_item[0]) != _colume:
            assert False, 'Cannot sum matrixs with different numbers of rows or columes!'
        _item = sm_number(_item, force)
        for _r in range(_row):
            for _c in range(_colume):
                new_matrix[_r][_c] += _item[_r][_c]
    return new_matrix


def sm_minus(matrix_1, matrix_2, force=False):
    '''minus two matrixs, matrix_1 - matrix_2'''
    return sm_copy(sm_sum(matrix_1, sm_negative(matrix_2), force=force))


def sm_multis(*matrixs_or_numbers, force=False):
    '''multiplication for matrixs and numbers'''
    matrixs = []
    numbers = 1
    for _item in matrixs_or_numbers:
        if type(_item) is list or type(_item) is tuple:
            if force:
                matrixs.append(sm_number(_item))
            elif sm_numcheck(_item):
                matrixs.append(_item)
            else:
                assert False, 'Your matrix is illegal for multiplication!'
        elif type(_item) is int or type(_item) is float or type(_item) is complex:
            # changed for plural
            numbers *= _item
        else:
            assert False, 'Type of arguments must be list or int or float or complex!'
    new_matrix = sm_copy(matrixs[0])
    for _i in range(1, len(matrixs)):
        new_matrix = sm_multi_mm(new_matrix, matrixs[_i])
    return sm_multi_mn(new_matrix, numbers)


def sm_multi_mm(matrix_1, matrix_2):
    '''multiplication for only 2 matrixs'''
    _length = len(matrix_1[0])
    if _length != len(matrix_2):
        assert False, 'Your matrix is illegal for multiplication!'
    new_matrix = sm_gen(len(matrix_1), len(matrix_2[0]))
    for new_row in range(len(matrix_1)):
        for new_column in range(len(matrix_2[0])):
            for _n in range(_length):
                new_matrix[new_row][new_column] +=\
                    matrix_1[new_row][_n] * matrix_2[_n][new_column]
    return new_matrix


def sm_multi_mn(matrix, number):
    '''multiplication for one matrix and one number'''
    new_matrix = sm_copy(matrix)
    for _item in new_matrix:
        for _i in range(len(_item)):
            _item[_i] *= number
    return new_matrix
