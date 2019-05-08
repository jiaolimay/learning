# -*- coding:utf-8 -*-
import xlrd
import xlwt

# workbook = xlrd.open_workbook('D:\\Personal\\personal.xlsx')
# sheet = workbook.sheets()[0]
# sheet = workbook.sheet_by_name('test')
# sheet = workbook.sheet_by_index()
# print(sheet.nrows)
# print(sheet.ncols)
# print(sheet.row_values(0)[0])
'''rows'''
# for i in range(sheet.nrows):
#     # print(i,sheet.row_values(i)[0])
#     # print(i,sheet.row(i)[0].value)
#     print(i,sheet.cell(i,0).value)
'''cols'''
# for i in range(sheet.ncols):
#     print(i,sheet.row_values(0)[i])

'''write excel'''
excel = xlwt.Workbook()
sheet = excel.add_sheet('测试')
sheet.write(0,0,'test1')
sheet.write(0,1,'张三')
excel.save('D:\\pythontest.xls')

