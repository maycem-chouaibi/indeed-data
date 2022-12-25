# Created by Mayssem CHouaibi
# Class for scraping indeed data

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the chrome driver. Starts the service and then creates new instance of chrome driver
driver = webdriver.Chrome(executable_path="PATH_HERE/chromedriver.exe")
URL = "https://www.indeed.com/jobs?q=data+scientist&l=New+York"
driver.get(URL)

def extract_job_from_result(driver): 
    # Initialize dataframe
    jobs = pd.DataFrame(columns=['Title', 'Company', 'Location', 'Slary', 'Description'])
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
            for companyName in company.find_elements(By.TAG_NAME,'a'):
                jobCompany = companyName.text

        for companyLocation in job.find_elements(By.CLASS_NAME,'companyLocation'):
            jobLocation = companyLocation.text
    
        for salaryContainer in job.find_elements(By.CLASS_NAME,'salaryOnly'):
            for salary in salaryContainer.find_elements(By.CLASS_NAME, 'salary-snippet-container'):
                for salaryRange in salary.find_elements(By.CLASS_NAME,'attribute_snippet'):
                    jobSalary = salaryRange.text

        for description in job.find_elements(By.CLASS_NAME,'job-snippet'):
            for jobDesc in description.find_elements(By.TAG_NAME,'li'):
                jobDescription = jobDesc.text

        # add to df
        jobs.loc[len(jobs.index)]=[jobTitle, jobCompany, jobLocation, jobSalary, jobDescription]
    return jobs

print(extract_job_from_result(driver))