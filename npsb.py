# Reading an excel file using Python
import xlrd
# #
# class npsb:
#     def __init__(self, path):
#         # To open Workbook
#         wb = xlrd.open_workbook(path)
#         self.sheet = wb.sheet_by_index(0)
#
#     def print(self, sheet):
#         # For row 0 and column 0
#         # for i in range(wb.ncols):
#         print(sheet.cell_value(1, 0))
#
# if __name__ == '__main__':
#     np = npsb("resources/NPSB_ISS_ACQ_TRX_export_OCT_2019_updated.xlsx")
#     np.print(np.sheet)
# #
#
#
# # Give the location of the file
loc = (r"resources/NPSB_ISS_ACQ_TRX_export_OCT_2019_updated.xlsx")
# loc1 = (r'resources/atm.xlsx')
# loc12 = (r'resources/atm_acc.xlsx')
loc2 = (r'resources/NPSB_ISS_ACQ_TRX_export_20_OCT_2019.xlsx')
# # To open Workbook
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
# sheet.cell_value(1, 0))
# # For row 0 and column 0
# for i in range(sheet.ncols):
# print(sheet)

import pandas as pd

df = pd.read_excel (loc2)
# df2 = pd.read_excel (loc12)
 #for an earlier version of Excel, you may need to use the file extension of 'xls'
# print (df['DATE_TIME'])

array = [0] * 32

# Create a Pandas dataframe from the data.
newdf = df['TERMSIC']
# newdf2 = df2['TERMSIC']
# newdf = df['TERMSIC']

# p = pd.DataFrame()
# p = p.append(newdf)
start = 0
end = 1
# data_top = newdf
# print(df[newdf==data_top].index.item())
# print(data_top.index.values)

a = []
# for each in newdf:
#     # print(each)
#     a.append(newdf[newdf == each])
# print(df)
# print(df2)
# for each in df['PAN']:
#     print(each)
def icrm(day):
    array[day] = array[day] + 1
a = []
for d in newdf:
    # date = str(d.split(' ')[0])
    date = str(d)
    if(date == "6011"):
        continue
    else:
        if date in a:
            1
        else:
            a.append(date)
print(a)
    # __date = date.split('-')
    # day = __date[0]
    # month = __date[1]
    # year = __date[2]
        # print(date)
    # icrm(int(day))

# print(newdf[0])
# print(newdf[1])
# print(newdf[10697])
# print(newdf[10698])
# print(newdf[10699])
# # print('----------------')
# print(newdf[10700])
# print('----------------')
# print(newdf[22435])
# print(newdf[22436])
# print(newdf[22438])
#     # end = d[0]
# array[30] = d[0]
# print(array)
# print(week(1))

# Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('resources/pandas_simple.xlsx', engine='xlsxwriter')
#
# # Convert the dataframe to an XlsxWriter Excel object.
# newdf.to_excel(writer, sheet_name='DATE_TIME')
#
# # Close the Pandas Excel writer and output the Excel file.
# writer.save()
