"""Git is a wrapper for parse config and GitHub API

"""

import re
import requests

__author__ = "at15"


class Repo:
    def __init__(self):
        self.path = ""


class GitHubClient:
    def __init__(self):
        self.private_token = ""
        self.base_url = "https://api.github.com"

    def issue_url(self, owner, project):
        return "{}/repos/{}/{}/issues".format(self.base_url, owner, project)

    def fetch_issues(self, issue_url):
        # TODO: page
        # TODO: error handling, like network problem
        res = requests.get(issue_url)
        issues = res.json()
        # TODO: handle project with tons of issues
        # Link:<https://api.github.com/repositories/13124802/issues?page=2>; rel="next",
        # <https://api.github.com/repositories/13124802/issues?page=13>; rel="last"
        simplified_issues = []
        for issue in issues:
            simplified_issues.append({
                "title": issue['title'],
                "number": str(issue['number'])
            })
        return simplified_issues

def parse_config(file_path):
    try:
        f = open(file_path, "r")
        content = f.read()
        f.close()
    except FileNotFoundError:
        raise ValueError("invalid git config file path, can't read file")
    # TODO: handle multiple remote
    # TODO: support other than github
    # TODO: fail gracefully when it is not github
    lines = content.split("\n")
    remote_url = ""
    for i in range(len(lines)):
        if lines[i] == '[remote "origin"]':
            remote_url = lines[i + 1]
            break
    if remote_url == "":
        raise ValueError("invalid git config file, can't find origin")
    # git@github.com:jaxbot/github-issues.vim.git
    # https://github.com/jaxbot/github-issues.vim.git
    # NOTE: use [:/] to support both https and ssh
    pattern = re.compile(".*github.com[:/](.*)/(.*).git")
    r = pattern.match(remote_url)
    owner, project = r.groups()
    return {"owner": owner, "project": project}
