import string
from collections import Counter

def is_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

def odd_even(src_str):
    try:

        with open(src_str , "r") as file:

            content = file.readlines()
            
            for line in content:

                try:

                    num = int(line.strip())
                    stat = is_even(num)
                    print(f"{num} is {stat}.")

                except ValueError:
                    "This is not an integer!"

    except FileNotFoundError:

        print("File not found!")
        return 0
    
def double_check(m , n):
    if m == n:
        return True
    else:
        return False

def check_line_by_line(src_str):

    try:
        prog = 0
        with open(src_str , "r" , encoding = "utf-8") as file:

            for line in file:

                prog += line.count("prog")

        print(prog)
        return

    except FileNotFoundError:
        print("File not found!")
        return 0

def check_whole_string(src_str):
    try:
        prog = 0
        with open(src_str , "r" , encoding = "utf-8") as new_file:

            content = new_file.read()
            for line in content:

                prog += line.count("prog")

            print(prog)
            return
        
    except FileNotFoundError:
        print("File not found!")
        return 0

def remove_punc(str):
    new_str = ""
    for char in str:
        if char not in string.punctuation:
            new_str += char
    return new_str

def word_count(src_str):
    
    try:
        with open(src_str , "r" , encoding = "utf-8") as file:
            content = file.read()
            words = content.lower().split()
            count = Counter(words)
        return count
    
    except FileNotFoundError:
        print("File not found!")
        return {}

def filtered_word_count(word_count , filter):

    try:
        with open(filter , "r" , encoding = "utf-8") as filter_file:
            filters = filter_file.read()
            filters = remove_punc(filters)
            filter_words = filters.lower().split()
            for word in filter_words:
                del word_count[word]
            return word_count
    except FileNotFoundError:
        print("File not found!")
        return {}

def row_sum(src_str):
    try:
        with open(src_str , "r") as file:
            matrix = [[int(num.strip()) for num in line.split(',')] for line in file]
            new_list = []
            for row in matrix:
                new_list += [sum(row)]
            return new_list
    except FileNotFoundError:
        print("File not found!")
        return []

def mat_min(src_str):
    try:
        with open(src_str , "r" , encoding = "utf-8") as file:
            content = file.read()
            matrix = [int(num.strip()) for row in content.split('\n') for num in row.split(',') if num.strip()]
            minimum = min(matrix)
            return minimum
    except FileNotFoundError:
        print("File not found!")
        return []
    
                            

#odd_even("numbers.txt")
#check_line_by_line("programming_languages.txt")
#check_whole_string("programming_languages.txt")
#print(double_check(check_line_by_line("programming_languages.txt") , check_whole_string("programming_languages.txt")))
#print(word_count("programming_languages.txt"))
#print(filtered_word_count(word_count("programming_languages.txt") , "stopwords_list.txt"))   
#print(row_sum("matrix.txt"))
print(mat_min("matrix.txt"))

input("Press any key to exit...")