import requests # scraper
from bs4 import BeautifulSoup # parser
import time # delay
import smtplib # email

empty_seat_count = 0
url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&submit=Register%20Selected&wldel=PSYC%2C365%2C001'
html = requests.get(url).content
soup = BeautifulSoup(html)

def get_students(url):
    table = soup.find_all('table')[3] # Third table of page
    row = table.find_all('tr')[2] # Receives row
    col = row.find_all('td')[1] # Receives column
    empty_seat_count = col.get_text()

def main():
    get_students(url)

while True:
    main()
    if empty_seat_count != 0:
        course_name = soup.title.string.split()
        msg = 'Subject: Empty seat in ' + course_name[0] +'!!!'
        print(msg)
        from_addr = 'chanbin.lee123@gmail.com'
        to_addr  = 'chanbin.lee123@gmail.com'
        break

    else:
        print("No seat")
        time.sleep(10)
        continue