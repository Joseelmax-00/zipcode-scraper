### Chrome webdriver location (It will look for it in PATH and/or the current folder if left as "")
### Change this if getting the Error message: chromedriver.exe must be in PATH or similar
chrome_location = ""


### Constant parameters (tags must be in order)
tags = ["Timezone", "Area code", "Population", "Population Density", "Housing Units", "Median Home Value", "Land Area", "Occupied Housing Units", "Median Household Income"]


### This is the maximum number of Chrome instances that will be open at the same time 
### Starting = 6, change by multiplying or dividing by 2
num_threads = 1



### The variables under this line should not be changed

### This changes the location of the first entry on the excel spreadsheet (it starts saving to B5,B6...C5,C6... as default)
start_col = 5
start_row = 2

### These are the names that a file CANNOT HAVE:
reserved_filenames = ["zipcodes.txt", "debug.log", "backup.txt", "template.xlsx", "vars.py", "zipcode_scraper.py", "utilities.py", ]

### This is showed if writing info in the console when selecting options
mode1_doc = """This mode will ask you for the name of an EXISTING text file that was created via the 2nd option. Then, will resume the scraping operation from this existing file, and save any newly scraped data to it. It will avoid scraping already scraped zipcodes. If anything goes wrong, a backup will be created in backup.txt"""
mode2_doc = """This mode creates a new text file and starts the scraping operation, saving the scraped data to this newly created text file."""
mode3_doc = """This mode requests a text file that contains the zipcodes and an excel book, it will save the information into the excel with the format from template.xlsx. It will also remove all corrupted and duplicate entries from the text file as well as sort it by descending order."""


