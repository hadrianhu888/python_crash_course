import csv
import matplotlib.pyplot as plt
from datetime import datetime
import string
import os
from os import path
import sys
from sys import argv


def get_date_highs_lows(filename, date_index, tmax_index, tmin_index):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            high = int(row[tmax_index])
            low = int(row[tmin_index])
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    return dates, highs, lows


def get_csv_indices_names(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for index, column_header in enumerate(header_row):
            print(index, column_header)
    return header_row


def get_high_low_indices(header_row):
    for index, column_header in enumerate(header_row):
        if column_header == 'TMAX':
            tmax_index = index
        if column_header == 'TMIN':
            tmin_index = index
        if column_header == 'DATE':
            date_index = index
    return date_index, tmax_index, tmin_index


first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(first_date)

filename = 'data/death_valley_2018_simple.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    # find Tmax and Tmin in the header row
    for index, column_header in enumerate(header_row):
        if column_header == 'TMAX':
            tmax_index = index
        if column_header == 'TMIN':
            tmin_index = index
        if column_header == 'DATE':
            date_index = index
    print(tmax_index, tmin_index, date_index)
    # read the data
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    print(highs)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

# plot the data

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

# Format the plot

plt.title("Daily high and low temperatures - 2018\nDeath Valley\n", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# save the plot

plt.savefig('images', 'death_valley_high_lows.png')
