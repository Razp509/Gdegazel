import pygsheets
from datetime import datetime

from core.config import settings


gc = pygsheets.authorize(service_file='service-acount.json')


sh = gc.open(settings.TABLE_NAME)

sheet_title = settings.SHEET_TITLE

wks = sh.worksheet_by_title(sheet_title)


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
    value_cell.value = ''
    value_cell.update()
    return "Ячейка очищена"


def all_work_day():
    col = settings.CELL_TOTAL_DAYS
    cell_col = wks.cell(col)    
    val = int(cell_col.value)
    return val


def work_day():
    col = f'{work_day_month.get(month())}{settings.FLOATING_CELL_COUNT}' #
    cell_col = wks.cell(col)    
    val = int(cell_col.value)
    return val


def all_work_money():
    col = settings.CELL_TOTAL_AMOUNT
    cell_col = wks.cell(col)
    val = int(cell_col.value)
    return val


def work_money():
    col = f'{col_month.get(month())}{settings.FLOATING_CELL_COUNT}' #
    cell_col = wks.cell(col)
    val = int(cell_col.value)
    return val
