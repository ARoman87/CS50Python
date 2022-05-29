import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    s = s.lower()

    if "to" in s:
        left, right = s.split("to")
        left = left.strip()
        right = right.strip()
        left_time, left_day = left.split(" ")
        right_time, right_day = right.split(" ")
        if ":" in left_time and ":" in right_time:
            left_hour, left_minutes = left_time.split(":")
            right_hour, right_minutes = right_time.split(":")
            left_hour = int(left_hour)
            left_minutes = int(left_minutes)
            right_hour = int(right_hour)
            right_minutes = int(right_minutes)
            if (
                left_minutes < 60
                and right_minutes < 60
                and left_hour <= 12
                and right_hour <= 12
            ):
                if left_day == "am":
                    if left_hour == 12:
                        left_hour = 0
                    left_hour = f"{left_hour:02}:{left_minutes:02}"
                elif left_day == "pm":
                    if left_hour == 12:
                        left_hour = f"{left_hour:02}:{left_minutes:02}"
                    else:
                        left_hour += 12
                        left_hour = f"{left_hour:02}:{left_minutes:02}"
                if right_day == "am":
                    right_hour = f"{right_hour:02}:{right_minutes:02}"
                elif right_day == "pm":
                    if right_hour == 12:
                        right_hour = f"{right_hour:02}:{right_minutes:02}"
                    else:
                        right_hour += 12
                        right_hour = f"{right_hour:02}:{right_minutes:02}"
                else:
                    raise ValueError
                return f"{left_hour} to {right_hour}"
            else:
                raise ValueError
        if ":" not in left_time and ":" not in right_time:
            right_time = int(right_time)
            left_time = int(left_time)
            if left_day == "am":
                if left_time == 12:
                    left_time = 0
                left_time = f"{left_time:02}:00"
            elif left_day == "pm":
                if left_time == 12:
                    left_time = f"{left_time:02}:00"
                else:
                    left_time += 12
                    left_time = f"{left_time:02}:00"
            if right_day == "am":
                if right_time == 12:
                    right_time = 0
                right_time = f"{right_time:02}:00"
            elif right_day == "pm":
                if right_time == 12:
                    right_time = f"{right_time:02}:00"
                else:
                    right_time += 12
                    right_time = f"{right_time:02}:00"
            else:
                raise ValueError
            return f"{left_time} to {right_time}"
    else:
        raise ValueError
