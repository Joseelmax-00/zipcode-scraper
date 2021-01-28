print("Importing required libraries")
from selenium import webdriver
from time import sleep, perf_counter
from vars import *
import threading
## I had to resort to threading since creating multiple processes would crash the computer.
from openpyxl import load_workbook, Workbook
from utilities import *

timer = perf_counter()
    
"""To implement:
-ADD MAIN MENU
-Add everything to excel sheet
-ADD Blocked names with names that the file cannot have
-ADD INFORMATION ABOUT OPTIONS
"""





## This sends all the zipcodes to the "zipcodes.txt" file for easier manipulation
## Uncomment the next 2 lines to create a zipcodes.txt file with all the zipcodes in order (this extracts data from the spreadsheet named "template.xlsx")
# wsheet = load_spreadsheet()
# zip_file = zipcodes_to_txt(wsheet)



### Main block
## This is where the magic happens
## The process is already very optimised regarding memory consumption and CPU usage (I cannot optimise how much resources google chrome consumes, however.)
## The program could be optimised to occupy less disk space by reusing the code from this main file, that would require a complete rework of this file. Could save lines of code, doesn't save me any time tho.


mode = ask_input()

if mode == 1:
    ## First we ask the parameters
    existing_file_name = input("Name of the existing file to resume: ")
    if is_reserved(existing_file_name):
        raise FileNotFoundError
    
    ### This block backups, then cleans, then sorts (to remove duplicates) the text file to remove corrupted entries.
    ## Create a backup of the file
    with open(existing_file_name, "r", encoding = "utf-8") as file:
        with open("backup.txt", "w", encoding = "utf-8") as backup_file:
            print("Saving backup to backup.txt")
            for line in file:
                backup_file.write(line)

    
    # Cleaning it
        clean_file_mem = clean_txt(file)
    with open(existing_file_name, "w", encoding = "utf-8") as file:
        for line in clean_file_mem:
            file.write(line)
        
        
        
        ## Sorts the file
    with open(existing_file_name, "r", encoding = "utf-8") as file:
        sorted_file = sorted_(file)
    with open(existing_file_name, "w", encoding = "utf-8") as file:
        for line in sorted_file:
            file.write(line)
            
    
    
    
    
    ## This sets up the threads, and calculates the zipcodes that each will take care of
    print("Setting up multiple processes...")
    start_points = []
    starting = 2
    with open("zipcodes.txt", "r", encoding = "utf-8") as file:
        last_row = 0
        for line in file:
            last_row += 1
    for _ in range(num_threads):
        start_points.append(int(starting))
        starting += last_row/num_threads
    start_points.append(last_row)
    print("The threads start at row:", start_points)
    
    ## This starts the threads and the perf counter
    timer = perf_counter()
    threads = []

    for i in range(num_threads):
        
        t = threading.Thread(target=thread_operation, args = [start_points[i], start_points[i+1], existing_file_name, i])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()





elif mode == 2:
    ### This first block asks for a filename, checks if it exists and asks the user if it wants to overwrite it.
    new_file_name = input("Choose a name for the new file (include extension, preferrably .txt): ")
    try:
        if is_reserved(new_file_name):
            raise ValueError
        open(new_file_name, "r", encoding = "utf-8")
        yes_no = input("NOTE: File already exists, do you want to overwrite it and lose all data in it? (Y/N): ")
        if yes_no == "y" or yes_no == "Y":
            raise FileNotFoundError
        else:
            raise ValueError
    
    except FileNotFoundError:
        """This error is raised if the file does not exist or the user wants to overwrite it"""
        print("Creating file")
        with open(new_file_name, "w", encoding = "utf-8") as file:
            file.write("")
        print("File created")
    
    except ValueError:
        """This is raised if the user does not want to overwrite the data in the file"""
        print("Aborting operation")
        quit()
    
    
    
    ## This second block does exactly the same as the first one but with the new file
    ## No need to sort the file or backup since it's empty
    ## This sets up the threads, and calculates the zipcodes that each will take care of
    print("Setting up multiple processes...")
    start_points = []
    starting = 2
    with open("zipcodes.txt", "r", encoding = "utf-8") as file:
        last_row = 0
        for line in file:
            last_row += 1
    for _ in range(num_threads):
        start_points.append(int(starting))
        starting += last_row/num_threads
    start_points.append(last_row)
    print("The threads start at:", start_points)
    
    ## This starts the threads and the perf counter
    timer = perf_counter()
    threads = []

    for i in range(num_threads):
        print("Executed thread", i)
        t = threading.Thread(target=thread_operation, args = [start_points[i], start_points[i+1], new_file_name])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
   
   
   
   
    
elif mode == 3:
    ### This block just asks the user for input
    valid = False
    while not valid:
        txt_file_name = input("Enter the name of the text file that has all the scrapped zipcodes' information (including the extension, like .txt): ")
        try:
            if is_reserved(txt_file_name):
                raise FileNotFoundError
            open(txt_file_name, "r", encoding = "utf-8")
            print()
            print("File opened")
            print()
            valid = True
        
        except FileNotFoundError:
            """This error is raised if the file does not exist"""
            print("The file does not exist or is a reserved file name (like zipcode.txt), enter the name of an existing, non reserved, file.")
    
    
    
    ### This block cleans and sorts the file
    # First we backup the txt file
    with open(txt_file_name, "r", encoding = "utf-8") as file:
        with open("backup.txt", "w", encoding = "utf-8") as backup_file:
            
            for line in file:
                backup_file.write(line)
            print("Saved backup of txt file to backup.txt")
    
    # Cleaning it
        print("Cleaning and sorting the file (This may take a while)")
        clean_file_mem = clean_txt(file)
    with open(txt_file_name, "w", encoding = "utf-8") as file:
        for line in clean_file_mem:
            file.write(line)
    print("Cleaned file, now sorting...")
    
    
    # This sorts the file
    with open(txt_file_name, "r", encoding = "utf-8") as file:
        sorted_file_mem = sorted_(file)
    with open(txt_file_name, "w", encoding = "utf-8") as file:
        for line in sorted_file_mem:
            file.write(line)
    print("Sorted")
    
    
    
    
    ### This block just asks the name of the excel file to output to
    valid = False
    while not valid:
        print()
        excel_file_name = input("Enter the name of the excel file to output to (NOTE: The name MUST contain the .xlsx extension): ")
        try:
            if excel_file_name[-5:] != ".xlsx" or is_reserved(txt_file_name):
                raise FileNotFoundError
            
            valid = True
        except FileNotFoundError:
            """We raise this error if the file is not an .xlsx"""
            print()
            print("The file MUST include the .xlsx, include it when entering its name")
            sleep(3)
    
    
    
    
    
    ### This block loads the template spreadsheet and then saves the data to the specified file.
    ## This loads the template spreadsheet
    print("Loading template...")
    wbook = load_workbook("template.xlsx")
    wsheet = wbook.active
    print("Template loaded")
    
    txt_to_excel(txt_file_name, excel_file_name, wsheet)
    print("Saving to", excel_file_name)
    wbook.save(excel_file_name)
    print("Saved")
    







### After all ended the program prints this:
print("The process took", int(perf_counter() - timer), "seconds")
if mode == 1 or mode == 2:
    print("Performance per thread:", int(perf_counter() - timer) / num_threads)


