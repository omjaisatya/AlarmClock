import datetime
import time
import winsound  

def set_alarm():
    while True:
        try:
            alarm_time_str = input("Enter the time for the alarm in HH:MM format (24-hour): ")
            alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M").time()
            if alarm_time > datetime.datetime.now().time():
                repeat_option = input("Do you want the alarm to repeat? (yes/no): ").lower()
                repeat_days = []

                if repeat_option == 'yes':
                    repeat_days_str = input("Enter the days to repeat (comma-separated, e.g., 'mon,tue,thu'): ").lower()
                    repeat_days = repeat_days_str.split(',')
                sound_option = input("Enter the sound file path or leave blank for default sound: ").strip()
                sound_path = sound_option if sound_option else "SystemExclamation"

                return alarm_time, repeat_days, sound_path

            else:
                print("Please enter a time in the future.")

        except ValueError:
            print("Invalid time format. Please enter the time in HH:MM format.")

def run_alarm(alarm_time, repeat_days, sound_path):
    while True:
        current_time = datetime.datetime.now().time()
        if current_time >= alarm_time:
            print("Alarm time reached! Wake up!")
            winsound.PlaySound(sound_path, winsound.SND_FILENAME)

            snooze_option = input("Do you want to snooze the alarm? (yes/no): ").lower()
            if snooze_option == 'yes':
                snooze_duration = int(input("Enter snooze duration in seconds: "))
                alarm_time = (datetime.datetime.now() + datetime.timedelta(seconds=snooze_duration)).time()
            else:
                break

        time_difference = datetime.datetime.combine(datetime.date.today(), alarm_time) - datetime.datetime.combine(datetime.date.today(), current_time)
        sleep_seconds = min(time_difference.seconds, 60) 
        time.sleep(sleep_seconds)

if __name__ == "__main__":
    try:
        alarm_time, repeat_days, sound_path = set_alarm()

        if alarm_time:
            print(f"Alarm set for {alarm_time.strftime('%H:%M')}")

            while True:
                current_day = datetime.datetime.now().strftime("%a").lower()
                if datetime.datetime.now().time() >= alarm_time and (not repeat_days or current_day in repeat_days):
                    run_alarm(alarm_time, repeat_days, sound_path)
                    break
                time_difference = datetime.datetime.combine(datetime.date.today(), alarm_time) - datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time())
                sleep_seconds = min(time_difference.seconds, 60) 
                time.sleep(sleep_seconds)

    except Exception as e:
        print(f"An error occurred: {e}")
