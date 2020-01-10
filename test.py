import requests
from bs4 import BeautifulSoup

def get_students(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html)

    table = soup.find_all('table')[3]
    rows = table.find_all('tr')[1:] #[1:] skips header

    row = table.find_all('tr')[2]
    for row in rows:
        cols = row.find_all('td')[1]
        print (cols.get_text())

def main():
    url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&submit=Register%20Selected&wldel=PSYC%2C365%2C001'
    get_students(url)

if __name__ == "__main__":
    main()