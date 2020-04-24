import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def extract_post(html, subreddit):
  votes = html.find("div", {"class":"_1rZYMD_4xY3gRcSS3p8ODO"})
  if votes:
    votes = votes.string
  title = html.find("h3", {"class":"_eYtD2XCVieq6emjKBH3m"})
  if title:
    title = title.string
  link = html.find("a", {"class":"SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"})
  if link:
    link = link['href']
  if votes and title and link:
    return {'votes':int(votes), 'title':title, 'link':link, 'subreddit':subreddit}
  else:
    return None

def scrape_subreddit(subreddit):
  all_posts = []
  try:
    url = f"https://www.reddit.com/r/{subreddit}/top/?t=month"
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, "html.parser")
    post_container = soup.find("div", {"class":"rpBJOHq2PR60pnwJlUyP0"})
    if post_container:
      posts = post_container.find_all("div", {"class": None}, recursive=False)
      for post in posts:
        exctracted_post = extract_post(post, subreddit)
        if exctracted_post:
          all_posts.append(exctracted_post)
  except Exception:
    pass
  return all_posts

def aggregate_subreddits(subreddits):
  aggregated = []
  for subreddit in subreddits:
    posts = scrape_subreddit(subreddit)
    aggregated = aggregated + posts
  return aggregated