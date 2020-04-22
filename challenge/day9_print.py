import requests
from flask import Flask, render_template, request

v0 = "http://hn.algolia.com/api/v1"
# https://news.ycombinator.com/


# This URL gets the newest stories.
new = f"{v0}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{v0}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{v0}/item/{id}"

# f"{v0}/user/

db = {} # fake DB??? db[].get db[id] = detail
app = Flask("DayNine")

# / 

# /<id>

#The v0 API is essentially a dump of our in-memory data structures. We know, what works great locally in memory isn't so hot over the network. Many of the awkward things are just the way HN works internally. Want to know the total number of comments on an article? Traverse the tree and count. Want to know the children of an item? Load the item and get their IDs, then load them. The newest page? Starts at item maxid and walks backward, keeping only the top level stories. Same for Ask, Show, etc.

#I'm not saying this to defend it - It's not the ideal public API, but it's the one we could release in the time we had. While awkward, it's possible to implement most of HN using it.


######################################################
@app.route("/")
def index() :
  # toggle
  # /?order_by=new
  # /?order_by=popular <- default

  # hits : hits
  return render_template("index.html")

@app.route("/<id>")
def detail() :

  # "title" : title
  # "score" : score
  # "by" : by
  # "url" : url
  # "children" : children
  return render_template("detail.html")
######################################################

app.run(host="127.0.0.1")