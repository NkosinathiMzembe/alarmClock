'''
An Alarm Clock Program
@author: Nkosinathi Mzembe
@version: 1.0
'''

#To Obtain local time
import time 

#Function To Notify User To Wake Up
def alarmNotice():
    for i in range(5):
        print("\nIt's Time To Wake Up ! ! !")
        time.sleep(2)
    
#Function To Set Alarm
def alarm():
    print("\nKindly Provide The Time You Would Like The Alarm To Ring At")
    alarmHr = int(input("Set Alarm Hour: "))
    alarmMin = int(input("Set Alarm Minutes: "))
    print("\nAlarm Set For "+str(alarmHr)+":"+str(alarmMin))

    secondAlarm = str(input("\nDo You Want To Set Another Alarm? ['Yes' or 'No']: ")).lower()
    if secondAlarm == "yes":
        alarmHour = int(input("Set Alarm Hour: "))
        alarmMinutes = int(input("Set Alarm Minutes: "))
        print("\nAlarm Set For "+str(alarmHr)+":"+str(alarmMin))

    #Condition to sound first alarm
    while True:
        if(time.localtime().tm_hour == alarmHr and time.localtime().tm_min == alarmMin):
           alarmNotice()
           break

    #Condition to sound second alarm    
    while True:
        if(time.localtime().tm_hour == alarmHour and time.localtime().tm_min == alarmMinutes):
           alarmNotice()
           break
  
#Main Function 
def main():
    #Prompt to user
    print("\tAlarm Clock Terminal Application")
    print("\nThe Current Time Is |",time.localtime().tm_hour,":",time.localtime().tm_min)
    alarm()

main()
