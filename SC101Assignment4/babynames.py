"""
File: babynames.py
Name: 
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds or updates the given year and rank for the specified name in the name_data dict.
    """
    if name not in name_data:
        # Name does not exist, add it with the year and rank
        name_data[name] = {year: rank}
    else:
        # Name exists, check if the year already exists for this name
        if year not in name_data[name]:
            # Year does not exist for this name, add it with the rank
            name_data[name][year] = rank
        else:
            # Year exists, compare the ranks and keep the higher one (lower rank number)
            existing_rank = name_data[name][year]
            if int(rank) < int(existing_rank):
                # New rank is higher, update it
                name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.
    """
    with open(filename, 'r') as file:
        year = file.readline().strip()  # Read the first line to get the year
        for line in file:
            # Split the line by commas and strip spaces and newlines
            parts = line.split(',')
            rank = parts[0].strip()
            name1 = parts[1].strip()  # Male name
            name2 = parts[2].strip()  # Female name
            
            # Use the previously implemented function to add/update data
            add_data_for_name(name_data, year, rank, name1)
            add_data_for_name(name_data, year, rank, name2)



def read_files(filenames):
    name_data = {}  # Initialize an empty dictionary to hold all name data
    for filename in filenames:
        add_file(name_data, filename)  # Assume add_file is implemented as in Milestone 2
    return name_data



def search_names(name_data, target):
    matching_names = []
    target_lower = target.lower()  # Convert target to lowercase for case-insensitive comparison
    for name in name_data:
        # If the lowercase name contains the lowercase target, add it to the results
        if target_lower in name.lower():
            matching_names.append(name)
    return matching_names



def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
