import openpyxl

filename = 'C:/home/jens/workspace/itu/qualification-seminar-2018/session_6/befkbhalderstatkode_small.xlsx'
wb = openpyxl.load_workbook(filename)
print(wb)