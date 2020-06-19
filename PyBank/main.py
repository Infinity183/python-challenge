import os
import csv

budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)


    month_counter = 0
    net_change = 0
    max_gain_month = ""
    max_gain_total = 0
    max_loss_month = ""
    max_loss_total = 0

    for row in csv_reader:
        month_counter += 1
        row[1] = int(row[1])
        net_change += row[1]
        if row[1] > max_gain_total:
            max_gain_month = row[0]
            max_gain_total = row[1]
        elif row[1] < max_loss_total:
            max_loss_month = row[0]
            max_loss_total = row[1]

#text_output = open("output.txt", "r+")

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {month_counter}')
print(f'Total: ${net_change}')
print(f'Average Change: ${round(float(net_change / month_counter), 2)}')
print(f'Greatest Increase in Profits: {max_gain_month} (${max_gain_total})')
print(f'Greatest Decrease in Profits: {max_loss_month} (${max_loss_total})')

