import os
import csv

budget_data = os.path.join('Resources_one', 'budget_data.csv')


with open(budget_data, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    #Don't read the header
    next(csv_reader, None)
    
   
    total_dates = 0
    total_sum = 0
    total_change = 0
    previous_profit_loss = None
    biggest_profit = None
    biggest_loss = None
    biggest_profit_month = None
    biggest_loss_month = None

    
    #1 
    total_dates = len(list(csv_reader))

# Add the .seek(0) operator to reset the file
    csvfile.seek(0)

    next(csv_reader, None)

    #2 - Total sum of column 2
    for row in csv_reader:
        total_sum += float(row[1])

        #3 - avg change
        current_profit_loss = float(row[1])
        if previous_profit_loss is not None:
            profit_change = current_profit_loss - previous_profit_loss
            total_change += profit_change

        #4 greatest total increase
        month = row[0]
        profit_loss = float(row[1])

        if previous_profit_loss is not None:
            profit_change = profit_loss - previous_profit_loss
            if biggest_profit is None or profit_change > biggest_profit:
                biggest_profit = profit_change
                biggest_profit_month = month

        #5 greatest total decrease
        if previous_profit_loss is not None:
            profit_change = profit_loss - previous_profit_loss
            if biggest_loss is None or profit_change < biggest_loss:
                biggest_loss = profit_change
                biggest_loss_month = month

        previous_profit_loss = profit_loss

total_average_change = total_change / (total_dates - 1)

print('Financial Analysis')
print('-----------------------------------------')
print(f'Total Months: {total_dates}')
print(f'Total: ${total_sum}')
print(f'Average Change: ${total_average_change:.2f}')
print(f'Greatest Increase in Profits: {biggest_profit_month} {biggest_profit}')
print(f'Greatest Decrease in Profits: {biggest_loss_month} {biggest_loss}')

output_file = os.path.join('financial_analysis_results.txt')
with open(output_file, 'w') as textfile:

    textfile.write('Financial Analysis\n')
    textfile.write('-----------------------------------------\n')
    textfile.write(f'Total Months: {total_dates}\n')
    textfile.write(f'Total: ${total_sum}\n')
    textfile.write(f'Average Change: ${total_average_change:.2f}\n')
    textfile.write(f'Greatest Increase in Profits: {biggest_profit_month} ${biggest_profit}\n')
    textfile.write(f'Greatest Decrease in Profits: {biggest_loss_month} ${biggest_loss}\n')
