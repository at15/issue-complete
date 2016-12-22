__author__ = 'at15'
import requests
import repo
import vim


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

# parse_issue()

repo.add_to_vim_list('res', repo.list_open_issues('config'))

