import csv
import sys
filename = 'weibo_data.csv'

data = []
try:
    with open(filename) as f:
        reader = csv.reader(f)
        header = reader.next()
        data = [row for row in reader]
except csv.Error as e:
    print("Error readering CSV file at line %s: %s" % (reader.line_num, e))
    sys.exit(-1)
if header:
    print(header)
    print('==================')

for datarow in data
    print(datarow)