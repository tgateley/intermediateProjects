import time


def countdown(timer):
    while timer >= 0:
        hour = timer // 60
        minutes = timer % 60

        formatted_time = f"{hour:02d}:{minutes:02d}"

        print(formatted_time)
        time.sleep(1)

        timer -= 1

    print('Time is up!!')


seconds = int(input("Enter the countdown time(seconds): "))
countdown(timer=seconds)

