DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# This is the list of the days in a week

total_sales = []  # This is an empty list to add the sales

# Function to get sales for a day
def get_sales(day):
    while True:
        try:
            sales = float(input(f"Enter the total sales for {day}: $"))
            if sales >= 0:
                return sales
            else:
                print("This input is invalid. The amount of sales has to be greater than or equal to 0")
        except ValueError:
            print("Invalid input. Enter a valid number.")

# Loop to get sales for each day of the week
for day in DAYS:
    daily_sales = get_sales(day)
    total_sales.append(daily_sales)

# Calculate the total, minimum, and maximum sales
sales_total = sum(total_sales)
minimum_sales = min(total_sales)
maximum_sales = max(total_sales)

# Format the currency with two decimal places and comma separation
total_sales_currency = "${:.2f}".format(sales_total)
minimum_sales_currency = "${:.2f}".format(minimum_sales)
maximum_sales_currency = "${:.2f}".format(maximum_sales)

# Display the results
print(f"The total sales is: {total_sales_currency}")
print(f"The minimum sales amount was: {minimum_sales_currency}")
print(f"The maximum sales amount was: {maximum_sales_currency}")