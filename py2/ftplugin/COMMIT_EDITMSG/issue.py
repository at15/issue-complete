import re
import requests
import json
import os

import vim


class GitRepo:
    config = ""
    user_name = ""
    repo_name = ""
    simplified_issues = []

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
        # print "remote url is " + remote_url
        # TODO: cache and show api process
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
        if not self.get_cached_issues():
            self.get_api_issues()
        return self.simplified_issues

    def get_cached_issues(self):
        self.read_cache()
        return self.simplified_issues

    # TODO: add timeout to avoid network problems
    def get_api_issues(self):
        r = requests.get(self.issue_url())
        issues = r.json()
        simplified_issues = []
        for issue in issues:
            simplified_issues.append({
                'title': issue['title'],
                'number': str(issue['number'])
            })
        # print the issue names
        for s in simplified_issues:
            # TODO: use sprintf
            print '#' + s['number'] + ' ' + s['title']
        self.simplified_issues = simplified_issues
        self.save_cache()

    def read_cache(self):
        try:
            f = open(self.cache_name(), 'r')
            data = f.read()
            self.simplified_issues = json.loads(data)
            return True
        except IOError:
            print 'no cache'
            return False

    def save_cache(self):
        if not os.path.exists(self.cache_folder()):
            os.makedirs(self.cache_folder())
        data = json.dumps(self.simplified_issues)
        f = open(self.cache_name(), 'w')
        f.write(data)
        f.close()

    def cache_folder(self):
        return os.path.dirname(os.path.realpath(__file__)) + '/cache'

    def cache_name(self):
        return self.cache_folder() + '/' + self.user_name + '_s_' + self.repo_name + '.cache'


def add_to_vim_list(list_name, issues):
    for issue in issues:
        vim.eval('add(' + list_name + ', "' + '#' + issue['number'] + ' ' + issue['title'] + '")')


def list_open_issues(config='.git/config'):
    repo = GitRepo(config)
    return repo.get_issues()


def update_issues(config='.git/config'):
    repo = GitRepo(config)
    repo.get_api_issues()