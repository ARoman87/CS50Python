dates = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        user_input = input("Date: ").capitalize()
        if "/" in user_input:
            month, day, year = user_input.split("/")
            if month.isdigit():
                month = int(month)
                day = int(day)
                year = int(year)
                if month <= 12 and day <= 31 and year <= 2022:
                    print(f"{year}-{month:02}-{day:02}")
                    break

        elif "," in user_input:
            month, day, year = user_input.split(" ")
            day = day.replace(",", "")
            if month in dates:
                month = dates.index(month)
                month = int(month) + 1
                day = int(day)
                year = int(year)
                if month <= 12 and day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break
    except:
        break
