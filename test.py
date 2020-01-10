import requests # scraper
from bs4 import BeautifulSoup # parser
import time # delay
import smtplib # email
from email.mime.text import MIMEText
from email.header import Header

empty_seat_count = 0
url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&submit=Register%20Selected&wldel=PSYC%2C365%2C001'
html = requests.get(url).content
soup = BeautifulSoup(html)

path = "C:/Users/cbl04/Documents/empty_seat_parser/password.config"
f = open(path, 'r')
password = f.read()

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

        from_addr = '0415cbl@naver.com'
        to_addr  = ['chanbin.lee123@gmail.com', '0415cbl@gmail.com']

        # email
        msg = MIMEText("Register now: " + url)                   
        msg['Subject'] = 'Empty seat in ' + course_name[0] + course_name[1] # 메일 제목 첨부
        msg['From'] = '0415cbl@naver.com'      
        msg['To'] = '0415cbl@gmail.com'       
       
        # email server
        server = smtplib.SMTP('smtp.naver.com', 587)
        server.starttls()
        server.login('0415cbl', password)

        # send email
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.close()
        break

    else:
        print("No seat")
        time.sleep(10)
        continue