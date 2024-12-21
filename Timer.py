import time
import os

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("زمان به پایان رسید!")

def play_sound():
    try:
        os.system("play bell.mp3")  # برای لینوکس
        # os.system("start bell.mp3")  # برای ویندوز
    except Exception as e:
        print("نمی‌توان صدا را پخش کرد:", e)

def main():
    try:
        minutes = int(input("چند دقیقه می‌خواهید تایمر تنظیم شود؟ "))
        seconds = minutes * 60
        countdown_timer(seconds)
        play_sound()
    except ValueError:
        print("لطفاً یک عدد معتبر وارد کنید!")

main()