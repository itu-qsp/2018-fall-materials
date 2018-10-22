
#solution to Part C in Assignment 6

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
    :return: set
        A set of sorted country code numbers.
    """
    wb = openpyxl.load_workbook(filename)
    sheet = wb.get_sheet_by_name("Sheet1")
    
    list_of_columns = list(sheet.columns)
    column_of_interest = list_of_columns[column_number]
    cells_of_interest = column_of_interest[1:]

    country_codes = []

    for cell_object in cells_of_interest:
        country_codes.append(cell_object.value)

    country_codes_unique = set(country_codes)
    country_codes_sorted = sorted(country_codes_unique)
    return country_codes_sorted

#The rest was given in the code

def main():
    cph_person_codes = country_codes_data('befkbhalderstatkode_small.xlsx', 3)
    complete_codes = country_codes_data('country_codes.xlsx', 0)
    print("Unique codes for people living in Copenhagen:\n", sep="\n", cph_person_codes)
    print('-----------------')
    print("All unique country codes sorted:\n", sep="\n", complete_codes)
    print('-----------------')
if __name__ == "__main__":
    main()
