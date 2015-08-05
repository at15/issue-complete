import json
import requests

def hi():
    url = "https://api.github.com/repos/at15/issue-complete/issues"
    r = requests.get(url)
    print r.json()
    print "Hi !"