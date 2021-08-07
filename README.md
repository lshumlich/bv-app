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
1. Use VSCode to edit the code and make whatever changes to the source that is required. It is highly suggested that you
only change a little before you test the app, like one line at a time if practical.
1. Test locally
    * pipenv shell
    * pipenv install (Only needed once or when a new package is used)
    * py app.py
    * In the browser: localhost:5000 
    * test in browser with this [link to localhost:5000!](http://localhost:5000)
    * note that the hostname should be your computer's name
1. Build the Docker container locally and test
    * In VSCode in the Explorer / Project view; right-click on the file named **Dockerfile** and select the **Build Image...** option.
    A new **Image** is created on your local machine.
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
1. Create a Docker image and push it to AWS ECR
    * Create a CodeBuild project to: run the tests, build the docker container, push the container to ECR. 
    ??? Doc how and where to do this ??? 
    * For now, run the CodeBuild Project called DevOps-train4. This currently runs file buildspec.yml on the root of this project.
1. Deploy the image on AWS.
    * ??? Needs some work. 
    * Go to AWS CloudFormation
    * Select Create a stack 
    * Select Options:
        * Template is ready
        * Upload a template file
        * Choose file: **devops_training\CloudFormation\createCluster.yaml**
        * select **Next** button
    * The **specify stack details** should be displayed.
        * Stack name: **Stack1**
        * leave the defaults as is 
        * SubnetA: (Pick first option on the dropdown)
        * SubnetB: (Pick second option on the dropdown)
        * VPC (Pick last option on the dropdown )
        * select **Next** button
    * The **Configure stack options** should display.
        * leave the defaults as is 
        * select **Next** button
    * The **Review Stack1** should be displayed.
        * leave the defaults as is 
        * At the bottom **check** true 'I acknowledge that AWS CloudFormation might create IAM resources with custom names.'
        * select **Create stack** button
        * this could take a few minutes.
        * press the refresh button until the event **Stack1 CREATE_COMPLETE** shows up at the top of the list.
    * Test the application on AWS
        * Select the **Outputs** tab
        * Select the Endpoint value/link
        * Congragulations. Test the application running on AWS.
1. Deploy an update while it's running






## To Do

(How to show/teach the students to do this in 1.5 weeks)

1. Automate the build process so the container gets built when new code is checked in.
1. Automate the deploy process so the container gets deployed when the container gets built.
    * do a simple deploy
    * use a blue green deploy strategy
1. Run the tests. Determine if the tests can and should be run inside the Docker container?







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
