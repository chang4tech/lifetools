import datetime

#birth = datetime.date(1995,1,20)
year = int(input("Please input your birth year:"))
month = int(input("Please input your birth month:"))
day = int(input("Please input your birth day:"))
birth = datetime.date(year,month,day)
today = datetime.date.today()
lifespan = 61
lifespan = int(input("Please input your expected lifespan."))

print("Your birth date: "+str(birth))
print("Today: "+str(today))

pastdays = (today-birth).days
pastmonths = round(pastdays/30)
print("About " + str(pastdays)+ " days / " + str(pastmonths) + " months passed.")
percent = pastmonths/(lifespan*12)
#print("Percentage: " + str(percent))
print("Your life progress: \n" + int(percent*20)*'*'+'•'*int((1-percent)*20),str('{0:.2f}'.format(percent*100))+'%')
