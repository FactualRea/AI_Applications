from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def fetch_website_content(url):
    """
    Return the title and contents of the website at the given url;
    truncate to 2,000 characters as sensible limit
    """
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else "No title found"
    if soup.body:
        for irrelevent in soup.body(['script', 'style', 'img', 'input']):
            irrelevent.decompose()
        text_content = soup.get_text(separator = "\n", strip=True)
    else:
        text = ""
    return (title + "\n\n" + text)[:2_000]