import csv
from sys import argv


def main():

    # Check for command-line usage
    if len(argv) != 3:
        print("Incorrect # of inputs")
        exit()

    # Read database file into a variable
    with open(argv[1]) as file:
        reader = csv.reader(file)
        database = list(reader)

    # TODO: Read DNA sequence file into a variable
    with open(argv[2]) as file:
        sequence = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    matches = []
    # Use database[1] to skip the length of the first sub-list database
    # Longest_match return a number to be added to matches =[]` list
    for i in range(1, len(database[0])):
        matches.append(longest_match(sequence, database[0][i]))
        # TODO: Check database for matching profiles
        coincidence = 'No Match'
        coincidence_count = 0
        # Skip the first entry and obtein the number of sub-lists within the list.
        for i in range(1, len(database)):
            for j in range(len(matches)):
                # Use int to convert string to int
                if matches[j] == int(database[i][j+1]):
                    coincidence_count += 1

            if coincidence_count == len(matches):
                coincidence = database[i][0]
                # If found match, stop.
                break
            else:
                coincidence_count = 0
    print(coincidence)

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
