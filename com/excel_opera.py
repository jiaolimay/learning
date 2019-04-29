# -*- coding:utf-8 -*-
import xlrd
import os
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))

def read_excel(path,index,column):
    xls = xlrd.open_workbook(path)
    sheet = xls.sheet_by_index(index)
    # print(sheet.nrows)
    data=[]
    for i in range(sheet.nrows):
        # print(i)
        data.append(sheet.row_values(i)[column])
        # print(sheet.row_values(i)[column])
    return data


# print("excelpath is : " ,excelpath)
# read_excel(excelpath,0,1)
