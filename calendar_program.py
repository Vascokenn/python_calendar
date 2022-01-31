#Program to display calender of pre-given month and year
#importing calendar modile

import calendar


#yy = 2022
#mm = 12

#Take month and year from the user

yy = int(input('Enter Year: '))
mm = int(input('Enter Month: '))

#display the calender

print(calendar.month(yy, mm))
