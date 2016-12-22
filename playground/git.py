"""Git ???

"""

import re

__author__ = "at15"


class Repo:
    def __init__(self):
        self.path = ""


def parse_config(file_path):
    # TODO: error handling
    f = open(file_path, "r")
    content = f.read()
    f.close()
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
        # TODO: throw proper exception
        return
    # git@github.com:jaxbot/github-issues.vim.git
    # https://github.com/jaxbot/github-issues.vim.git
    # NOTE: use [:/] to support both https and ssh
    pattern = re.compile(".*github.com[:/](.*)/(.*).git")
    r = pattern.match(remote_url)
    owner, project = r.groups()
    return {"owner": owner, "project": project}
