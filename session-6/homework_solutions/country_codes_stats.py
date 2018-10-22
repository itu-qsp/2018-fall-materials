
import stat_codes
import openpyxl


def country_codes_data(filename, column_number):
    """Read country code data from a given Excel file,
    in which entire columns contain country codes and
    the first row is a header row without values.

    :param filename: str
        Path to the Excel (.xslx) file containg a row
        with country codes
    :param column_number: int
        The index number of the column containing the
        country codes.
    :return: list
        A list of country code numbers.
    """

    # TODO: Implement me!
    pass

#THE FOLLOWING FUNCTION IS FOR THE OPTIONAL ASSIGNMENT PART E ( remember to uncomment line 41-43 before running)
def translate_code_to_text(code): 
    # TODO: Implement me!
    pass


#THE CODE BELLOW RUNS THE FUNCTIONS
def main():
    cph_person_codes = country_codes_data('befkbhalderstatkode_small.xlsx', 3)
    complete_codes = country_codes_data('country_codes.xlsx', 0)
    print("Codes for people living in Copenhagen:\n", sep="\n", cph_person_codes)
    print('-----------------')
    print("All country codes:\n", sep="\n", complete_codes)
    print('-----------------')

#UNCOMMENT THE LINES UNDER THIS LINE WHEN RUNNING CODE FOR THE ASSIGNMENT PART E

    #print("People from the following countries live in Copenhagen":)
    #for code_nr in cph_person_codes:
        #print(translate_code_to_text(code_nr), end =',')
    

if __name__ == "__main__":
    main()
