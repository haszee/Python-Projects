'''
Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
'''

import time, datetime, winsound, os, platform

def main():

	while True:
		try:
			set_alarm = input('Enter what time to wake up in 24 hr format (hr:min:sec): ').split(':')
			break
		except ValueError:
			print('Please enter the time')

	alarm_time = datetime.time(int(set_alarm[0]),int(set_alarm[1]),int(set_alarm[2]))

	
	alarm(alarm_time)

def alarm(alarm_time):
	current_time = datetime.datetime.now().time()
	current_hour = current_time.hour
	current_min = current_time.minute
	current_sec = current_time.second

	start_time = current_hour*3600 + current_min * 60 + current_sec
	end_time = alarm_time.hour*3600 + alarm_time.minute*60 + alarm_time.second
	elapsed_time = end_time - start_time

	print(f'The current time is {current_time}')
	print(f'Alarm is set for {alarm_time}')
	time.sleep(elapsed_time)
	sound()

def sound():
	for repeats in range(3):
		for beeps in range(10):
			winsound.MessageBeep(1)
			time.sleep(2)
		time.sleep(60)

main()