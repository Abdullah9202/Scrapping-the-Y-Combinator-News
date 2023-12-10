import requests
import bs4

# Making request
response = requests.get(url="https://news.ycombinator.com/")
# Response text
response_Txt = response.text
# Soup
soup = bs4.BeautifulSoup(response_Txt, 'html.parser')

# Heading
heading = soup.select_one(selector="span.pagetop b.hnname a")
print(heading.getText())

# Getting News and authors and points
raw_News_List = []
raw_Point_List = []
raw_author_List = []
raw_anker_link_list = []

# Getting the news
for news in soup.select(selector='td.title span.titleline a[rel="noreferrer"]'):
    raw_News_List.append(news.getText())

# Getting authors
for author in soup.select(selector="td.title span.titleline span a span.sitestr"):
    raw_author_List.append(author.getText())
    
# Getting the anker links
for link in soup.select(selector='td.title span.titleline a[rel="noreferrer"]'):
    raw_anker_link_list.append(link.get('href'))
    
# Getting the points
for point in soup.select(selector="td.subtext span.subline span.score"):
    raw_Point_List.append(int(point.getText().split(" ")[0]))

# Combining the news, authors and links
news_author_List = [f"{news} by {author} (Visit: {link})" for news, author, link in zip(raw_News_List, raw_author_List, raw_anker_link_list)]

# Making a sorted dict of points and news
news_author_Link_Dict = dict(sorted({point: news for point, news in zip(raw_Point_List, news_author_List)}.items(), reverse=True))

for count, news in enumerate(news_author_Link_Dict.values()):
    print(f"{count + 1}: {news}")