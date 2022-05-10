import csv



with open('onlinefile.txt') as file_, open('Filename2.csv', 'w') as csvfile:
    lines = [x for x in file_.read().strip().split('@') if x]
    writer = csv.writer(csvfile)
    writer.writerow(('ID', 'Report'))
    for idx, line in enumerate(lines, 1):
        writer.writerow((idx, line.strip('@')))