# Loan Qualifier

This application helps identify the loans you qualify for from the lenders & details in the daily_rate_sheet.csv
This application requests details such as credit score, monthly debt, total montgly income, loan amount and home value . 
Then calculates, debt to income ratio and compares the values input with the daily rate sheet to identify qualifying loans. 
The users can then choose to record the results in a csv.
---

## Technologies

python script using fire, questionary & pytest. 

---

## Installation Guide
Clone the coode 
Create a conda environment :  conda create -n <env_name> python=3.7 anaconda
Activate env:  conda activate <env_name>
Install dependencies : pip install -r .\requirements.txt
Run the code : python app.py 
Enter the path for the daily_rate_sheet.csv 
Type the answers for the questions prompted on terminal and save the results on csv

---

## Usage

The users can enter the data for the questions prompted at the terminal to see the loans they qualify for . 
[ Note, you can replace it with another file (similar to daily_rate_sheet.csv] of the same format if you want to plugin different data]

---

## Contributors

Columbia boot camp content creators

---

## License

