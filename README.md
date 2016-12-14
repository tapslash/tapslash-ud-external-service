# Tapslash External Service Tutorial

This tutorial will walk you through the steps to set up and deploy an [external service](http://documentation.tapslash.com/docs/external-services).

# clone this repository

```
git clone "https://github.com/tapslash/external-service"
cd external-service
```

# create a new app on heroku

1. If you haven't already, sign up for heroku and open up your [dashboard](https://dashboard.heroku.com/apps).

2. Click **New** -> **Create a New App**.

3. Fill out an **App Name** such as `tapslash-dog-service` then click **Create App**.

4. Select **Heroku Git** as your deployment method.

# deploy your service to heroku

```
heroku git:remote -a tapslash-dog-service
echo " " >> ./README.md
git add .
git commit -m "add a space to the readme"
git push heroku master
```

# test your new endpoint

```
curl "https://tapslash-dog-service.herokuapp.com/"
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

1. Log in to your developer account at [Tapslash](http://developer.tapslash.com/).

2. Click the dropdown menu in the top left, and select **Create**

3. Click **Create A Service**

4. Click **External Service**

5. Set **Category** and **Description** to whatever you want.

6. Set **Service Name** to `dogs`.

7. Set **Service URL** to `https://tapslash-dog-service.herokuapp.com/`.

8. Select a valid 300x300 png Flat Icon. (near the bottom)

9. **Submit**

# add the service to your app

1. Navigate to your App under the dropdown menu.

2. Click **Services**

3. Search for the **dogs** service you've just created.

4. Click **Add Service**

# you're all done!

If you have a Tapslash client pointed at this app you should see the dogs service show up in your bar.

