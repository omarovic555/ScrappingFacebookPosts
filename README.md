### ScrappingFacebookPosts contains Python web services that implement web scraping logic, as well as a set of utilities that simplify the task of managing scraped data. The repository is organized into several directories, including "apis", "services", and "tests", which contain the core functionality of the web scraping logic.

### first of all, you need to install docker to containerize the scrapping services, as you notice there are three dockerfiles, the first offers two webservices ( fb_posts_scrapping.py and save_scrapping_data.py ) the first one which extracts the data posts of a facebook page and the second which saves this result in an Alchemy database, the second file is to test the two webservices and the last dockerfile is to launch a telegram bot which takes the page id as a parameter facebook and return scrapping result in telegram chat.

### So before building the 3 images from the dockerfiles Don't forget to set a config.env file in \app directory  which contains an environment variable which contains the token value for the telegram bot.

### Then run these commands to build the images and run the containers in the ScrappingFacebookPosts\app directory

```shell
$ docker build -t my_telegram_image_app -f ../Dockerfile.telegram .

$ docker build -t my_test_image_app -f ../Dockerfile.test .

$ docker build -t my_image_app -f ../Dockerfile .

$ docker run my_test_image_app

$ docker run my_image_app

$ docker run my_telegram_image_app
```

### Open the Desktop docker and go to the Logs part of the containers being run to see the result and you can even test the APIs with the curl command in the Terminal part by typing:

```shell
# curl http://127.0.0.1:8000/savedata?pageId=GuinnessWorldRecords
```
