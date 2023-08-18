# LinkedIn Job Scraper
I made a LinkedIn scraper as practice for working with APIs and documentation. I can proudly say I created this project just by testing it myself and utilizing APIs and documentation without the need to look up a guide online.

This project helped me get practice on using Selenium in Python, as well as the Google Sheets API.
# Feature Plans
Currently, I am trying to find a way to make it so that this can be publicly used by anyone instead of tailored just towards me. Thus, this project is not usable yet, but I am just putting the code out there as a display for now. Please do either fork this repository or contact me in case you would want to help with this project.

Features:
- usable by anyone
- separate threaded script to look through each link in sheet and extract details (qualifications, payment, etc.)
****
# Documentation
As a basic documentation, the Python version required is at least 3.10.7, though I'd recommend 3.11.4 since that was the version this was made on. The library requirements are listed in requirements.txt, and the command ```pip install -r requirements.txt``` will install everything needed. 
#
As for the actual usage, the ```main.py``` file is the only one that needs to be run. You would also need to run the ```datainsert.py``` file first, but I will fix that.

The way that the script gets all of its links is from the ```linkedinlinks.txt``` file located in the files directory. The structure is ```{Name of subsheet in Google Sheets file},{link}```. Already in there is examples of it, as I was testing it with internship opportunities using the keywords "Artificial Intelligence" or "Machine Learning". This is for the program to know which sheet in the book to insert the data into.

As for the links themselves, they will have to be in an unlogged browser session. For instance, I got these links from going into an incognito mode tab that was not logged into my LinkedIn profile. This is so that the program does not get tripped up by dummy HTML elements. I also added certain tags to my links as well, as I was searching specifically for internships. 
****
# Results so far
As shown below, the Google Sheets book gets all of the aggregated data in its specific page.
![image](https://github.com/ankitmudunuri/linkedinscraper/assets/77700444/e6883e6e-809a-4ac8-adad-54ca022eeec0)
