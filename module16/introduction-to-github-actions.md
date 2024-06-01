# What are actions?

GitHub Actions automate tasks within your repositories. They're like mini-programs written in YAML that live alongside your code. These actions can handle various tasks beyond CI/CD, including:

- Running automated tests
- Responding to issues and mentions
- Triggering code reviews
- Managing pull requests and branches
Actions run on machines called runners, which can be hosted by GitHub or set up by you. There's also a marketplace where you can find pre-built actions for common tasks.

# Explore Actions flow

- GitHub tracks events that occur. Events can trigger the start of workflows.
- Workflows can also start on cron-based schedules and can be triggered by events outside of GitHub.
- They can be manually triggered.
- Workflows are the unit of automation. They contain Jobs.
- Jobs use Actions to get work done.

# Understand Workflows

Workflows define automated tasks within your GitHub repository using YAML files. They live in the .github/workflows folder of your repository.

## Key Components:

- **Triggers**: Specify events that initiate the workflow (e.g., pushing code, creating an issue).
- **Jobs**: Outline the actions to be executed within the workflow. Each job defines its execution environment, such as the runner to use.

In essence, workflows orchestrate the automation process within your repository. 

### Describe standard workflow syntax elements

- **Name:** Optional but recommended. Identifies the workflow and appears in the GitHub UI.
- **On:** Specifies the event or events that trigger the workflow.
- **Jobs:** Contains one or more jobs to be executed.
- **Runs-on:** Specifies the runner to use for the jobs.
- **Steps:** Contains the list of steps for each job, executed on the same runner.
- **Uses:** Specifies predefined actions to be retrieved and used.
- **Run:** Executes a command on the runner, such as an NPM command.

### Explore Events

 Different types of events that can trigger workflows in GitHub Actions:

- **Scheduled events:** Trigger workflows based on a cron schedule.
- **Code events:** Triggered by specific actions in the repository, like pull requests or pushes.
- **Manual events:** Allow for manual triggering of workflows.
- **Webhook events:** Triggered by GitHub webhook calls, like updates to Wiki pages.
- **External events:** Can be triggered by `repository_dispatch`, allowing external systems to trigger workflows.

Each event type is demonstrated with a YAML example showing how to configure it in a workflow definition.


