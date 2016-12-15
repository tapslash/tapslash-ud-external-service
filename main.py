""" Flask App which implements Urban Dictionary as a Tapslash External Service. """
import json
import os

from flask import Flask
from flask import request
import unirest

app = Flask(__name__)

MASHAPE_KEY = os.environ["MASHAPE_KEY"]

URBAN_DICTIONARY_URL = "https://mashape-community-urban-dictionary.p.mashape.com/define?term={}"

@app.route("/")
def index():
    """ Returns json search result objects. """

    # Parse query parameter.
    query = request.args.get("q", "hacker") # if no parameter is supplied "hacker" is default ;)

    # Request search results from Urban Dictionary.
    response = unirest.get(
        URBAN_DICTIONARY_URL.format(query),
        headers={
            "X-Mashape-Key": MASHAPE_KEY,
            "Accept": "application/json"
        }
    )

    # Map Urban Dictionary results into Tapslash results.
    results = [
        {
            "title": item["word"],
            "subtitle": item["definition"],
            "uid": item["defid"],
            "url": item["permalink"],
            "detail": {},
            "image": {
                "url": "https://lh5.googleusercontent.com/-rY97dP0iEo0/AAAAAAAAAAI/AAAAAAAAAGA/xm1HYqJXdMw/s0-c-k-no-ns/photo.jpg",
                "width": "1024",
                "height": "1024"
            },
            "display_type": "default",
            "output": item["permalink"]
        }
        for item in json.loads(response.raw_body).get("list", [])
    ]

    return json.dumps(
        # Put the results under the "results" field on the response object.
        {"results": results},
        # Not neccesary to indent, but looks nice for this demo.
        indent=2
    )

if __name__ == "__main__":
    app.run()
