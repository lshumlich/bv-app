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
* AWS cli

## To Build the application

1. Use VSCode to edit the code and make whatever changes to the source that is required. It is highly suggested that you
only change a little before you test the app, like one line at a time if practical.

1. Test locally
    * pipenv shell
    * pipenv install (Only needed once or when a new package is used)
    * py app.py
    * In the browser: localhost:5000 
    * test in browser with this [link to localhost:5000!](http://localhost:5000)
    * note that the hostname should be your computer's name.

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

1. Push changes to the source code repository. The repository is hosted on AWS CodeCommit. ??? Larry add documentation on how to create a repository and push to it. ???

1. Use CodeBuild to test and push a new Docker image to AWS Elastic Container Repository (ECR)
    1. To create a CodeBuild project, select CodeBuild from the services dropdown:
        * Select **Build projects** from the left menu
        * Select **Create build project** button
        * The **Create build project** should display
            * Enter **MyBuildProject** for Project Name
            * Select **AWS CodeCommit** for Source provider
            * Select **devops_training** for Repository
            * Select **Branch** for Reference type
            * Select **Main** for Branch
            * Select **Managed image** box for Environment Image
            * Select **Ubuntu** for Operating system
            * Select **Standard** for Runtime(s)
            * Select highest number for Image
            * Select **Linux** for Environment type
            * Click **Privileged** true
            * Leave **New service role** for Service role
            * Leave Role name
            * Enter **buildspec.yml** for Buildspec name
            * Select **Create build project** button
            * The project should be created. 
            * IMPORTANT: Find the service role that has been defined. It is on the Build details tab of the project. 
                * Select the **Service role** link, preferably in a new tab in the browser
                * Select the **Add policy** button
                * In the **Attach Permissions** page search for **ecr**
                * Select the box beside **EC2InstanceProfileForImageBuilderECRContainerBuilds** and click it on
                * Select **Attach policy** button
            * Now Start the build, as defined in the next step.

    1. To manually trigger a new build once the Build Project is defined, select CodeBuild from the services dropdown.
        * Select **Build projects** from the left menu
        * Select **MyBuildProject** from the projects
        * Select **Start build** button
        * In a few minutes the project should run which will run the tests and create a new docker image with the new version of the software






    * Make sure the IAM policy to read the source code repository in Code

1. Create a Docker image and push it to AWS Elastic Container Repository (ECR)
    * Create a CodeBuild project to: run the tests, build the docker container, push the container to ECR. 
    ??? Doc how and where to do this ??? 
    * For now, run the CodeBuild Project called DevOps-train4. This currently runs file buildspec.yml on the root of this project.
    * References
        * https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker.html
        * https://docs.aws.amazon.com/codebuild/latest/userguide/test-reporting.html


1. Deploy the image on AWS manually
    * Select Amazon Elastic Container Service (ECS)
    * Create a Task
        * Select **Task definitions** from the menu in upper left hand side in the ECS main page
            * Select **Create new Task Definition** button
            * Select **FARGATE** box
            * Select **Next step** button
        * The **Configure task and container definitions** page should display
            * Enter **MyECSTaskDef** in Task Definition Name
            * Select the **ecsTaskExecutioinRole** from the dropdown
            * Select **.5GB** from the dropdown
            * Select **0.25vCPU** from the dropdown
            * Select **Add a container**
        * The **Add container** page should display
            * Enter **MyTaskContainer** in Container name
            * Enter your version of **208019545904.dkr.ecr.ca-central-1.amazonaws.com/devops:latest** in Image
            * Enter **5000** in port
            * Select **Add** button
        * The **Configure task and container definitions** page should display again
            * Select **Create**
            * The **Launch Status** page should display
            * Select **View task definition**


    * Create a Cluster

        * Select **Clusters** from the menu in upper left hand side in the ECS main page
            * Select **Create cluster** button
            * Select **Networking only** box
            * Select **Next step** button
        * The **Configure cluster** should display
            * Enter: **MyECSCluster** for Cluster name
            * Select **Create**
            * Select **View Cluster** button
        * The **MyECSCluster** should display
            * Select **Deploy** button
        * The **Deploy** page should display
            * Select **Service** box
            * Select **MyECSTaskDev** in the Family dropdown
            * Select **The Latest** in Revision
            * Enter **MyECSService** in Service name
            * Spec ---
            * Leave Deployment type to **Rolling update**

    * The ?????? Start Here Larry



1. Deploy the image on AWS using CloudFormation.
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



1. Deploy an update to a running ECR cluster
    * To understand [ECR Deploy Concepts with CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps-ecs.html)
    read this artical.
    * This seems like a good step by step???: [step by step](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-deployment.html)
    There is reference in this artical for:
        * information about how to use CodePipeline to detect and automatically deploy changes to an Amazon ECS service with CodeDeploy
        *  Tutorial: Creating a service using a blue/green deployment
    * ??? Larry Finish This



1. Copy the python docker image to your ECR. We do this to avoid docker limits when building and running.
    * In ECR create a repository called python.
    * Select the repository and push the **View push commands** 
    * We modify them slightly to:
        1. aws ecr get-login-password --region ca-central-1 | docker login --username AWS --password-stdin 208019545904.dkr.ecr.ca-central-1.amazonaws.com
        1. docker pull python:3.8-slim-buster
        1. docker tag python:3.8-slim-buster 208019545904.dkr.ecr.ca-central-1.amazonaws.com/python:3.8-slim-buster
        1. docker push 208019545904.dkr.ecr.ca-central-1.amazonaws.com/python:3.8-slim-buster



1. CloudFormation Info
    * https://docs.aws.amazon.com/cloudformation/index.html
    * https://github.com/awslabs/aws-cloudformation-templates/
    * https://aws.amazon.com/cloudformation/resources/templates/
    * https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green.html


Questions:
    * Setting up target groups
    * Assigning trafic to the target groups

LoadBalancer
    Listeners Forward to TargetGroups with Rules 



A listener is attached to a Service

Info 

## To Do

(How to show/teach the students to do this in 1.5 weeks)

1. Automate the build process so the container gets built when new code is checked in.
1. Automate the deploy process so the container gets deployed when the container gets built.
    * do a simple deploy
    * use a blue green deploy strategy
1. Run the tests. Determine if the tests can and should be run inside the Docker container?
1. Publish test results
1. 







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

# Usefull Commands

208019545904.dkr.ecr.ca-central-1.amazonaws.com/devops@sha256:03f4fb0fbce187c605046658f734c49bef1131d55c9ebdbcdd53b05b8ee98f45

208019545904.dkr.ecr.ca-central-1.amazonaws.com/devops@sha256:3c6109df11e94cf5cb24a12ff7321dbc813cc577efb350f9055e9c11f5278ad1 

docker tag sha256:3c6109df11e94cf5cb24a12ff7321dbc813cc577efb350f9055e9c11f5278ad1 208019545904.dkr.ecr.ca-central-1.amazonaws.com/devops:V10

docker images 208019545904.dkr.ecr.ca-central-1.amazonaws.com/devops

docker images 208019545904.dkr.ecr.ca-central-1.amazonaws.com/devops

 docker tag 0e5574283393 myregistryhost:5000/fedora/httpd:version1.0

 sha256:03f4fb0fbce187c605046658f734c49bef1131d55c9ebdbcdd53b05b8ee98f45

 docker pull 208019545904.dkr.ecr.ca-central-1.amazonaws.com/devops@sha256:03f4fb0fbce187c605046658f734c49bef1131d55c9ebdbcdd53b05b8ee98f45

 docker tag 208019545904.dkr.ecr.ca-central-1.amazonaws.com/devops:latest 208019545904.dkr.ecr.ca-central-1.amazonaws.com/devops:v0.11

 docker tag 7107d2fbc677 208019545904.dkr.ecr.ca-central-1.amazonaws.com/devops:v0.10

 docker push 208019545904.dkr.ecr.ca-central-1.amazonaws.com/devops:v0.10

[Container] 2021/08/10 04:34:56 Running command aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded

[Container] 2021/08/11 03:21:05 Running command aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com
Error response from daemon: Get https://.dkr.ecr.ca-central-1.amazonaws.com/v2/: dial tcp: lookup .dkr.ecr.ca-central-1.amazonaws.com: no such host


