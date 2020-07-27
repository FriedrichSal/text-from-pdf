"""
Function for extracting text from pdfs and html
"""
import logging
import io
import datetime
import requests
import json
import pdftotext
import html2text

from utils import fetch_html_or_pdf

logger = logging.getLogger(__name__)

def get_text_from_url(url):
    """
    Queries url
    """

    # Query url
    logger.info("Procssing {}".format(url))
    content, status_code, content_type, resp_url = fetch_html_or_pdf(url)
    assert(status_code == 200)


    # Deal with PDF content
    if (content_type == "pdf"):
        # Check that content type matches the one stored in db
        logger.info("Detected PDF content")
        pdf_file = io.BytesIO(content)
        try:
            pdf = pdftotext.PDF(pdf_file)
            url_text = "\n\n".join(pdf)
            return url_text

        except Exception as e:
            logger.error(e)
            logger.error("Could not get text from {}. Set to empty string.".format(url))
            return None

    # Deal with HTML contnet
    elif content_type == 'html':
        logger.info("Detected HTML content")

        # Convert html to text
        h = html2text.HTML2Text()
        h.ignore_links = True
        try:
            url_text = h.handle(content.decode("utf-8"))

            return url_text
        except UnicodeDecodeError as e:
            logger.error("Could not decode response content", exc_info=True)
            return None

    # Ivalid Content type
    else:
        logger.error("Invalid content_type {} encountered.".format(content_type))
        return None
