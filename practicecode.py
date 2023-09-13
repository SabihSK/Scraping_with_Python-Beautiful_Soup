from bs4 import BeautifulSoup


# find data from a local website 
'''

with open ('home.html','r') as html_file :
    content = html_file.read()

    soup = BeautifulSoup(content , 'lxml')
    # print(soup.prettify)
    lines = soup.find_all("p")
    print(lines)

    # finding specific button and price 

    cards = soup.find_all('div', class_ = 'card' )
    for course in cards :
        course_name = course.h5.text

        course_price = course.a.text.split()[-1]
        print(f'{course_name}'costs {course_price})
        '''

import requests



print('Put some skill that you are not familier with')
unfamilier_skill = input('>')
print(f'FILTERING OUT {unfamilier_skill}')

def finding_jobs():
    code_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').text
    # print(code_text)

    soup = BeautifulSoup(code_text, 'lxml')

    job = soup.find_all('li' , class_ = "clearfix job-bx wht-shd-bx")

    for  job in job: 
        publisheddate = job.find('span', class_ ="sim-posted").text.replace(' ', '')
        if 'today'  in publisheddate:


            company_name = job.find ('h3', class_= "joblist-comp-name").text.replace(' ','')
            skills = job.find('span', class_ ="srp-skills").text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamilier_skill not in skills:

                with open('Jobs.txt', 'w') as information :
                    information.write(f'Company name : {company_name.strip()}')
                    information.write(f'Required skills: { skills}')
                    information.write(f'More Info : {more_info}')
            
  
finding_jobs()
# if __name__ == '__main__':
#     while True :
#         finding_jobs()
#         time_wait = 10 
#         print(f'Waiting {time_wait} seconds....')
#         time.sleep(600)