import pygsheets
from datetime import datetime

from core.config import settings


gc = pygsheets.authorize(service_file='service-acount.json')


sh = gc.open(settings.TABLE_NAME)

sheet_1 = settings.WORK_SHEET_1
sheet_2 = settings.WORK_SHEET_2

wks_1 = sh.worksheet_by_title(sheet_1)
wks_2 = sh.worksheet_by_title(sheet_2)


col_month = {1:'B', 2:'D', 3:'F', 4:'H', 5:'J', 6:'L', 7:'N', 8:'P', 9:'R', 10:'T', 11:'V', 12:'X'}
work_day_month = {1:'A', 2:'C', 3:'E', 4:'G', 5:'I', 6:'K', 7:'M', 8:'O', 9:'Q', 10:'S', 11:'U', 12:'W' }


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
    value_cell = wks_2.cell(col)    
    if value_cell.value == '':
        value_cell.value = money_received
        value_cell.update()
        return "Данные внесены!"
    else:
        return "Сегодня данные уже вносились!"
    

def cell_clear():
    col = f'{col_month.get(month())}{day() + 1}'
    value_cell = wks_2.cell(col)
    value_cell.value = ''
    value_cell.update()
    return "Ячейка очищена"


def month_work_day():
    col = f'{work_day_month.get(month())}38'
    cell_col = wks_2.cell(col)    
    val = int(cell_col.value)
    return val


def month_work_money():
    col = f'{col_month.get(month())}38'
    cell_col = wks_2.cell(col)
    val = int(cell_col.value)
    return val


def year_work_day():
    col = 'A41'
    cell_col = wks_2.cell(col)    
    val = int(cell_col.value)
    return val


def year_work_money():
    col = 'C41'
    cell_col = wks_2.cell(col)
    val = int(cell_col.value)
    return val


def all_work_day():
    col_old = 'A48'
    col = 'A41'
    cell_col_old = wks_1.cell(col_old)
    cell_col = wks_2.cell(col)
    val = int(cell_col_old.value) + int(cell_col.value)
    return val


def all_work_money():
    col_old = 'C48'
    col = 'C41'
    cell_col_old = wks_1.cell(col_old)
    cell_col = wks_2.cell(col)
    val = int(cell_col_old.value) + int(cell_col.value)
    return val