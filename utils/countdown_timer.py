import time

def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Temps restant/Time remaining : {i} secs", end='\r')
        time.sleep(1)
