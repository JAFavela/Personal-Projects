# GoldMiner
### Author: Jorge A Favela
This project was started with the goal of reducing the steps required to obtain documents and perform tasks on Goldmine, UTEPS student web portal. For example, obtaining a PDF copy of your current transcript would require you to:
1. Launch your browser.
2. Navigate to web page.
3. Enter login credentials.
4. Navigate through the various menus and pages to get to the transcript(about 6-7 clicks)
5. Print to pdf.

# With Goldminer:
1. Launch Goldminer.
2. Click the menu option.

## What it does:
- Uses selenium to automate the logging in and navigating to certain documents for view or direct export to users computer.
- It is capable of performing tasks such as registering for your classes given a list of CRN's.
- On first launch, a user may choose to store their login credentials and preferred browser in an encrypted file to eliminate the need to log in.

## Current options available:
- View Current Transcript (unofficial): Takes you to your unofficial transcript to view on the browser.
- Export Current Transcript (PDF): Saves a copy of your current transcript as a PDF in the Exports folder
- View Financial Aid Awarded For Current Term: Takes you to your awarded aid to view on the browser.
- Run Degree Evaluation: Runs your degree evaluation and displays it on the browser
- Export Current Class Schedule (PDF): Saves a copy of your current class schedule.
- View Current Class Schedule: Takes you to your current class schedule.
- Instant Course Registration (Must Know CRN's): Takes CRN numbers for your desired classes and automatically registers you for all of them
- Save/Update Credentials: Allows you to store or update currently stored credentials.

Along with the code, I have included a zip file with the EXE versions which should work on most Windows machines.
Just unpack contents and run Loader.exe.
