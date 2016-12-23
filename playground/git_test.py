import unittest
import os
import git


class TestGit(unittest.TestCase):
    def test_parse_config(self):
        config_file = os.path.dirname(os.path.realpath(__file__)) + "/config"
        repo = git.parse_config(config_file)
        self.assertEqual("at15", repo["owner"])
        with self.assertRaises(ValueError):
            git.parse_config("some where only we know")

    def test_issue_url(self):
        github_client = git.GitHubClient()
        self.assertEqual("https://api.github.com/repos/at15/assets-bower-ci/issues",
                         github_client.issue_url("at15", "assets-bower-ci"))

    def test_fetch_issues(self):
        github_client = git.GitHubClient()
        print(github_client.fetch_issues(github_client.issue_url("dyweb", "Ayi")))



if __name__ == '__main__':
    unittest.main()
