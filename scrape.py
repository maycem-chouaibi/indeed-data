# Created by Mayssem CHouaibi
# Class for scraping indeed data

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

# Create a new instance of the chrome driver. Starts the service and then creates new instance of chrome driver
driver = webdriver.Chrome(executable_path="PATH_HERE/chromedriver.exe")
URL = "https://www.indeed.com/jobs?q=data+scientist&l=New+York"
driver.get(URL)

def extract_job_from_result(driver): 
    # Initialize dataframe
    jobs = pd.DataFrame(columns=['Title', 'Company', 'Location', 'Salary', 'Description'])
    # Extract container for job
    for job in driver.find_elements(By.CLASS_NAME,"job_seen_beacon"):
        jobTitle=''
        jobCompany=''
        jobLocation=''
        jobSalary=''
        jobDescription=''
        #extract each element
        for title in job.find_elements(By.CLASS_NAME,'jobTitle'):
            for titleText in title.find_elements(By.TAG_NAME,'span'):
                jobTitle = titleText.text
        
        for company in job.find_elements(By.CLASS_NAME,'companyName'):
            jobCompany = company.text
            for companyName in company.find_elements(By.TAG_NAME,'a'):
                jobCompany = companyName.text                    

        for companyLocation in job.find_elements(By.CLASS_NAME,'companyLocation'):
            jobLocation = companyLocation.text
    
        for salary in job.find_elements(By.CLASS_NAME, 'salary-snippet-container'):
            for salaryRange in salary.find_elements(By.CLASS_NAME,'attribute_snippet'):
                jobSalary = salaryRange.text
        for salaryInSpanTag in job.find_elements(By.CLASS_NAME, 'estimated-salary'):
            for salaryfinal in salaryInSpanTag.find_elements(By.TAG_NAME,'span'):
                jobSalary = salaryfinal.text
        
        for description in job.find_elements(By.CLASS_NAME,'job-snippet'):
            for jobDesc in description.find_elements(By.TAG_NAME,'li'):
                jobDescription = jobDesc.text

        # add to df
        jobs.loc[len(jobs.index)]=[jobTitle, jobCompany, jobLocation, format_salary(jobSalary), jobDescription]

    # write to xl
    jobs.to_excel("indeed.xlsx", index=False, sheet_name='sheet1')

# extract digits from salary range
def str_to_numerical(stringValue):
    multiply = stringValue.find('K')
    if(multiply <=0 ):
        multiply = 1
    else:
        multiply = 1000
    regex = re.findall(r"[-+]?(?:\d*\.*\d+)", stringValue)
    res = float(''.join(regex)) * multiply
    return res

# format job salary range into number
def format_salary(salary):
    temp = salary.split('-')
    yearlySalary = temp[1].find('a year') if len(temp) == 2 else temp[0].find('a year')
    temp = str_to_numerical(temp[1]) - str_to_numerical(temp[0]) if len(temp) == 2 else str_to_numerical(temp[0])
    if(not yearlySalary > 0): 
        temp = temp * 2080
    return temp

extract_job_from_result(driver)
