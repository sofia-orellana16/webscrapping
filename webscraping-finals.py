from urllib.request import urlopen, Request
from bs4 import BeautifulSoup



url = 'https://registrar.web.baylor.edu/exams-grading/spring-2023-final-exam-schedule'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers= headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

my_classes = ['MW 2:30 p.m.','TR 9:30 a.m.','TR 11:00 a.m.','TR 2:00 p.m','MWF 10:10 a.m.']

classes_row = soup.findAll('tr')

for classes in classes_row[28:47]:
    td = classes.findAll('td')
    # if final: #this would also work since it would iterate only in classes that are not empty
    meeting_time = td[0].text.strip()
    exam_day = td[1].text.strip()
    exam_time = td[2].text.strip()

    if meeting_time in my_classes:
        print('For class:', meeting_time, 'the final is scheduled for', exam_day, 'at', exam_time )
    