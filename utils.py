import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import requests
from contextlib import closing
from requests.exceptions import RequestException, ConnectionError


"""Helper functions from https://realpython.com/python-web-scraping-practical-introduction/"""
def fetch_html_or_pdf(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(requests.get(url, stream=True, timeout=7)) as resp:
            content_type = resp.headers["Content-Type"].lower()
            if content_type.find('html') > -1:
                content_type = 'html'
            elif content_type.find('pdf') > -1:
                content_type = 'pdf'
            else:
                logger.warning("Wrong content type {}. Returning None".format(content_type))
                return None
            return resp.content, resp.status_code, content_type, resp.url

    except (RequestException, UnicodeDecodeError, KeyError) as e:
        logger.error("Error during requests to {0} : {1}".format(url, str(e)))
        return None
