import string

def remove_punc(str):
    new_str = ""
    for char in str:
        if char not in string.punctuation:
            new_str += char
    return new_str

def write_filtered():
    file_name = input("Please enter the file name:")
    str = input("Please enter the string:")
    new_str = ''
    try:
        with open(file_name , "r" , encoding = "utf-8") as f:
            stopwords = set(f.read().splitlines())

            # Split input string into terms
            terms = str.split()

            # Filter out stopwords
            filtered_terms = [term for term in terms if term.lower() not in stopwords]

        # Write filtered terms to output file
        with open(str, 'w') as f:
            f.write('\n'.join(filtered_terms))

    except FileNotFoundError:
        print("File not found!")
        return {}

write_filtered()