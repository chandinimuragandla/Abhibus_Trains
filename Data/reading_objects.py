# import xlrd
# from Library.config import Config
# # path = r'C:\Users\DELL\PycharmProjects\chandini\train data.xlsx'
#
#
# def read_locators():
#     workbook = xlrd.open_workbook(Config.DATA_PATH)
#     worksheet = workbook.sheet_by_name('train_module')
#     rows = worksheet.get_rows()
#     print(rows)
#     header = next(rows)
#     d = {}
#     for row in rows:
#         d[row[0].value] = (row[1].value,row[2].value)
#     return d


####################################
import xlrd
from Library.config import Config


class ReadExcel:

    def read_test_data(self,sheetname):
        wb = xlrd.open_workbook(Config.DATA_PATH)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()
        header=next(rows)
        data = []
        for row in rows:
            values = ()
            for j in range(columns):
                values += (row[j].value,)
            data.append(values)
        return data

    def read_locators(self,sheetname):
        wb = xlrd.open_workbook(Config.DATA_PATH)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)
        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)
        return d
