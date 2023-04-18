import csv
import random

# set file
inputpath = '../etc/data/'
outputpath='../etc/data/lownoise'
input = inputpath+'auto2.csv'
split = input.split('.')
output = outputpath+split[0]+"_lownoise."+split[1]


# set possibility
p = 0.01 # noise possibility for a row
q = 0.01 # noise possibility for a column


with open(input, newline='') as csvfile_in, open(output, 'w', newline='') as csvfile_out:
    reader = csv.reader(csvfile_in)
    writer = csv.writer(csvfile_out)

    headers = next(reader)
    writer.writerow(headers)

    lowercase_headers = [header for header in headers if header[0].islower()]
    
    for row in reader:
        if random.random() < q:
            for i in range(len(row)):
                if headers[i] not in lowercase_headers and random.random() < p:
                    row[i] = "?"

        writer.writerow(row)

