"""
Implements Flask api for extracting text from pdf / html 

Adapted from https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html

"""

import argparse
import logging
import json
from flask import Flask, request
from flask_restful import Resource, Api

from text2pdf import (
    get_text_from_url,
)

logger = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app)

# Resource for crawling websites

class TextForUrl(Resource):
    # Resource for fetching and storing text of url stored in database with given link_id
    def get(self):
        # Adding http
        url = request.args.get('url')

        logger.info(f"url={url}")
        return get_text_from_url(url)

# Test Resource
class HelloWorld(Resource):
    def get(self):
        return {"this": "works"}



# Define Routes for resources
api.add_resource(TextForUrl, "/textforurl")
api.add_resource(HelloWorld, "/")


if __name__ == "__main__":
    # Parse arguments on how to start the web app
    parser = argparse.ArgumentParser(description="some settings.")
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        nargs=1,
        default=[80],
        help="port on which to serve the app",
        metavar="PORT",
    )
    args = parser.parse_args()
    port = args.port[0]

    # Dev or production server
    # host 0.0.0.0 to allow connectiosn from outside the container
    logger.info("start dash with flask development server")
    app.run(port=port, debug=True, host="0.0.0.0")

