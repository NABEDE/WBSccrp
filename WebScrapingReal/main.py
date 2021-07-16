from bs4 import BeautifulSoup
import requests
import time
import json


print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
unfamiliar_skill = unfamiliar_skill.lower()
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text  = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', {"class" : "clearfix job-bx wht-shd-bx"}) #job = soup.find_all('li', {"class" : "clearfix job-bx wht-shd-bx"})
    #company_name = job.find('h3', {"class" : "joblist-comp-name"})
    for index, job in enumerate(jobs):
        publish_date = job.find('span', {"class": "sim-posted"}).span.text
        if 'few' in publish_date:
            company_name = job.h3.text.replace(' ', '')
            skills = job.find('span', {"class": "srp-skills"}).text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                info_jobs = {
                    "Company Name":f'{company_name.strip()}',
                    "Required skills":f'{skills.strip()}',
                    "More info":f'{more_info}'
                }
                #print(info_jobs)
                json_info = json.dumps(info_jobs, indent=3)
                # Writing to sample.json
                with open("info_json.json", "w") as outfile:
                    outfile.write(json_info)
                with open(f'posts/{index}.txt', 'w') as f:
                    #print(publish_date)
                    # print(skills)
                    # print(company_name)
                    f.write(f"Company Name : {company_name.strip()} \n")
                    f.write(f"Required skills : {skills.strip()} \n")
                    f.write(f"More info : {more_info} \n")
                    #print(f'''
                    #Company Name: {company_name}
                    #Required skills: {skills}
                    #''')
                print(f"File saved: {index}")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes ...')
        time.sleep(time_wait * 60)


#clearfix job-bx wht-shd-bx