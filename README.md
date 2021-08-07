# DevOps training Application for Bow Valley Collage 

These are some example files that will be used to teach the DevOps course. There is a small web app and a very 
simple API.

Tools used:
* VSCode
* Web
    * HTML
    * CSS
    * JavaScript
* python
    * flask
* Docker
* AWS

## To Build the application
1. Use VSCode to edit the code and make whatever changes to the source that are required. It is highly suggested that you
only change a little before you test, like one line at a time if practical.
1. Test locally
    * pipenv shell
    * pipenv install (Only needed once or when a new package is used)
    * py app.py
    * In the browser: localhost:5000 
    * test in browser with this [link to localhost:5000!](http://localhost:5000)
    * note that the host name should be your computer's name
1. Build the Docker container locally and test
    * In VSCode in the Explorer / Project view; right click on the file named **Dockerfile** and select the **Build Image...** option.
    A new Image is created on your local machine.
    * Start Docker Desktop
    * In the **Containers / Apps** tab, make sure there is no **devopstraining** container running. If so put your mouse
    over the Container and select the delete option.
    * In the **Images** tab, there should be a **devopstraining** image.
    * as you move your mouse over the image a **RUN** option will display. Select it.
    * A **New Container** dialog will display. Select the **Optional Settings** dropdown.
    * In the **Ports / Local Host** enter **5010**. Press Run. 
    * Test the app running in the container [localhost:5010](http://localhost:5010). You can use any 
    available port number instead of 5010.
1. Push changes to the repository. The repository is hosted on AWS CodeCommit.







# ----- Sample info below -----

```
Some piece of code in here
```

## General Info

Some Stuff

* Point
* Point

Ordered List
1. Stuff
1. Stuff
    1. Stuff
    1. Stuff
    1. Stuff
1. Stuff

It's very easy to make some words **bold** and other words *italic* with Markdown. You can even [link to Google!](http://google.com)

![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
