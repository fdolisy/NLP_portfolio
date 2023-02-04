"""
 >>> Author: Fanny Dolisy
 >>> Title: Text Processing with python
"""
import re
import os
import pickle
import sys

def populate_dictionary(filepath: str) -> dict:
    """
    Adds dictionary entries of people objects
    Args: 
        filepath: the sysarg file path
    Returns: dict
        the dictionary of people objects
    """
    people = {}
    filepath = get_data_filepath(filepath)
    try:
        with open(filepath , 'r') as f:
            # skip past the first line
            f.readline()
            for line in f:
                # split on comma
                line_list = line.split(",")
                # last name
                last_name = line_list[0].capitalize()
                # first name
                first_name = line_list[1].capitalize()
                # add middle initial
                if not line_list[2]:
                    middle_initial = 'X'
                else:
                    # middle initial exists
                    if len(line_list[2]) != 1:
                        middle_initial = line_list[2][0].capitalize()
                    else:
                        middle_initial = line_list[2].capitalize()
                # id
                id = test_format_id_input(line_list[3])
                # phone number
                phone_number = convert_phone_number(line_list[4])
                
                # check for duplicate entries before adding to dict
                while id in people:
                    print(f"ERROR id {id} already exists in dictionary")
                    id = input(f"Please enter a new id for {first_name} {last_name}: ")
                    id = test_format_id_input(id)
            
            # create dict entry
                people[id] = Person(last_name, first_name, middle_initial, id, phone_number)
    except FileNotFoundError:
        print(f"ERROR: File located at {filepath} was not found, please run again with a valid file")
        exit()
    return people


def get_data_filepath(filepath: str) -> str:
    """
    Gets the cross platform filepath of the data file
    Returns: string
        the file path
    """
    current_dir = os.getcwd()
    print(f"{os.path.join(current_dir, filepath)}")
    return os.path.join(current_dir, filepath)


def test_format_id_input(id: str) -> str:
    """
    Loops until a validly formatted id is inputted 
    Args: 
        id: the currently inputted id to be initially checked
    Returns: string
        a validly inputted id
    """
    while not re.fullmatch(r'[a-zA-Z]{2}\d{4}', id):
                print(f"ID {id} is invalid\n ID should be two letters followed by two numbers")
                id = input("Please enter a valid id: ")
    return id


def convert_phone_number(number: str) -> str:
    """
    Converts a phone number into the accepted format 
    Args: 
        number: the currently inputted number to be initially checked
    Returns: string
        a validly formatted phone number
            >> 000-000-0000
    """
    ideal_regex = "\w{3}\-\w{3}-\w{4}"
    # correct match
    if re.fullmatch(ideal_regex, number):
        return number
    # extract the digits, to format the number without input
    digits = re.sub("\D", "", number)
    # if there is the wrong number of digits, ask for a new number
    if len(digits) != 10:
        while not re.fullmatch(ideal_regex, number):
            print(f"Phone number {number} is invalid\n Please enter in the form 000-000-0000") 
            number = input(f"Please enter a valid phone number: ")
    else:
        number = f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    return number


class Person:
    def __init__(self, first_name, last_name, middle_initial, id, phone):
        """
        Constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.middle_initial = middle_initial
        self.id = id
        self.phone = phone


    def display(self) -> None:
        """
        Displays the attributes the class
        """
        print(f"Employee id: {self.id}")
        print(f"\t {self.first_name} {self.middle_initial} {self.last_name}")
        print(f"\t {self.phone}\n")

def main():
    # check to ensure there is a system argument (first if program name)
    if len(sys.argv) != 2:
        print(f"ERROR: have one system argument containing the file path of the data")
        exit()
    else:
       inputted_filepath = sys.argv[1]
    # populate the dictionary
    people_dict = populate_dictionary(inputted_filepath)
    # dump to a pickle file and reopen
    pickle.dump(people_dict, open('dict.p', 'wb')) 
    read_people = pickle.load(open('dict.p', 'rb')) 
    # display the read in dictionary
    for key in read_people:
        person = read_people[key]
        person.display()

if __name__ == "__main__":
    main()
