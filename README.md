# The zipcode_scraper was created by José Maquia, eeseljose@gmail.com, github.com/Joseelmax-00.

This was my first project for an Upwork.com client. It scrapes the database of unitedstateszipcodes.org for certain items of information on a list of around 50.000 zipcodes. It exports those results to a text file, which can then be exported to an excel book. The project includes multithreading in order to achieve the fastest speed possible. 

## Description

```markdown
This program scrapes the database on https://www.unitedstateszipcodes.org/ for data, such as 
population, timezones, or other statistics

Read the requirements section if you encounter any problem.

The program works by opening a Chrome browser window, loads the page for a specific zipcode, 
extracts the data and pastes it into a text file, you then need to convert the text file into an 
excel spreadsheet with option number 3.
```

## Instructions

```markdown
First, you need to edit the variables in vars.py to suit your needs (don't worry, all variables 
have a description so you know what you are editing).

The number on the num_threads defines what is the highest number of instances of Chrome 
that you want have open at the same time when you run zipcode_scraper.py. If this number 
is 10, it will open 10 or less chrome windows. 


If you are getting any the error message that says "...chromedriver.exe must be in PATH..." do the
following:
	* Create a copy of chromedriver.exe in your Windows folder (located on your hard drive)
	* Set the chrome_location variable in vars.py as "/Windows/chromedriver"



To use this program just open the shell console in the folder where the program is located in 
and execute the following command: 

	python zipcode_scraper.py

This will start the program. You will have 3 options:
	
	1) Scrape to an already existing file: 
		
		+++	This mode will ask you for the name of an EXISTING text file that was 
			created by the 2nd option. Then, will resume the scraping operation from 
			this existing file, and save any newly scraped data to it. It will avoid 
			scraping already scraped zipcodes. If anything goes wrong, a backup will 
			be created in backup.txt"""


	2) Scrape to a new file: 				
		
		+++	This mode creates a new text file and starts the scraping operation, 
			saving the scraped data to this newly created text file.


	3) Convert from text file to excel spreadsheet: 	

		+++ 	When you finish scraping, the information will be stored in a text file, 
			in order to better visualize it you can use this option to 
			This mode requests a text file that contains the zipcodes, and will also 
 			request an excel book, it will save the information into the excel book 
			with the format from template.xlsx. It will also remove all corrupted 
			and duplicate entries from the text file as well as sort it by 
			descending order.				
	

		
That's it. It is that simple, just enter a number, enter a filename, and the program will 
take care of the rest!!


This program can be adapted to gather more data by editing the code in the get_required_info 
function on the utilities.py module.
```




