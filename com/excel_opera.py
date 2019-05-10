# _*_ coding:utf_8 -*_
import xlrd
import os
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))
excelpath = PATH('../appendix/testdata.xls')

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

'''using dic, column as key, row's values as value'''
dic={}
def read_excel_dic(path,index):
    xls = xlrd.open_workbook(path)
    sheet = xls.sheet_by_index(index)
    for j in range(sheet.ncols):
        data = []
        for i in range(sheet.nrows):
            data.append(sheet.row_values(i)[j])
            dic[j] = data
    return dic

print("excelpath is : " ,excelpath)
print(read_excel_dic(excelpath,0))

