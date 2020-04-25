import requests
import csv
from io import StringIO
from flask import Flask, render_template, request, redirect, Response, send_file
from bs4 import BeautifulSoup
from scrapper import aggregated_jobs

app = Flask("RemoteJobs")

db = {}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search")
def search():
  term = request.args.get("term").lower()
  
  websites = [ {"name": "stackoverflow", "url": f"https://stackoverflow.com/jobs?r=true&q={term}"}, {"name": "weworkremotely", "url": f"https://weworkremotely.com/remote-jobs/search?term={term}"},{"name": "remoteok", "url": f"https://remoteok.io/remote-dev+{term}-jobs"}]

  if term not in db:
    jobs = aggregated_jobs(websites)
    db[term] =jobs
  jobs = db[term]
  
  return render_template("home2.html", jobs=jobs, term=term)

@app.route("/export")
def export():
  term = request.args.get("term").lower()
  def generate(): 
    data = StringIO()
    w = csv.writer(data)

    # write header
    w.writerow(("Title", "Company","Link"))
    yield data.getvalue()
    data.seek(0)
    data.truncate(0)

    # write each log item
    for job in db[term]:
      w.writerow((job["title"], job["company"], job["url"]))
      yield data.getvalue()
      data.seek(0)
      data.truncate(0)

  # stream the response as the data is generated
  response = Response(generate(), mimetype='text/csv')
  # add a filename
  response.headers.set("Content-Disposition", "download",filename = f"{term}.csv")
  return response
app.run(host="127.0.0.1")