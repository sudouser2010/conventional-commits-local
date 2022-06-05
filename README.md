# Conventional-Commits-Local
## Enforces [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) Locally With A Git Hook:
#### Suppose you have a Git repo named `Target` and you want to always enforce Conventional Commits. Follow the install instructions below to setup a Git Hook for the `Target` repo.

## How to install:
    * git clone <url for this repo>
    * cd conventional-commits-local
    * cp commit_msg.py <local path to `Target` Git repo>/hooks/commit-msg
    * chmod +x <local path to `Target` Git repo>/hooks/commit-msg

## How to run tests:
    * pip install pytest
    * pytest test_commit_msg.py

## How to use:
    Just make a commit. When the commit message doesn't pass the Conventional Commit validation, 
    it will fail with an error message. When that happens, modify the commit message 
    so it passes validation and recommit.
