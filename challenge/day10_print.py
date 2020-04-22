import os
import requests
from flask import Flask, render_template, request, redirect

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"

os.system("clear")

# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")

# 기본 popular
@app.route("/")
def home():
  
  order = request.args.get("order_by")
  fake_db = db.get(order)
  if fake_db: # db get
    hits = fake_db
    toggle = order
  else: # requests

    if order == 'new':
      get_request = requests.get(new)
      toggle = "new"
    else:
      get_request = requests.get(popular)
      toggle = "popular"

    if get_request.status_code == 200:
      json = get_request.json()
      hits = json['hits']
      db[toggle] = hits

    else:
      return redirect("/")

  return render_template(
      "index.html",
      hits=hits,
      toggle=toggle
    )

@app.route("/<id>")
def detail(id):
  detail = make_detail_url(id)
  fake_data = db.get(id)
  if fake_data:
      title = fake_data.get("title")
      points = fake_data.get("points")
      author = fake_data.get("author")
      url = fake_data.get("url")
      children = fake_data.get("children")
  else:
    get_request = requests.get(detail)
    if get_request.status_code == 200:
      json = get_request.json()
      title = json.get("title")
      points = json.get("points")
      author = json.get("author")
      url = json.get("url")
      children = json.get("children")
      # fake db
      detail = {
        "title": title,
        "points": points,
        "author": author,
        "url": url,
        "children": children
      }
      db[id] = detail
    else:
      return redirect("/")

  return render_template(
    "detail.html",
    title=title,
    points=points,
    author=author,
    url=url,
    children=children
  )
  

app.run(host="127.0.0.1")