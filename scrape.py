# Created by Mayssem CHouaibi
# Class for scraping indeed data
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from jobClass import Job

def get_jobs():
    # Create a new instance of the chrome driver. Starts the service and then creates new instance of chrome driver
    driver = webdriver.Chrome(executable_path="PATH_HERE/chromedriver.exe")
    jobs = pd.DataFrame(columns=['Title', 'Company', 'Location', 'Salary', 'Description'])

    for i in range(0, 140, 10):
        URL = "https://www.indeed.com/jobs?q=data+scientist&l=New+York&start="+str(i)
        driver.get(URL)
        # Initialize dataframe
        # Extract container for job
        for job in driver.find_elements(By.CLASS_NAME,"job_seen_beacon"):
            # add to df
            extracted = extract_job_from_result(job)
            jobs.loc[len(jobs.index)]=extracted.to_list()
    jobs.insert(0, 'CompanyID', calculate_companyIDs(jobs['Company']))
    return jobs

def extract_job_from_result(job): 
    # Instanciate job object
    jobInstance = Job()
    #extract each element
    for title in job.find_elements(By.CLASS_NAME,'jobTitle'):
        for titleText in title.find_elements(By.TAG_NAME,'span'):
            jobInstance.jobTitle = titleText.text
    
    for company in job.find_elements(By.CLASS_NAME,'companyName'):
        jobInstance.company = company.text
        for companyName in company.find_elements(By.TAG_NAME,'a'):
            jobInstance.company = companyName.text                    

    for companyLocation in job.find_elements(By.CLASS_NAME,'companyLocation'):
        jobInstance.location = companyLocation.text

    for salary in job.find_elements(By.CLASS_NAME, 'salary-snippet-container'):
        for salaryRange in salary.find_elements(By.CLASS_NAME,'attribute_snippet'):
            jobInstance.salary = jobInstance.format_salary(salaryRange.text)
    for salaryInSpanTag in job.find_elements(By.CLASS_NAME, 'estimated-salary'):
        for salaryfinal in salaryInSpanTag.find_elements(By.TAG_NAME,'span'):
            jobInstance.salary = jobInstance.format_salary(salaryfinal.text)
    
    for description in job.find_elements(By.CLASS_NAME,'job-snippet'):
        for jobDesc in description.find_elements(By.TAG_NAME,'li'):
            jobInstance.description = jobDesc.text

    return jobInstance

def jobs_to_excel(jobs):
    # write to xl
    jobs.to_excel('indeed.xlsx', index=False)

# Fct to calculate IDs
def calculate_companyIDs(companyNames):
    companyIDs=[]
    for cn in companyNames:
        companyIDs.append(companyNames.to_list().index(cn))
    return companyIDs
