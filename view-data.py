import matplotlib.pyplot as plt
import pandas as pd


def plot_data(): 
    dataset = pd.read_excel('indeed.xlsx')

    company = dataset['Company']
    salary = dataset['Salary']
    
    plt.bar(company, salary)
    plt.title('Salary by company')
    plt.xticks(rotation=40)
    plt.xlabel('company')
    plt.xlabel('salary')
    plt.show()

plot_data()