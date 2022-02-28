# import openpyxl
#
#
# class Paramatrized:
#
#     @staticmethod
#     def getTestData(test_data):
#         Dict = {}
#         book = openpyxl.load_workbook("C:\\Users\\degahlot\\Desktop\\Book1.xlsx")
#         sheet = book.active
#         for i in range(1, sheet.max_row + 1):
#             if sheet.cell(row=i, column=1).value == test_data :
#                 for j in range(1, sheet.max_column + 1):
#                     Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
#
#         return[Dict]