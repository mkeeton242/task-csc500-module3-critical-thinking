###
# Project:      AlarmTimeProblem.py
# Author:       Michael Keeton
# Created:      09/29/2024
# Description:  A program that asks the user for the time now
#               in hours, the number of hours to wait for the alarm,
#               and outputs the 24 hour time of the alarm.
###

def main():
    # Prompt user for current time and wait time.
    time_now = int(input('Enter the current hour in 24-hour time format: '))
    wait_time = int(input('Enter the number of hours to wait for the alarm: '))
    
    # Calculate and output the alarm time.
    alarm_time = (time_now + wait_time) % 24
    print('The alarm will go off at: {:d}:00 (in 24-hour time format).'.format(alarm_time))
    
main()
