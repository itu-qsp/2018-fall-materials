# Write a docstring for every function inside the paren_checker.py file.
# At minimum describe the purpose of the function, the parameters and the return value

def check_paren(filename):
    """Reads a file and checks that there are equally many opening and 
    closing round parentheses. Prints a message depending on input.
    
    Args:
        filename (str): the name (optionally path) of the file to check.
    Returns: 
        None
    """
    with open(filename) as file: 
        parentheses = 0 
        for line in file:
            for character in line:
                if character == '(':
                    parentheses += 1
                if character == ')':
                    parentheses -= 1
                    
    if parentheses == 0:
        print("I think all parenthesis are balanced.")
    elif parentheses > 0:
        print("Looks like you forgot to close some parenthesis...")
    else:
        print("You are closing a parenthesis without opening one...")    

def main():
    """Reads a file specified on the command line and checks that 
    there are equally many opening and closing round parentheses. 
    Prints a message depending on input.
    
    Returns: 
        None
        
    Example:
    $ python paren_checker.py file_to_check.py
    will check the file file_to_check.py for round parentheses.
    """
    import sys
    filename = sys.argv[1]
    check_paren(filename)

if __name__ == '__main__':
    main()