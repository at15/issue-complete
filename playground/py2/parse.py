__author__ = 'at15'

import re


def parse():
    f = open('config', 'r')
    content = f.read()
    lines = content.split('\n')
    remote_url = ""
    # loop to find the line with remote origin
    for i in range(len(lines)):
        if lines[i] == '[remote "origin"]':
            remote_url = lines[i + 1]
            break
    print remote_url
    # TODO: support http
    # https://github.com/ParsePlatform/parse-cli.git
    # git@github.com:ParsePlatform/parse-cli.git
    # remote_url = 'git@github.com:ParsePlatform/parse-cli.git'
    pattern = re.compile(r'.*github.com[:/](.*)/(.*).git')
    match = pattern.match(remote_url)
    # print match
    user_name = match.group(1)
    repo_name = match.group(2)
    print user_name
    print repo_name
    # get user and repo from the url


parse()