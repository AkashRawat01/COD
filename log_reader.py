import xlwt
from xlwt import Workbook
wb = Workbook()
sheet1= wb.add_sheet('sheet 1')

sheet1.write(0, 0,"Storage")
sheet1.write(0, 1,"Month")
sheet1.write(0, 2,"Date")
sheet1.write(0, 3,"Time")
sheet1.write(0, 4,"Database Name")


f= open('table1.sql','r')
b=0
for line in f:
    b=b+1
    a=line.split(' ')
    a[4]=a[4][0:-1]
    sheet1.write(b, 0, a[0])
    sheet1.write(b, 1, a[1])
    sheet1.write(b, 2, a[2])
    sheet1.write(b, 3, a[3])
    sheet1.write(b, 4, a[4])
    print(a)
   # print (l.split(" ")[0])


wb.save('haha.csv')