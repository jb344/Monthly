import datetime

# Day of the month that is pay day
PAYDAY = 27


def calculate_days_left_in_month():
    # Get the current date
    current_year = datetime.datetime.today().year
    current_month = datetime.datetime.today().month
    current_day = datetime.datetime.today().day

    # Current date
    now = datetime.date(current_year, current_month, current_day)

    # Check if the current day in the month is less than payday, aka we haven't been paid for a while
    if current_day < PAYDAY:
        # We are going to be paid in this current month, not next month...
        future = datetime.date(current_year, current_month, PAYDAY)
    else:
        # If the current month is December, next month is January so roll round, and the next year is also advanced
        if current_month == 12:
            current_month = 1
            current_year += 1
        # We are going to be paid next month, i.e perhaps its the 28th today, but we don't get paid until the 27th of the next month
        future = datetime.date(current_year, current_month, PAYDAY)

    # Return the days left, by subtracting the current date from the future payday
    return (future - now).days


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    days_left = calculate_days_left_in_month()
    print("What is your current balance?")
    # User needs to enter their current balance
    money_left = int(input())
    # Calculate how much we have left per day and per week, rounded to the nearest penny
    money_per_day = round(money_left / days_left, 2)
    money_per_week = round(money_left / (days_left / 7), 2)
    print("Per day: £" + str(money_per_day))
    print("Per week: £" + str(money_per_week))
