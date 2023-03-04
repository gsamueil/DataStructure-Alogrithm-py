"""Calculate Average Terperature"""
"""
NEET TO ASK USER HOW MANY DAYS you need to fill the number of temperatures
then calculate the average of this days 
"""

# num_days = int(input("How many day's temperature? "))
# total = 0 
# for i in range(1, num_days+1):
#     next_day = int(input("Day " + str(i) + "'s high temp :"))
#     total += next_day
# avg = round(total/num_days,2)
# print("\nAverage = " + str(avg))
"""tring for array list """
num_days = int(input("How many day's temperature? "))
total = 0
temp = []
for i in range(num_days):
    next_day = int(input("Day "+ str(i+1) + "'s high temp:"))
    temp.append(next_day)
    total += temp[i]
avg = round(total/num_days,2)
print("\n Average = " + str(avg))

above = 0
for i in temp:
    if i >avg:
        above += 1
print(str(above) + " day(s) above average")