# Conventional-Commits-Local
## Enforces Conventional Commits Locally With A Git Hook:
#### Suppose you have a Git repo named `Target` and you want to always enforce Conventional Commits. Follow the install instructions below to setup a Git Hook for the `Target` repo.

## How to install:
    * git clone <url for this repo>
    * cd conventional-commits-local
    * cp commit_msg.py <local path to `Target` Git repo>/hooks/commit-msg
    * chmod +x <local path to `Target` Git repo>/hooks/commit-msg

## How to Run Tests
    * pip install pytest
    * pytest test_commit_msg.py