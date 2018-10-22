#solution to Part A in Assignment 6
import openpyxl


def country_codes_in_kbh_data():
    """" A function that imports the file 'befkbhalderstatkode_small.xlsx' as a openpyxl workbook object (wb). 
    And uses methods from the the openpyxl library to return a list of countrycodes from the data. 
    """
    filename = 'befkbhalderstatkode_small.xlsx' #stores the filename for the data
    wb = openpyxl.load_workbook(filename) #read in data as openpyxl workbook object
    sheet = wb.get_sheet_by_name("Sheet1") #selecting the given sheet from the excel file

    list_of_columns = list(sheet.columns) #create a list of all the colunms ( as lists)
    column_of_interest = list_of_columns[3] #select the 4th column from the list of lists
    cells_of_interest = column_of_interest[1:] #select the cells of the coulun, without the colun name

    country_codes = [] #creates an empty list for storing country codes

    for cell_object in cells_of_interest: #iterates through every value in the selected column
        country_codes.append(cell_object.value) #append each value, one by one, to the country_codes list

    return country_codes #returns a list of all the country codes in the selected column from the excel sheet.



def country_codes_in_stats_data():
    """See comments for function above"""
    filename = 'country_codes.xlsx'
    wb = openpyxl.load_workbook(filename)
    sheet = wb.get_sheet_by_name("Sheet1")

    list_of_columns = list(sheet.columns)
    column_of_interest = list_of_columns[0]
    cells_of_interest = column_of_interest[1:]

    country_codes = []

    for cell_object in cells_of_interest:
        country_codes.append(cell_object.value)

    return country_codes


def main():
    """Function for running the above functions, and printing the result"""
    cph_person_codes = country_codes_in_kbh_data()
    complete_codes = country_codes_in_stats_data()
    print(cph_person_codes)
    print(complete_codes)


if __name__ == "__main__":
    main()
