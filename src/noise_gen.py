import csv
import random

# set file
input = '../etc/data/auto2.csv'
output = '../etc/data/auto2_noise.csv'


# set possibility
p = 0.8 # noise possibility for a row
q = 0.8 # noise possibility for a column


with open(input, newline='') as csvfile_in, open(output, 'w', newline='') as csvfile_out:
    reader = csv.reader(csvfile_in)
    writer = csv.writer(csvfile_out)

    headers = next(reader)
    writer.writerow(headers)
    
    for row in reader:
        if random.random() < q:

            index = random.randint(0, len(row)-1)
            if random.random() < p:
                row[index] = "?"

        writer.writerow(row)

