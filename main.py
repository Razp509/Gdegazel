import pygsheets
from datetime import datetime
from date_funk import days_in_month


gc = pygsheets.authorize()

sh = gc.open('Gdegazel_table')
wks = sh.sheet1

dt = datetime.now()
month = dt.month
day = dt.day

# apply format
for i in range(1, days_in_month(month)):
    col = f'A{i}'
    header = wks.cell(col)
    if header.value == '':
        wks.apply_format([col], ["NUMBER"])
        header.value = day
        header.update()
        break




## set a formula and extend it to more cells
#cell = wks.cell('C1')
#cell.value = '=A1+B1'
#wks.apply_format('C1:C10', cell, 'userEnteredValue.formulaValue')