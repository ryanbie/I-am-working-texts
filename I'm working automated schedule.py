import schedule
import time

def job():
    print("I'm working...")

schedule.every().day.at("9:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)