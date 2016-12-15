# Tapslash External Service Tutorial

This tutorial will walk you through the steps to set up and deploy an [external service](http://documentation.tapslash.com/docs/external-services).

# clone this repository

```
git clone "https://github.com/tapslash/external-service"
cd external-service
```

# deploy your app with heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/tapslash/external-service/)

Take note of the endpoint chosen for your app, and rememberd to replace instances of `YOUR-HEROKU-ENDPOINT` throughout this tutorial.

# test your new endpoint

```
curl YOUR-HEROKU-ENDPOINT
```

should return your json data:

```
{
  "results": [
    {
      "uid": "6GuZIHD",
      "url": "http://imgur.com/gallery/6GuZIHD",
      "output": "http://imgur.com/gallery/6GuZIHD",
      "image": {
        "url": "http://i.imgur.com/6GuZIHD.jpg",
        "height": "960",
        "width": "643"
      },
      "subtitle": "a golden retriever",
      "display_type": "default",
      "title": "dog"
    },
    {
      "uid": "6GuZIHD",
      "url": "http://imgur.com/gallery/6GuZIHD",
      "output": "http://imgur.com/gallery/6GuZIHD",
      "image": {
        "url": "http://i.imgur.com/6GuZIHD.jpg",
        "height": "960",
        "width": "643"
      },
      "subtitle": "a golden retriever",
      "display_type": "default",
      "title": "dog"
    },
    {
      "uid": "6GuZIHD",
      "url": "http://imgur.com/gallery/6GuZIHD",
      "output": "http://imgur.com/gallery/6GuZIHD",
      "image": {
        "url": "http://i.imgur.com/6GuZIHD.jpg",
        "height": "960",
        "width": "643"
      },
      "subtitle": "a golden retriever",
      "display_type": "default",
      "title": "dog"
    }
  ]
}
```

# create an external service on Tapslash

- Log in to your developer account at [Tapslash](http://developer.tapslash.com/).

- Click the dropdown menu in the top left, and select **Create**

- Click **Create A Service**

- Click **External Service**

- Set **Category** and **Description** to whatever you want.

- Set **Service Name** to `dogs`.

- Set **Service URL** to `YOUR-HEROKU-ENDPOINT`.

- Select a valid 300x300 png Flat Icon. (near the bottom)

- **Submit**

# add the service to your app

- Navigate to your App under the dropdown menu.

- Click **Services**

- Search for the **dogs** service you've just created.

- Click **Add Service**

# you're all done!

If you have a Tapslash client pointed at this app you should see the dogs service show up in your bar.

