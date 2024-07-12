import csv
import pandas as pd

def reading_csv():
    # csv file name
    filename = "Cet_1_08.csv"

    # initialzing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        print("Total no. of rows: %d" % (csvreader.line_num))

    # printing the field names
    print('Field names are:' + ', '.join(field for field in fields))

    # printing first 5 rows
    print('\nFirst 5 rows are:\n')
    for row in rows[:5]:
        # parsing each column of a row
        for col in row:
            print("%10s" % col, end=" ")
        print('\n')

def reading_csv_into_dict():
    with open('Cet_1_08.csv', mode='r') as file:
        # create a CSV reader with DictReader
        csv_reader = csv.DictReader(file)

        # initialize an empty list to store the dictionaries
        data_list = []

        # iterate through each row in the CSV file
        for row in csv_reader:
            # append each row ( as a dictionary) to the list
            data_list.append(row)
    # print the list of dictionaries
    for data in data_list:
        print(data)

def writing_csv():
    # field names
    fields = ['Name','Branch','Year','CGPA']

    # data rows of csv file
    rows = [['Nikhil', 'COE', '2', '9.0'],
            ['Sanchit', 'COE', '2', '9.1'],
            ['Aditya', 'IT', '2', '9.3'],
            ['Sagar', 'SE', '1', '9.5'],
            ['Prateek', 'MCE', '3', '7.8'],
            ['Sahil', 'EP', '2', '9.1']]

    # name of csv file
    filename = "uni_records.csv"

    # writing to csv file
    with open(filename,'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the fields
        csvwriter.writerow(fields)
        # writing the data rows
        csvwriter.writerow(rows)

def writing_dict_to_csv():
    # my data rows as dictionary objects
    mydict = [{'branch': 'COE', 'cgpa': '9.0',
               'name': 'Nikhil', 'year': '2'},
              {'branch': 'COE', 'cgpa': '9.1',
               'name': 'Sanchit', 'year': '2'},
              {'branch': 'IT', 'cgpa': '9.3',
               'name': 'Aditya', 'year': '2'},
              {'branch': 'SE', 'cgpa': '9.5',
               'name': 'Sagar', 'year': '1'},
              {'branch': 'MCE', 'cgpa': '7.8',
               'name': 'Prateek', 'year': '3'},
              {'branch': 'EP', 'cgpa': '9.1',
               'name': 'Sahil', 'year': '2'}]
    # field names
    fields = ['name','branch','year','cgpa']

    # name of csv file
    filename = "univeristy_records.csv"

    # writing to csv file
    with open(filename,'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile,fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(mydict)

def csv_pandas():
    df = pd.read_csv('Cet_1_08.csv', sep='delimiter', header=None, engine='python')
    print(df[5:25])
def main():
    reading_csv()



if __name__ == "__main__":
    main()