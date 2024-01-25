import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        current_time = actual_time.strftime("%H:%M:%S")
        if current_time == set_alarm_timer:
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

def get_alarm_time():
    alarm_time = input("Enter the time of alarm in HH:MM:SS format: ")
    alarm_period = alarm_time[8:].lower()
    alarm_hour = int(alarm_time[:2])
    alarm_minute = int(alarm_time[3:5])
    alarm_seconds = int(alarm_time[6:8])
    return alarm_hour, alarm_minute, alarm_seconds, alarm_period

if __name__ == "__main__":
    alarm_hour, alarm_minute, alarm_seconds, alarm_period = get_alarm_time()
    set_alarm_timer = f"{alarm_hour:02}:{alarm_minute:02}:{alarm_seconds:02}"
    alarm(set_alarm_timer)
