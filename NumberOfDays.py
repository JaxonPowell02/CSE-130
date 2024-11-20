#Python

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        raise ValueError("Invalid month")

def days_in_year(year):
    return 366 if is_leap_year(year) else 365

def calculate_days_between(start_date, end_date):
    total_days = 0
    start_month, start_day, start_year = start_date
    end_month, end_day, end_year = end_date

    if start_year == end_year:
        if start_month == end_month:
            total_days = end_day - start_day
        else:
            total_days += days_in_month(start_year, start_month) - start_day

            for month in range(start_month + 1, end_month):
                total_days += days_in_month(start_year, month)

            total_days += end_day
    else:

        for month in range(start_month, 13):
            if month == start_month:
                total_days += days_in_month(start_year, start_month) - start_day
            else:
                total_days += days_in_month(start_year, month)

        for year in range(start_year + 1, end_year):
            total_days += days_in_year(year)

        for month in range(1, end_month):
            total_days += days_in_month(end_year, month)
        total_days += end_day

    return total_days

def main():
    try:

        print("Enter the start date:")
        start_month = int(input("  Month: "))
        assert 1 <= start_month <= 12, "Month must be between 1 and 12."
        start_day = int(input("  Day: "))
        assert 1 <= start_day <= 31, "Day must be between 1 and 31."
        start_year = int(input("  Year: "))
        assert start_year > 1753, "Year must be greater than 1753."
        assert 1 <= start_day <= days_in_month(start_year, start_month), "Invalid day for the given month."
        start_date = (start_month, start_day, start_year)

        print("Enter the end date:")
        end_month = int(input("  Month: "))
        assert 1 <= end_month <= 12, "Month must be between 1 and 12."
        end_day = int(input("  Day: "))
        assert 1 <= end_day <= 31, "Day must be between 1 and 31."
        end_year = int(input("  Year: "))
        assert end_year > 1753, "Year must be greater than 1753."
        assert 1 <= end_day <= days_in_month(end_year, end_month), "Invalid day for the given month."
        assert (end_year, end_month, end_day) >= (start_year, start_month, start_day), "Ending date must not be before the starting date."
        end_date = (end_month, end_day, end_year)

        total_days = calculate_days_between(start_date, end_date)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    except:
        print("Something went wrong try again.")


    print(f"Total days between {start_date} and {end_date}: {total_days}")

if __name__ == "__main__":
    main()
