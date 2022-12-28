import scrape
import kmeansclustering

scrape.jobs_to_excel(scrape.get_jobs())
kmeansclustering.cluster()

