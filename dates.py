from datetime import datetime

def calculate_date_difference(date1_str, date2_str, date_format="%Y-%m-%d"):
    """
    Calculate the difference between two dates.
    Args:
        date1_str (str): First date in YYYY-MM-DD format
        date2_str (str): Second date in YYYY-MM-DD format
        date_format (str): Format of the input dates
    Returns:
        int: Absolute difference in days between the two dates
    """
    try:
        date1 = datetime.strptime(date1_str, date_format)01
        date2 = datetime.strptime(date2_str, date_format)
        difference = abs((date2 - date1).days)
        return difference
    except ValueError as e:
        return f"Error: {str(e)}"

def main():
    print("Date Difference Calculator")
    print("------------------------")
    print("Please enter dates in YYYY-MM-DD format")
    
    date1 = input("Enter first date: ")
    date2 = input("Enter second date: ")
    
    difference = calculate_date_difference(date1, date2)
    
    if isinstance(difference, int):
        print(f"\nThe difference between {date1} and {date2} is {difference} days.")
    else:
        print(difference)  # Print error message

if __name__ == "__main__":
    main()
