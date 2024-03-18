from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    job_listings = soup.find_all('div', class_='media')

    for job in job_listings:
        title = job.find('h2', class_='title').text

        salary = job.find('span', class_='salary').text if job.find('span', class_='salary') else "Salary not provided"

        print("Title:", title)

        print("Salary:", salary)
else:
    print("Failed to retrieve data from the website.")
