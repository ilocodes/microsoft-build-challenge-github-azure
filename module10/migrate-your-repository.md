# Migrating to GitHub

## Planning Considerations

The most important consideration before executing your migration to GitHub is whether you need to retain anything beyond the current state of your source. If you're satisfied with starting a new project with just your current source as-is, your best option is to treat it like a new project and upload the source to your repository.

However, if you want to retain version-control history, you'll need to import using the GitHub Migrator tool. For more information about the import support for different version-control platforms, check out [Importing data from third-party version control systems](https://docs.github.com/en/github/importing-your-projects-to-github/importing-source-code-to-github).

Beyond Git data, you might also want to retain issues, pull requests, or other data. Support for these items varies by platform, and is generally available from community projects. This module doesn't cover migrating non-Git data.

## Handling Binary Files Currently Stored in Your Project

As a best practice, GitHub repositories should be limited to the files necessary for building projects. Avoid committing large binary files such as build artifacts. Binary files like spreadsheets and presentations are better suited to be tracked on portals that understand how to serve and version them properly. If you need to version large binary files, consider using the Git LFS (Large File Storage) Git extension.

## Creating Important Git Files Like .gitignore

Git supports .gitignore files to help enforce version-control file policies. These files define the search patterns used to exclude files and folders from source-control tracking. The following simple example recursively excludes any folders called Bin or bin, as well as their contents, from source-control tracking:

`[Bb]in/`
