import pygsheets
from datetime import datetime
from date_funk import days_in_month


gc = pygsheets.authorize()

sh = gc.open('Gdegazel_table')
wks = sh.sheet1

dt = datetime.now()
month = dt.month
day = dt.day


lst_col = {4:'A', 5:'B', 6:'C', 7:'D', 8:'E', 9:'F', 10:'G', 11:'H', 12:'I'}

num_col = lst_col.get(month)


for i in range(4, days_in_month(month)):
    col = f'{num_col}{i}'
    header = wks.cell(col)
    if header.value == '':
        wks.apply_format([col], ["NUMBER"])
        header.value = day
        header.update()
        break
