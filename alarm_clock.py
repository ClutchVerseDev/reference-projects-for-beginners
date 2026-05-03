import time
import datetime

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    is_running = True
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == alarm_time:
            print("WAKE UP!!🥱")
            is_running = False

        time.sleep(1)

print(f"Current time: {datetime.datetime.now().strftime('%H:%M:%S')}")
alarm_time = input("Enter alarm time in the format HH:MM:SS: ")
set_alarm(alarm_time)
