import json
import requests
import vim


class GitRepo:
    config = ""

    def __init__(self, config_file):
        f = open(config_file, 'r')
        content = f.read()
        self.parse_config(content)
        f.close()

    def parse_config(self, content):
        # Read the config and parse
        # TODO: parse and get the url
        print content

def hi():
    # url = "https://api.github.com/repos/at15/issue-complete/issues"
    # r = requests.get(url)
    #print r.json()
    #print "Hi !"
    repo()


# get the repo of current file
def repo():
    r = GitRepo('.git/config')
    # TODO: prase the text and get github url to get issues