import csv

with open('data1.csv', 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)


#reading with delimiter
#reader = csv.reader(file,delimiter=':')

#skipping header row
#next(reader)
# for row in reader:
#     print(row)

#reading csv as  a dictionary
with open('data1.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        if row['city'] == "Mumbai":
            print(row['name'], row['age'])



