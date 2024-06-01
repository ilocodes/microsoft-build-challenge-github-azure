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

# Describe standard workflow syntax elements

- **Name:** Optional but recommended. Identifies the workflow and appears in the GitHub UI.
- **On:** Specifies the event or events that trigger the workflow.
- **Jobs:** Contains one or more jobs to be executed.
- **Runs-on:** Specifies the runner to use for the jobs.
- **Steps:** Contains the list of steps for each job, executed on the same runner.
- **Uses:** Specifies predefined actions to be retrieved and used.
- **Run:** Executes a command on the runner, such as an NPM command.

# Explore Events

 Different types of events that can trigger workflows in GitHub Actions:

- **Scheduled events:** Trigger workflows based on a cron schedule.
- **Code events:** Triggered by specific actions in the repository, like pull requests or pushes.
- **Manual events:** Allow for manual triggering of workflows.
- **Webhook events:** Triggered by GitHub webhook calls, like updates to Wiki pages.
- **External events:** Can be triggered by `repository_dispatch`, allowing external systems to trigger workflows.

Each event type is demonstrated with a YAML example showing how to configure it in a workflow definition.

# Explore Jobs

- Workflows contain one or more jobs. A job is a set of steps that will be run in order on a runner.
- Steps within a job execute on the same runner and share the same filesystem.
- The logs produced by jobs are searchable, and artifacts produced can be saved.

# Explore Runner

This guide explores the two main types of runners used in GitHub Actions: GitHub-hosted and self-hosted runners.

## Understanding Runners

- Runners are compute resources that execute workflows defined in GitHub Actions.
- Each runner can handle one job (a sequence of steps) within a workflow at a time.
- They enable building, testing, and deploying projects directly within GitHub repositories.

## Types of Runners

### GitHub-hosted runners:

- Convenient option with no infrastructure management required by users.
- Scales automatically based on demand.
- Offers pre-configured environments with various operating systems (Ubuntu, Windows, macOS).
- Includes basic built-in tools (grep, find, which on Ubuntu/macOS).
- Additional software installation possible within workflows.
- Secure and isolated execution environment for each workflow run.
- Seamless integration with GitHub Actions.
- Limited job execution time (max 6 hours) and workflow run time (max 35 days).
- Free tier available, with usage-based billing beyond that.

### Self-hosted runners:

- Provide greater control and customization for execution environments.
- Can be deployed on-premises or in the cloud for flexibility.
- Fully customizable hardware, software, and network configurations.
- Integrates with existing infrastructure and tools.
- No limits on job or workflow run execution time.
- Requires user setup, configuration, and management.
- Open-source runner software available on GitHub.
- Requires outbound network connectivity and authentication for GitHub access.
- Users are responsible for updates, security patches, monitoring, and troubleshooting.
- No additional licensing cost beyond GitHub Actions and infrastructure expenses.

## Choosing the Right Runner

- GitHub-hosted runners: Ideal for most use cases due to ease of use, scalability, and security.
- Self-hosted runners: Preferred for specific needs like custom environments not offered by GitHub-hosted runners, integration with on-premises infrastructure or tools, and unlimited execution time for long-running tasks.

## Security Considerations

- GitHub strongly discourages using self-hosted runners for public repositories due to potential security risks.

## Additional Notes

- Both runner types use YAML workflows stored in the `.github/workflows` directory of your repository.
- Self-hosted runner registration can occur at the repository, organization, or enterprise level.

# Explore release and test an action

This section explores how to view action output, manage releases, and test actions within GitHub Actions.

## Viewing Action Output

- Action execution console output is readily available within the GitHub UI.
- Navigate to **Actions** in the repository menu.
- Select a specific workflow to view its output.
- Click on the job name to see the individual steps' output.
- This output helps with debugging actions. Additional logging can be enabled if needed (refer to documentation on enabling debug logging).

## Managing Action Releases

While using the latest action version might be convenient, specific versions are sometimes required. Here's how to request a specific release:

- **Tags:** Specify the exact version you desire (e.g., `actions/install-timer@v2.0.1`).
- **SHA-based Hashes:** Define a specific SHA hash for the action, ensuring it hasn't been modified. However, this approach also prevents automatic updates.
- **Branches:** Refer to a specific branch (e.g., `actions/install-timer@develop`) to get the latest version from that branch. This allows for updates but increases the risk of code changes breaking your workflow.

