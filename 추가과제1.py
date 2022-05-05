import datetime
Y_month=int(input("You : Enter month born (1-12): "))
Y_day=int(input("You : Enter day born (1-31): "))
Y_year=int(input("You : Enter year born (4-digit): "))
T_month=int(input("Today: Enter month born (1-12): "))
T_day=int(input("Today: Enter day born (1-31): "))
T_year=int(input("Today: Enter year born (4-digit): "))

your_day=datetime.date(Y_year,Y_month,Y_day)
Today_day=datetime.date(T_year,T_month,T_day)
count_day=Today_day-your_day
print(f"Number of days you lived: {count_day.days}")