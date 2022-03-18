class Alarm_Clock:
    def __init__(self):
        self.clocks_current_time= ''
        self.alarm_on= False
        self.alarm_time= ''

    def set_time(self):
        self.clocks_current_time= input('What time would you like to set: ') 
        print(f'The clock time is now {self.clocks_current_time}')
        
    
    def turning_alarm_on(self):
        setting_alarm= input('Would you like to use the alarm, y/n? ')
        if setting_alarm == 'y':
            print("Okay, the alarm is now on. Don't forget to set the alarm time!")
        else:
            print('Alarm is off!')


    def setting_alarm_time(self):
        set_alarm_time= input('What time would you like to set your alarm: ')
        print(f'Alarm time set to {set_alarm_time}.')


