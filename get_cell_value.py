import openpyxl

def cell_value(file, sheet,cell):
    file = openpyxl.load_workbook(file)
    sheet = file[sheet]
    value = sheet[cell].value
    return value
g_