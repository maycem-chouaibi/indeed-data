import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from sklearn.preprocessing import normalize
from sklearn.cluster import AgglomerativeClustering
def cluster():
    #read data
    df = pd.read_excel('indeed.xlsx')

    #Select columns for analysis
    data = pd.DataFrame(list(zip(df['CompanyID'], df['Salary'])),columns=['Company', 'Salary'])

    #This algorithm is sensitive to outliers so we should remove rows whre the salary is 0
    data.drop(data[data['Salary'] <= 0].index, inplace = True)

    #Normalize data
    data_scaled = normalize(data)
    data_scaled = pd.DataFrame(data_scaled, columns=data.columns)

    #Plot dendrogram to find nbre of clusters
    plt.figure(figsize=(10, 7))
    plt.title("Dendrogram")
    shc.dendrogram(shc.linkage(data_scaled, method='ward'))

    #From dendrogram we can see that we need 4 clusters
    cluster = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
    cluster.fit_predict(data_scaled)
    plt.figure(figsize=(10, 7))
    plt.scatter(data_scaled['Company'], data_scaled['Salary'], c=cluster.labels_)
    plt.show()

