import day_temp
import print_day
import day_calculator

import requests
import json
from datetime import datetime
from fpdf import FPDF

def main():
    print('\n                               Hello Dear Guest!')
    print('\nThe program presents the forecasted weather for a fixed location (Gdańsk) for the upcoming 7 days.\n')
    number_of_days = day_calculator.diff_dates()
    days = []
    days = day_temp.main(number_of_days)

    pdf_file = FPDF()

    for day in days:
        print_day.print_day(pdf_file,day)
    pdf_file.output('Weather_data.pdf', 'F')

if __name__ == "__main__":
    main()