#coding:utf-8
import xlrd
# 确定Excel位置并打开
Excelpath ='../Testdata/excel_case.xlsx'
data = xlrd.open_workbook(Excelpath)
# 选择Excel第一页sheet
tables = data.sheets()[0]
# 打印Excel行数
print(tables.nrows)
# 打印Excel第二行，第三列内容
print(tables.cell_value(1,2))
