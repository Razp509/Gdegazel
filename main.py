import pygsheets
from datetime import datetime


gc = pygsheets.authorize(service_file='gdegazel-service-acount.json')

sh = gc.open('Gdegazel_table')
wks = sh.sheet1


col_month = {4:'B', 5:'D', 6:'F', 7:'H', 8:'J', 9:'L', 10:'N', 11:'P', 12:'R'}
work_day_month = {4:'A', 5:'C', 6:'E', 7:'G', 8:'I', 9:'K', 10:'M', 11:'O', 12:'Q' }


def month():
    dt = datetime.now()
    month = dt.month
    return month


def day():
    dt = datetime.now()
    day = dt.day
    return day

        
def into_cell(money_received):
    col = f'{col_month.get(month())}{day() + 1}'
    value_cell = wks.cell(col)    
    if value_cell.value == '':
        value_cell.value = money_received
        value_cell.update()
        return "Данные внесены!"
    else:
        return "Сегодня данные уже вносились!"
    

def cell_clear():
    col = f'{col_month.get(month())}{day() + 1}'
    value_cell = wks.cell(col)
    # value_cell.value = ''
    value_cell.value = ''
    value_cell.update()
    return "Ячейка очищена"


def all_work_day():
    col = 'A48'
    cell_col = wks.cell(col)    
    val = int(cell_col.value)
    return val


def work_day():
    col = f'{work_day_month.get(month())}45'
    cell_col = wks.cell(col)    
    val = int(cell_col.value)
    return val


def all_work_money():
    col = 'C48'
    cell_col = wks.cell(col)
    val = int(cell_col.value)
    return val


def work_money():
    col = f'{col_month.get(month())}45'
    cell_col = wks.cell(col)
    val = int(cell_col.value)
    return val

