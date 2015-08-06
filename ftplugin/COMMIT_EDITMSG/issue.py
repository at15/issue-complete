import json
import requests
import vim
import re


class GitRepo:
    config = ""
    user_name = ""
    repo_name = ""

    def __init__(self, config_file):
        f = open(config_file, 'r')
        content = f.read()
        self.parse_config(content)
        f.close()

    def parse_config(self, content):
        # Read the config and parse
        # TODO: parse and get the url
        lines = content.split('\n')
        remote_url = ""
        # loop to find the line with remote origin
        for i in range(len(lines)):
            if lines[i] == '[remote "origin"]':
                remote_url = lines[i + 1]
                break
        print "remote url is " + remote_url
        pattern = re.compile(r'.*github.com[:/](.*)/(.*).git')
        match = pattern.match(remote_url)
        user_name = match.group(1)
        repo_name = match.group(2)
        self.user_name = user_name
        self.repo_name = repo_name

    def issue_url(self):
        # TODO: error handling
        return "https://api.github.com/repos/" + self.user_name + "/" + self.repo_name + "/issues"

def hi():
    # url = "https://api.github.com/repos/at15/issue-complete/issues"
    # r = requests.get(url)
    # print r.json()
    #print "Hi !"
    repo()


# get the repo of current file
def repo():
    r = GitRepo('.git/config')
    # TODO: prase the text and get github url to get issues