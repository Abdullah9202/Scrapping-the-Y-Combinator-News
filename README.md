# Hacker News Headlines

This Python script scrapes the latest headlines from [Hacker News](https://news.ycombinator.com/), displaying them along with their authors and points. It utilizes the `requests` library to make HTTP requests and `BeautifulSoup` from the `bs4` library to parse the HTML content of the webpage.

## How it Works

1. It sends a GET request to the Hacker News website.
2. It parses the HTML content of the webpage using BeautifulSoup.
3. It extracts the headlines, authors, points, and links to the news articles.
4. It combines the headlines with their authors and links.
5. It sorts the news articles based on their points in descending order.
6. It prints the sorted news articles along with their authors.

## Dependencies

- Python 3
- `requests` library
- `beautifulsoup4` library

## Usage

To run the script, simply execute it using Python:

```bash
python script_name.py
