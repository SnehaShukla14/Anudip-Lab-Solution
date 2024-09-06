# Q.2) Write a function in Python to count and display the total number of words in a text file “ABC.txt”

# CODE:

def count_words_in_file(filename):
    """
    Counts the total number of words in a text file and prints the count.
    
    Parameters:
    filename (str): The name of the file to be read.
    """
    try:
        # Initialize a word count variable
        total_words = 0
        
        # Open the file in read mode ('r')
        with open(filename, 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Split the line into words using default whitespace separation
                words = line.split()
                # Update the total word count
                total_words += len(words)
        
        # Print the total number of words
        print(f"Total number of words in the file '{filename}': {total_words}")
    
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"The file {filename} does not exist.")
    except IOError:
        # Handle other I/O related errors (e.g., permission issues)
        print(f"An error occurred while reading the file {filename}.")

# Example usage
count_words_in_file("ABC.txt")

# OUTPUT:
# Total number of words in the file 'ABC.txt': 8
