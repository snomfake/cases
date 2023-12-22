import os
import sys
import time


def timer(count: int):
    while count > 0:
        min, sec = divmod(count, 60)
        print(f"{min:02} {sec:02}", end="\r")
        time.sleep(1)
        count -= 1
        os.system("clear")
    print("STOP!!!!!!!!!!!!!!!!!!!!!")


if __name__ == "__main__":
    count = int(input("Enter minutes: "))
    count *= 60
    try:
        timer(count)
    except KeyboardInterrupt:
        print("Bye")
        sys.exit(0)
