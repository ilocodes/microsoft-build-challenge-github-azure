# Explore the concept of pipelines in DevOps
DevOps pipelines focus on delivering continuous value to customers by streamlining the software delivery process. Instead of isolated efforts, the process emphasizes an end-to-end flow of value, creating a reliable and repeatable method from concept to customer. This approach involves breaking down the delivery process into stages, each verifying new features to prevent errors and ensure quality. The pipeline includes build automation and continuous integration, test automation, and deployment automation, supported by platform provisioning and configuration management. Continuous feedback and monitoring help identify and resolve obstacles, improving the pipeline's efficiency. Effective orchestration and infrastructure are crucial for the pipeline's success, enabling frequent and reliable delivery of updates.

# Describe Azure Pipelines
Azure Pipelines is a cloud service that automates building, testing, and deploying code projects, supporting continuous integration (CI) and continuous delivery (CD). It is cross-platform, working with various languages (e.g., Python, Java, C#) and integrates with version control systems like GitHub and Bitbucket. Azure Pipelines can deploy to multiple targets, including container registries, virtual machines, and major cloud services like Azure, AWS, and Google Cloud. It supports package management for NuGet, npm, and Maven. Azure Pipelines enhances code quality and consistency by automating tests and deployments, facilitating early bug detection and reliable release management.

# Understand Azure Pipelines Key Terms

Understanding the basic terms and parts of Azure Pipelines helps you further explore how it can help you deliver better code more efficiently and reliably.

![Diagram showing Key pipeline terms with a trigger action, starting the pipeline with multiple stages, using various jobs and tasks to create a build artifact, and start the deployment.](https://learn.microsoft.com/en-us/training/wwl-azure/explore-azure-pipelines/media/key-pipeline-concepts-overview-ca80c85c.png)

## Agent
When your build or deployment runs, the system begins one or more jobs. An agent is installable software that runs a build or deployment job.

## Artifact
An artifact is a collection of files or packages published by a build. Artifacts are made available for tasks such as distribution or deployment.

## Build
A build represents one execution of a pipeline. It collects the logs associated with running the steps and the test results.

## Continuous Delivery
Continuous delivery (CD) (also known as Continuous Deployment) is a process by which code is built, tested, and deployed to one or more test and production stages. Deploying and testing in multiple stages helps drive quality. Continuous integration systems produce deployable artifacts, which include infrastructure and apps. Automated release pipelines consume these artifacts to release new versions and fix existing systems. Monitoring and alerting systems constantly run to drive visibility into the entire CD process. This process ensures that errors are caught often and early.

## Continuous Integration
Continuous integration (CI) is the practice used by development teams to simplify the testing and building of code. CI helps to catch bugs or problems early in the development cycle, making them more accessible and faster to fix. Automated tests and builds are run as part of the CI process. The process can run on a schedule, whenever code is pushed, or both. Items known as artifacts are produced from CI systems. The continuous delivery release pipelines use them to drive automatic deployments.

## Deployment Target
A deployment target is a virtual machine, container, web app, or any service used to host the developed application. A pipeline might deploy the app to one or more deployment targets after the build is completed and tests are run.

## Job
A build contains one or more jobs. Most jobs run on an agent. A job represents an execution boundary of a set of steps. All the steps run together on the same agent.
For example, you might build two configurations - x86 and x64. In this case, you have one build and two jobs.

## Pipeline
A pipeline defines the continuous integration and deployment process for your app. It's made up of steps called tasks.
It can be thought of as a script that describes how your test, build, and deployment steps are run.

## Release
When you use the visual designer, you can create a release or a build pipeline. A release is a term used to describe one execution of a release pipeline. It's made up of deployments to multiple stages.

## Stage
Stages are the primary divisions in a pipeline: "build the app," "run integration tests," and "deploy to user acceptance testing" are good examples of stages.

## Task
A task is the building block of a pipeline. For example, a build pipeline might consist of build and test tasks. A release pipeline consists of deployment tasks. Each task runs a specific job in the pipeline.

## Trigger
A trigger is set up to tell the pipeline when to run. You can configure a pipeline to run upon a push to a repository, at scheduled times, or upon completing another build. All these actions are known as triggers.
