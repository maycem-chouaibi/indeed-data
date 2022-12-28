import re

class Job:
    def __init__(self, companyID='', jobTitle='', company='', location='', salary=0, description=''):
        self.companyID = companyID
        self.jobTitle = jobTitle
        self.company = company
        self.location = location
        self.salary = salary
        self.description = description

    # extract digits from salary range
    def str_to_numerical(self, stringValue):
        multiply = stringValue.find('K')
        if(multiply <=0 ):
            multiply = 1
        else:
            multiply = 1000
        regex = re.findall(r"[-+]?(?:\d*\.*\d+)", stringValue)
        if(len(regex) == 0):
            regex = ['0']
        res = float(''.join(regex)) * multiply
        return res
    # format job salary range into number
    def format_salary(self, salary):
        temp = salary.split('-')
        yearlySalary = temp[1].find('a year') if len(temp) == 2 else temp[0].find('a year')
        temp = self.str_to_numerical(temp[1]) - self.str_to_numerical(temp[0]) if len(temp) == 2 else self.str_to_numerical(temp[0])
        if(not yearlySalary > 0): 
            temp = temp * 2080
        return temp

    def to_list(self):
        return [self.jobTitle , self.company, self.location, self.salary, self.description]

        
