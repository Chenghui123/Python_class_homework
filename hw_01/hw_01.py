#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

def Name_reg(name):
    return name[0].upper() + name[1:].lower()

Name_list = ['adam', 'SAraH', 'miKe', 'LISA']

print(list(map(Name_reg, Name_list)))
