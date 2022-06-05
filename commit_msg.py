#!/usr/bin/env python3
import re
import sys


def is_valid(commit_message: str) -> bool:
    pattern = r'(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)' \
              r'{1}(\([\w\-\.]+\))?(!)?: ([\w ])+([\s\S]*)'
    match = re.match(pattern, commit_message)

    if match is None:
        return False

    return True


def main():
    commit_message_data = sys.argv[1]
    commit_message = open(commit_message_data, 'r').read()
    if not is_valid(commit_message):
        error_message = "COMMIT MESSAGE FAILED VALIDATION.\n" \
                        "Specific Reason: does not match Conventional Commit formatting.\n"
        raise SystemExit(error_message)


if __name__ == "__main__":
    main()
