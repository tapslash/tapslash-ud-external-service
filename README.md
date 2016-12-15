# Tapslash External Service Tutorial - Urban Dictionary (Using Flask)

This tutorial will walk you through the steps to set up and deploy an [external service](http://documentation.tapslash.com/docs/external-services).

## Get an API key for Urban Dictionary (through Mashape)

https://market.mashape.com/community/urban-dictionary

## Deploy With Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy/)

**NOTE**: Heroku will give you an endpoint, substitute that with `YOUR-HEROKU-ENDPOINT`.

## Set your Urban Dictionary API key in Heroku

1. Go to your Heroku App **Settings**

2. Navigate to **Config Vars**

3. Set `MASHAPE_KEY` to your Urban Dictionary (mashape) API key.

## Test Endpoint

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

## Create an External Service on Tapslash

- Log in to your developer account at [Tapslash](http://developer.tapslash.com/).

- Click the dropdown menu in the top left, and select **Create**

- Click **Create A Service**

- Click **External Service**

- Set **Category** and **Description** to whatever you want.

- Set **Service Name** to `dogs`.

- Set **Service URL** to `YOUR-HEROKU-ENDPOINT`.

- Select a valid 300x300 png Flat Icon. (near the bottom)

- **Submit**

## Add the Service to Your App on Tapslash

- Navigate to your App under the dropdown menu.

- Click **Services**

- Search for the **dogs** service you've just created.

- Click **Add Service**

## You're All Done!

If you have a Tapslash client pointed at this app you should see the dogs service show up in your bar.

