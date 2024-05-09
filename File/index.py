import os, io
from shutil import copyfile

import openpyxl # For file excel

def getValueExcel(filename, cellname):
    wb = openpyxl.load_workbook(filename) # Open file excel
    sheet1 = wb['Sheet1'] # Get sheet
    wb.close() # Close file excel
    return sheet1[cellname].value # Set value
def updateValueExcel(filename, cellname, value):
    wb = openpyxl.load_workbook(filename) # Open file excel
    sheet1 = wb['Sheet1'] # Get sheet
    sheet1[cellname].value = value # Set value
    wb.close() # Close file excel
    wb.save(filename) # Save file excel

filename = 'file.xlsx'
colA = 'A'
colB = 'B' 
for i in range(10):
    updateValueExcel(filename, colA + str(i+1), "Account " + str(i+1))
    updateValueExcel(filename, colB + str(i+1), "Password " + str(i+1))
for i in range(10):
    print(getValueExcel(filename, colA + str(i+1)), getValueExcel(filename, colB + str(i+1)))




