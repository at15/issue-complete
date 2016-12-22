import unittest
import os
import git

class TestGit(unittest.TestCase):
    def test_parse_config(self):
        config_file = os.path.dirname(os.path.realpath(__file__)) + "/config"
        repo = git.parse_config(config_file)
        self.assertEqual("at15", repo["owner"])

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
