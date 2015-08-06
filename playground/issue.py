__author__ = 'at15'
import requests

def parse_issue():
    r = requests.get("https://api.github.com/repos/at15/issue-complete/issues")
    issues = r.json()
    # print len(issues)
    simplified_issues = []
    for issue in issues:
        simplified_issues.append({
            'title': issue['title']
        })
    print simplified_issues

parse_issue()