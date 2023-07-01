import openpyxl

wb = openpyxl.load_workbook(r"8-Excel\archivo.xlsx")
print(wb.sheetnames)

sheet = wb["Hoja1"]

cell = sheet["a1"]

# Cambiar el valor de la celda
cell.value = "id"

print(cell.value)
print(cell.row)
print(cell.column)
print(cell.coordinate)
