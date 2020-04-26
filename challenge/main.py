import requests
from flask import Flask, render_template, request, redirect, send_file, Response
from bs4 import BeautifulSoup as bs
import csv
from io import StringIO

db = {}
def scrap_jobs(word):
    if word:
        word = word.lower()
        exist_jobs = db.get(word)

        if exist_jobs:
            jobs = exist_jobs
        else:
            ok_jobs = []
            stack_jobs = []
            workwork = Wework_scrapper()
            we_jobs = workwork.get_weworkd_jobs(word)
            jobs = ok_jobs + we_jobs + stack_jobs
            db[word] = jobs
    return jobs

app = Flask("Search Remote Jobs")

@app.route("/")
def home():
    return render_template(
        "home3.html"
    )
    
@app.route("/search")
def search():
    word = request.args.get("word")
    jobs = scrap_jobs(word)
    return render_template(
        "search.html",
        word=word,
        jobs=jobs,
        job_len=len(jobs)
    )
    
@app.route("/export")
def export():
    # word 확인
    term = request.args.get("term")
  
    # fake db 확인
    term = term.lower()
    jobs = db.get(term)

    if jobs:
        print(jobs)
        output = StringIO()
        output.write(u'\ufeff')

        # header
        for idx, key in enumerate(jobs[0].keys()):
            output.write(key)
            if idx < len([*jobs[0].keys()]) - 1:
                output.write(",")
        output.write("\n")
    
        for job in jobs:
            for idx, value in enumerate(job.values()):
                output.write(value)
                if idx < len([*jobs.values()]) - 1:
                    output.write(",")
            output.write("\n")
        
        response = Response(
        output.getvalue(),
        mimetype="text/csv",
        content_type="application/octet-stream",
        )
        response.headers["Content-Disposition"] = f"attachment; filename={term}.csv"
        return response
    else:
        print(jobs)
    
def save_to_file(jobs):
    file = open("list.csv", mode="w")
    write = csv.writer(file)
    write.writerow([*jobs[0].keys()])
    for job in jobs:
         write.writerow([*job.values()])
            
app.run("127.0.0.1")

class Ok_scrapper :
    OK_URL = "https://remoteok.io"
    site_name = "remoteok"

    def extract_job(tr_job):
        title = tr_job.find("td", {"class": "company_and_position"}).find("h2").get_text(strip=True)
        link = tr_job['data-url']
        company = tr_job['data-company']
        job_data = {
            "title": title,
            "company": company,
            "link": f"{OK_URL}/{link}"
        }
        return job_data

    def get_jobs(word):
        get_request = requests.get(f"{OK_URL}/remote-{word}-jobs")
        if get_request.status_code == 200:
            html_parse = bs(get_request.text, "html.parser")
            container = html_parse.find("div", {"class": "container"})
            table = container.find("table", {"id": "jobsboard"})

        tr_jobs = table.find_all("tr", {"class", "job"})
        jobs = []
        # tr 정제
        for tr_job in tr_jobs:
            job = extract_job(tr_job)
            jobs.append(job)

        return jobs

    def get_ok_jobs(word):
        print(f"{site_name} scrapper...")
        jobs = get_jobs(word)
        return jobs
    
class Stack_scrapper :
    LIMIT = 50
    STACK_OF_FLOW_URL = f"https://stackoverflow.com/jobs?sort=i"
    site_name = "stackofflow"

    def get_last_page(word):
        try:
            request = requests.get(f"{STACK_OF_FLOW_URL}&q={word}")
            html_parse = bs(request.text, "html.parser")
            # pagination
            pagination = html_parse.find("div", {"class": "s-pagination"})
            pages = pagination.find_all("a")
            # next 제거후 마지막 page
            last_page = pages[-2].get_text(strip=True)

        except AttributeError:
            return 0
        return int(last_page)

    def extract_job(html):
        div = html.find("div", {"class": "grid--cell fl1"})
        # title  
        title = div.find("h2").find("a")["title"]
        # company, location
        company, location = div.find("h3", {"class": "fs-body1"}).find_all("span", recursive=False)
        company = company.get_text(strip=True)
        if not company or not location:
            print(f"{company} {location}")
    
        # link
        job_id = html['data-jobid']

        return {
            "title": title, 
            "company": company, 
            "link": f"https://stackoverflow.com/jobs/{job_id}"
        }

    def get_jobs(last_page, word):
        jobs = []
        for page in range(last_page):
            print(f" scrapping stack_of_flow page: {page}")
        get_request = requests.get(f"{STACK_OF_FLOW_URL}&q={word}&pg={page + 1}")
        html_parse = bs(get_request.text, "html.parser")
        results = html_parse.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)

        return jobs

    # interface
    def get_stack_of_flow_jobs(word):
        print(f"{site_name} scrapper...")
        last_page = get_last_page(word)
        if last_page == 0:
            return
        jobs = get_jobs(last_page, word)
        return jobs
    
class Wework_scrapper :
    # wework
    WEWORK_URL = "https://weworkremotely.com"
    site_name = "weworkremotely"

    def extract_job(job_section):
        article = job_section.find("article")
        if article:
            job_list = article.find("ul").find_all("li")[:-1]
            jobs = []
        # li tags
        for job in job_list:
            a_section = job.select_one("li > a")
            if a_section:
                link = a_section['href'].strip()
                title = a_section.find("span", {"class": "title"}).get_text(strip=True)
            try:
              (company, _, _,) = a_section.find_all("span", {"class": "company"})
            except ValueError:
              (company, _,) = a_section.find_all("span", {"class": "company"})

            company = company.get_text(strip=True)

            cleaned_job = {
              "company": company,
              "title": title,
              "link": f"{WEWORK_URL}/{link}"
            }
            jobs.append(cleaned_job)

        return jobs

    def get_jobs(word):
        get_request = requests.get(f"{WEWORK_URL}/remote-jobs/search?term={word}")
        if get_request.status_code == 200:
            html_parse = bs(get_request.text, "html.parser")
            # jobs-container
            jobs_container = html_parse.find("div", {"class": "jobs-container"})
            # jobs
            job_section_list = jobs_container.find_all("section", {"class": "jobs"})

        aggregated_wework = []
        # section tags
        for job_section in job_section_list:
            job_list = extract_job(job_section);
            aggregated_wework = aggregated_wework + job_list
        return aggregated_wework

    # interface
    def get_weworkd_jobs(word):
        """ weworkremotely site scrapper """
        print(f"{site_name} scrapper...")
        jobs = get_jobs(word)
        return jobs
    