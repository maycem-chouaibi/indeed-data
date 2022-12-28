import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

def cluster():
    df=pd.read_excel('indeed.xlsx')

    # Create and fit the KMeans model
    data = pd.DataFrame(list(zip(df['CompanyID'], df['Salary'])),columns=['Company', 'Salary'])
    kmeans = KMeans(n_clusters=4).fit(data)

    # Find the centroids of the clusters
    centroids = kmeans.cluster_centers_

    # Get the associated cluster for each data record
    kmeans.labels_

    # Display the clusters contents and their centroids
    plt.scatter(data['Company'], data['Salary'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
    plt.xlabel('Company')
    plt.ylabel('Salary')
    plt.show()