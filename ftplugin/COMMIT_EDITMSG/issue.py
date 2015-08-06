import vim
import re
import requests


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

    def get_issues(self):
        r = requests.get(self.issue_url())
        issues = r.json()
        simplified_issues = []
        for issue in issues:
            simplified_issues.append({
                'title': issue['title']
            })
        print simplified_issues


def list_all():
    repo = GitRepo('.git/config')
    repo.get_issues()
