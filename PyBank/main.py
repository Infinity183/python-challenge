# We have to start by importing the dependencies.
import os
import csv

# Now we must read the budget_data csv file, which is in PyBank's Resources folder.
budget_data = os.path.join("Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # Since there's a header in this spreadsheet, we must define it.
    csv_header = next(csv_reader)

    # These are the variables we will be needing for our output...

    # The total number of months:
    month_counter = 0

    # The total Profits/Losses across the whole period:
    net_change = 0

    # The month with the highest gain:
    max_gain_month = ""

    # The total profit for the highest-gaining month:
    max_gain_total = 0

    # The month with the highest loss:
    max_loss_month = ""

    # The total loss for the highest-losing month:
    max_loss_total = 0

    # It's time to loop through the csv spreadsheet.

    # We check each row in the csv
    for row in csv_reader:
        # Each new row accounts for another month:
        month_counter += 1

        # We need to convert profit/loss value for each month
        # into an integer before applying mathematical comparisons
        # to them (row[1] corresponds to the Profit/Losses for
        # that month):
        row[1] = int(row[1])

        # We will now add the profit/loss for the given month
        # to our total:
        net_change += row[1]

        # Next, we must check to see if the current month has the
        # greatest profit thus far:
        if row[1] > max_gain_total:
            # If the current month is higher than the current max gain,
            # then we must redefine max_gain_month and max_gain_total to
            # correspond to the current row:
            max_gain_month = row[0]
            max_gain_total = row[1]
        # Likewise for checking for the greatest losses:
        elif row[1] < max_loss_total:
            max_loss_month = row[0]
            max_loss_total = row[1]


#text_output = open("output.txt", "r+")

# With our calculations complete, we will now print our results.
print("Financial Analysis")
print("----------------------------")
# I'm using f-strings to print the redefined variables
# more conveniently.
print(f'Total Months: {month_counter}')
print(f'Total: ${net_change}')
# The average change is calculated by dividing the total profit/loss
# by the total number of months. I am rounding to two decimal places
# so that it's easier to read.
print(f'Average Change: ${round(float(net_change / month_counter), 2)}')
print(f'Greatest Increase in Profits: {max_gain_month} (${max_gain_total})')
print(f'Greatest Decrease in Profits: {max_loss_month} (${max_loss_total})')

# With the terminal results now printed, we will now export the same
# results into a .txt file in the analysis folder.
text_path = os.path.join("PyBank", "analysis", "Analysis.txt")
analysis = open(text_path, 'w')

# Mostly, we're just printing the same things, but with different
# syntax. We need \n at the end of every line to start a new line.
analysis.write("Financial Analysis\n")
analysis.write("----------------------------\n")
analysis.write(f'Total Months: {month_counter}\n')
analysis.write(f'Total: ${net_change}\n')
analysis.write(f'Average Change: ${round(float(net_change / month_counter), 2)}\n')
analysis.write(f'Greatest Increase in Profits: {max_gain_month} (${max_gain_total})\n')
analysis.write(f'Greatest Decrease in Profits: {max_loss_month} (${max_loss_total})')
