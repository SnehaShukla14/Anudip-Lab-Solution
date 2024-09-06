# Q.1) Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

# CODE:

def read_and_display_file(filename):

    try:
        # Open the file in read mode ('r')
        with open(filename, 'r') as file:
            
            # Iterate over each line in the file
            for line in file:
                
                # Print each line to the screen. The 'end=""' parameter avoids adding extra newline characters.
                print(line, end='')                
    except FileNotFoundError:
        
        # Handle the case where the file does not exist
        print(f"The file {filename} does not exist.")
    except IOError:
        
        # Handle other I/O related errors (e.g., permission issues)
        print(f"An error occurred while reading the file {filename}.")

# Example usage:
read_and_display_file("ABC.txt")

# OUTPUT:
# Happy Coding!!
# Good opportunity to work with projects.

    
