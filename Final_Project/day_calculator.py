from datetime import datetime

def diff_dates():
    choosen_date = input('Please, enter the date of your choice (max. 7 days in advance) in the format: DD-MM-YYYY.\n')
    diff_dates = number_of_days(choosen_date)
    print(diff_dates)
    return diff_dates


def number_of_days(choosen_date):
    date_format = "%d-%m-%Y"
    now = datetime.now()

    future_date = datetime.strptime(choosen_date, date_format)
    diff_dates = future_date - now
    diff_dates = int(diff_dates.days)+1
    return (diff_dates)


# if __name__ == '__main__':
#     main()