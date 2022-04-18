def add_time (timestart, timeadd, date = ''):
    time1 = timestart.split(' ')
    time2 = time1[0]
    timeapm = time1[1]
    time3 = time2.split(':')
    hour = time3[0]
    minute = time3[1]
    timeadd2 = timeadd.split(':')
    houradd = timeadd2[0]
    minutesadd = timeadd2[1]
    listdate = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    if timeapm == 'AM':
        totalhour = int(hour) + int(houradd)
    else:
        totalhour = int(hour) + int(houradd) + 12
    totalminute = int(minute) + int(minutesadd)
    if totalminute >= 60:
        totalminute -= 60
        totalhour += 1

    day = 0
    while True:
        if totalhour >= 24:
            day +=1
            totalhour -= 24
        else:
            break
    if totalhour > 12:
        totalhour -= 12
        timeapm = 'PM'
    elif totalhour == 12:
        totalhour = 12
        timeapm = 'PM'
    elif totalhour == 0:
        totalhour = 12
        timeapm = 'AM' 
    else:
        timeapm = 'AM'
    if len(str(totalminute)) <2:
        totalminute = '0'+ str(totalminute)

    if day == 0:
        day2 =''
    elif day == 1:
        day2 = '(next day)'        
    else:
        day2 = '(' + str(day) +' days later)'
        
    if date != '':
        date = listdate[listdate.index(date.title()) + int(day)]
        print (str(totalhour) +':' + str(totalminute) +' ' + timeapm +', ' +  date + ' ' + day2)
    else:
        print (str(totalhour) +':' + str(totalminute) +' ' + timeapm + ' ' + day2)
    




add_time("3:00 PM", "3:10")
add_time("11:30 AM", "2:32", "Monday")
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30")
add_time("11:43 PM", "24:20", "tueSday")
add_time("6:30 PM", "205:12")
