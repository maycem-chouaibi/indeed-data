import scrape
import kmeansclustering
import hierarchicalClustering

scrape.jobs_to_excel(scrape.get_jobs())
kmeansclustering.cluster()
hierarchicalClustering.cluster()

