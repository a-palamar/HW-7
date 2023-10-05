from datetime import date
from datetime import datetime
from datetime import timedelta


def get_period(start_date: date, days:int):


    result = {}
    for _  in range(days + 1):
        weekday_name = start_date.strftime("%A")
        if weekday_name not in result:
            result[weekday_name] = []
        start_date += timedelta(1)
    return result

def get_birthdays_per_week(users):


    start_date = date.today()
    period = get_period(start_date, 7) 
    for user in users:
        bd: date = user["birthday"]
        date_bd = bd.day, bd.month
        
        for i in range(8):
            check_date = start_date + timedelta(days=i)
            if (bd.day, bd.month) == (check_date.day, check_date.month):                    
                weekday_name = check_date.strftime("%A")
                if weekday_name == "Saturday" or  weekday_name ==  "Sunday":
                    period["Monday"].append(user["name"])
                else:
                    period[weekday_name].append(user["name"])
    period = {k: v for k, v in period.items() if v} # Rempve empty days

    users = period
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 10, 6).date()},
        {"name": "Bill", "birthday": datetime(1980, 10, 5).date()},
        {"name": "Kim", "birthday": datetime(1990, 10, 8).date()},
    ]
    

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
