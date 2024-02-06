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

            content = new_file.readlines()
            for line in content:

                prog += line.count("prog")

            print(prog)
            return
        
    except FileNotFoundError:
        print("File not found!")
        return 0


#odd_even("numbers.txt")
#check_line_by_line("programming_languages.txt")
#check_whole_string("programming_languages.txt")
    
print(double_check(check_line_by_line("programming_languages.txt") , check_whole_string("programming_languages.txt")))

input("Press any key to exit...")