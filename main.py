import pygsheets
from datetime import datetime


gc = pygsheets.authorize()

sh = gc.open('Gdegazel_table')
wks = sh.sheet1

dt = datetime.now()
month = dt.month
day = dt.day


col_month = {4:'B', 5:'D', 6:'F', 7:'H', 8:'j', 9:'L', 10:'N', 11:'P', 12:'R'}
col_month_value = col_month.get(month)


        
def cell_value(money_received):
    col = f'{col_month_value}{day + 1}'
    value_cell = wks.cell(col)    
    if value_cell.value == '':
        value_cell.value = money_received
        value_cell.update()
        return "Данные внесены!"
    else:
        return "Сегодня данные уже вносились!"
    

def cell_clear():
    col = f'{col_month_value}{day + 1}'
    value_cell = wks.cell(col)
    # value_cell.value = ''
    value_cell.value = ''
    value_cell.update()
    return "Ячейка очищена"


def work_day():
    col = 'A36'
    cell_col = wks.cell(col)    
    val = int(cell_col.value)
    return val


def work_money():
    col = 'C36'
    cell_col = wks.cell(col)
    val = int(cell_col.value)
    return val
