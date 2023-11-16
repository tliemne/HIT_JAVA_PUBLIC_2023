import datetime


def count_days_datetime(date_string):

    date_input = datetime.datetime.strptime(date_string, "%d/%m/%Y")

    last_day_of_year = datetime.datetime.strptime(
        "31/12/{}".format(date_input.year), "%d/%m/%Y")

    return ((last_day_of_year - date_input).days + 1)


date_string = input()
number_of_days = count_days_datetime(date_string)
print(number_of_days)