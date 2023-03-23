import csv
with open('Housing (1).csv','r') as input_file:
    csv_reader = csv.reader(input_file)
    with open('output.csv','w') as output_file:
        csv_writer = csv.writer(output_file)
        for row in csv_reader:
            csv_writer.writerow(row[:3] + row[6:8])
            
