from csv import reader
from csv import writer

def get_avg(file_name):
    with open(file_name , newline = '') as file:
        r_content = reader(file)
        with open('average.csv' , 'w' , newline = '') as w_file:
            w_content = writer(w_file)
            for row in r_content:
                w_content.writerow( (row[0] + row[1]) / 2 )
            