import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self.sites = ['https://github.com/SimplifyJobs/Summer2025-Internships']

    def seed_applications(self):
        for item in self.sites:
            response = requests.get(item)
            soup = BeautifulSoup(response.text, 'lxml')
            data_list = []

            prevCompany = ''
            for row in soup.find_all('tr'):
                col = row.find_all('td')
                if col:
                    currCompany = ''
                    row_list = []
                    # Append company name and remove down arrow
                    companyName = row.find('td').text
                    if companyName != "↳":
                        prevCompany = companyName
                        currCompany = companyName
                    else:
                        currCompany = prevCompany
                    row_list.append(currCompany)
                    # Append position name
                    position = row.find('td').find_next('td').text.strip()
                    while '🛂' in position:
                        position = position[:-1]
                    while '🇺🇸' in position:
                        position = position[:-2]
                    row_list.append(position)
                    # Append location(s) name as a list
                    row_list.append(row.find('td').find_next('td').
                                    find_next('td').text.strip())
                    # Append application links - get the application source
                    link = (row.find('td').find_next('td').find_next('td').
                            find_next('td'))
                    if link.text.strip() == '🔒':
                        row_list.append('Application Closed')
                    else:
                        app_link = link.find('a', href=True)
                        if app_link:
                            row_list.append(app_link['href'])
                        else:
                            row_list.append('Application Closed')
                    # Append date to datePosted
                    row_list.append(row.find('td').find_next('td').
                                    find_next('td').find_next('td').
                                    find_next('td').text.strip())
                    # Append application links
                    data_list.append(row_list)
            return data_list
