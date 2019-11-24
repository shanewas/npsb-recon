# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = ("resources/NPSB_ISS_ACQ_TRX_export_OCT_2019_updated.xlsx") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
for i in range(sheet.ncols): 
    print(sheet.cell_value(0, i)) 