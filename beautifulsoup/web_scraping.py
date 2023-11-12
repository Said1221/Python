import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job = []
company = []
location_name = []
skill = []
links = []
salaries = []
responsibility = []
page_num = 0               # بعمل كده عشان اسوتش من صفحه للتانيه

while True:

    result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=flutter&start={page_num}")

    'save page content'
    src = result.content

    'create soup object to parse content'
    soup = BeautifulSoup(src, "lxml")

    page_limit = int(soup.find("strong").text)  # بعمل كده عشان اسوتش من صفحه للتانيه


    if (page_num > 2):
        break

    'find the elements containing info we need'
    'job title , job skills , company name , location name'
    job_title = soup.find_all("h2", {"class": "css-m604qf"})
    company_name = soup.find_all("a", {"class": "css-17s97q8"})
    location = soup.find_all("span", {"class": "css-5wys0k"})
    skills = soup.find_all("div", {"class": "css-y4udm8"})

    'loop over returned list to extract needed info into other lists'
    for i in range(len(job_title)):
        job.append(job_title[i].text)
        company.append(company_name[i].text)
        location_name.append(location[i].text)
        skill.append(skills[i].text)
        links.append(job_title[i].find("a").attrs['href'])

    page_num += 1




'بدخل كل وظيفه اجيب منها بيانات'
for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")

#    salary = soup.find("div","span" , {"class":"css-4xky9y"})
#    salaries.append(salary.text.strip())      #text.strip ==> عشان يشيل المسافات حول الجمله

#    requirement = soup.find("div" , {"class":"css-1t5f0fr"}).find("ul")
#    respon_text = ""
#    for li in requirement.find_all("li"):
#        respon_text += li.text+" | "
#    responsibility.append(respon_text)




'create csv file and fill it with values'
file_list = [job, company , location_name , skill , links , salaries , responsibility]
'عشان اول قيمه في الليست في الجوب تبقي مع اول قيميه في الكومباني مع اول قيمه لوكيشن و هكذا'
exported = zip_longest(*file_list)
with open("web.csv","w") as myFile:
    wr = csv.writer(myFile)
    wr.writerow(["job title", "company name", "location", "skills" , "links" , "salary" , "responsibility"])
    wr.writerows(exported)
