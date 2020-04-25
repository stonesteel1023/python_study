import requests
from bs4 import BeautifulSoup

def extract_job(html,website_name):
  if website_name == "stackoverflow":
    link = html.find("a", class_="s-link")
    if link:
      title = link["title"]
      url = f"https://stackoverflow.com{link['href']}"
    company = html.find("h3", class_="fs-body1").find("span")
    if company:
      company = company.text.strip()
  
  if website_name == "weworkremotely":
    company = html.find("span", class_="company")
    if company:
      company = company.text.strip()

    title = html.find("span", class_="title")
    if title:
      title = title.text.strip()

    urls = html.find_all("a")
    
    if len(urls) == 1:
      url = f"https://weworkremotely.com{urls[0]['href']}"
    elif len(urls) >= 2:
      url = f"https://weworkremotely.com{urls[1]['href']}"
    else:
      url = None

  if website_name == "remoteok":
    company = html.attrs["data-company"]
    if company:
      company = company.strip()

    url = html.attrs["data-url"]
    if url:
      url = f"https://remoteok.io{url}"
    
    title = html.find("h2", {"itemprop":"title"})
    if title:
      title = title.text.strip()
    
  if title and url and company:
    return {"title": title, "url": url, "company": company}
  else:
    return None

def scrape_jobs(website):
  all_jobs = []
  try:
    request = requests.get(website["url"])
    print(website["name"], request)
    soup = BeautifulSoup(request.text, "html.parser")
    job_container = []
    if(website["name"] == "stackoverflow"):
      job_container = soup.find_all("div", class_="-job")
    elif (website["name"] == "weworkremotely"):
      job_container = soup.find("section", class_="jobs").find_all("li")
    elif (website["name"] == "remoteok"):
      job_container = soup.find_all("tr", class_="job")
    
    for job in job_container:
      extracted_job = extract_job(job, website["name"])
      if extracted_job:
        all_jobs.append(extracted_job)

  except Exception:
    pass
  return all_jobs

def aggregated_jobs(websites):
  aggregated = []
  
  for website in websites:
    jobs = scrape_jobs(website)
    aggregated = aggregated + jobs

  return aggregated