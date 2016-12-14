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
echo " " >> README.md
git add .
git commit -m "add a space to the readme"
git push heroku master
```

# test your new endpoint

```
curl ""
```
 
