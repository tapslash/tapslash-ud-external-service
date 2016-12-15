""" An example external service which returns hard-coded dog pictures. """

import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def results():
    """ Returns json search result objects. """

    dog_result = {
	"subtitle": "a golden retriever",
	"title": "dog",
	"url": "http://imgur.com/gallery/6GuZIHD",
	"uid": "6GuZIHD",
        "detail": {},
	"image": {
	  "url": "http://i.imgur.com/6GuZIHD.jpg",
	  "width": "643",
	  "height": "960"
	},
	"display_type": "default",
	"output": "http://imgur.com/gallery/6GuZIHD"
    }

    # show 3 of the same result
    results = [dog_result, dog_result, dog_result]

    data = {"results": results}
    return json.dumps(data, indent=2)

if __name__ == "__main__":
    app.run()
