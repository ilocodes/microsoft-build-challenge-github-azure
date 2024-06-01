# Azure Repos

Azure Repos offers version control for your code, catering to both small and large projects. It provides two options:

- **Git**: A popular distributed version control system, allowing offline work and easy collaboration.
- **Team Foundation Version Control (TFVC)**: A centralized system ideal for structured environments.

## Key Benefits of Azure Repos

- **Free Private Hosting**: Unlimited private Git repositories and TFVC support.
- **Flexibility**: Use any Git client for secure access and management.
- **Integration**: Integrate with web hooks and APIs for automation and extension.
- **Intelligent Search**: Find code faster with semantic search features.
- **Collaboration Features**: Streamline code reviews with threaded discussions and continuous integration.
- **Built-in CI/CD**: Automate builds, tests, and deployments through Azure Pipelines or your preferred tools.
- **Code Quality Control**: Enforce high standards with branch policies that require code reviews, successful builds, and passing tests before merging changes.
- **Familiarity**: Use your favorite editors and IDEs with both Git and TFVC repositories.

## Migrating Your Source Code: Restructuring with Git

Migrating to Git offers a chance to reorganize your codebase, especially if your current structure isn't ideal. Since you'll be restructuring, there's little point in migrating historical data. 

Here's a simplified approach:

1. **Create Empty Repositories:** Set up new Git repositories (potentially multiple ones) for the reorganized structure.
2. **Copy and Organize Code:** Transfer and restructure your code into the new Git repositories.
3. **Commit and Push:** Commit your changes and push them to the remote Git repository.

### Shared Code Considerations:

- If you have shared code, create reusable packages and publish them to a package feed before migrating.
- Downstream applications can then consume these packages.

### Azure DevOps Migration Options:

1. **Single Branch Import (TFVC only):**
    - Import a single branch from your TFVC repository into Azure Repos.
    - Offers limited history (up to 180 days).
2. **Import Repository (General):**
    - Import existing Git repositories from various platforms (e.g., GitHub) into Azure Repos.

**Remember:** The single branch import with TFVC is limited to one branch and 180 days of history. However, it's a convenient option if that's all you need within Azure DevOps.

# Migrating Your TFVC History with Git-TFS

This guide explains how to use Git-TFS, an open-source tool, to migrate your entire TFVC codebase (including multiple branches and history) to a Git repository.

## Key Points

### Advantages:

- Migrates multiple branches and preserves branch relationships in Git.
- Allows dry runs to test the migration locally before full execution.

### Considerations:

- Migration can be time-consuming for large repositories.
- Requires .NET 4.5.2 and a specific Team Explorer version (depending on Azure DevOps target).

## Steps

1. Install Git-TFS (using Chocolatey if available) using run `choco install gittfs`
2. Add Git-TFS path to your system PATH environment variable.`set PATH=%PATH%;%cd%\GitTfs\bin\Debug`
3. Clone the entire TFVC repository using the `git tfs clone` command (specify URL, project path, etc.).`git tfs clone http://tfs:8080/tfs/DefaultCollection $/some_project`

## Additional Information

- Git-SVN is a similar tool for migrating Subversion repositories to Git.
- Refer to the provided documentation for advanced cloning use cases: `cd some_project` & `git log`

# GitHub Codespaces
Codespaces by GitHub offers a cloud-based development environment accessible from any device. It solves issues of outdated machines, developer mobility, and IP security concerns by providing a standardized VS Code experience in the cloud.

