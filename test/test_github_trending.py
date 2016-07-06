import sys
import unittest
try:
    from StringIO import StringIO
except Exception as e:
    from io import StringIO

from githubtrending import trending as githubtrending

from . import data

class TestGithubTrending(unittest.TestCase):

    def test_read_page(self):
        for each in data.READ_PAGE_DATA:
            url = each.get('url')
            expected_status_code = each.get('status_code')
            response, status_code = githubtrending.read_page(url)
            self.assertEqual(status_code, expected_status_code)

    def test_make_etree(self):
        for each in data.READ_PAGE_DATA:
            url = each.get('url')
            expected_status_code = each.get('status_code')
            expected_title = each.get('title').encode('utf8')
            response, status_code = githubtrending.make_etree(url)
            self.assertEqual(status_code, expected_status_code)
            page_title = response.xpath('//title')[0].text.encode('utf8')
            self.assertIn(expected_title, page_title)

    def test_get_trending_repo_names(self):
        tree, status_code = githubtrending.make_etree(data.TRENDING_REPO_URL)
        self.assertEqual(status_code, 200)
        repos = githubtrending.get_trending_repo_names(tree)
        self.assertEqual(data.TRENDING_REPO_COUNT, len(repos))

    def test_get_trending_repo_description(self):
        tree, status_code = githubtrending.make_etree(data.TRENDING_REPO_URL)
        self.assertEqual(status_code, 200)
        repo_desc = githubtrending.get_trending_repo_description(tree)
        self.assertEqual(data.TRENDING_REPO_COUNT, len(repo_desc))

    def test_get_trending_repo_meta(self):
        tree, status_code = githubtrending.make_etree(data.TRENDING_REPO_URL)
        self.assertEqual(status_code, 200)
        repo_meta = githubtrending.get_trending_repo_meta(tree)
        self.assertEqual(data.TRENDING_REPO_COUNT, len(repo_meta))

    def test_get_trending_repo_stars_and_languages(self):
        tree, status_code = githubtrending.make_etree(data.TRENDING_REPO_URL)
        self.assertEqual(status_code, 200)
        repo_meta = githubtrending.get_trending_repo_meta(tree)
        repo_stars_and_langauges = githubtrending.get_trending_repo_stars_and_languages(repo_meta)
        self.assertEqual(data.TRENDING_REPO_COUNT, len(repo_stars_and_langauges))

    def test_get_trending_repos(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        repos = githubtrending.get_trending_repos()
        sys.stdout = sys.__stdout__
        self.assertEqual(data.TRENDING_REPO_COUNT, len(repos))

    def test_get_trending_dev_names(self):
        tree, status_code = githubtrending.make_etree(data.TRENDING_DEV_URL)
        self.assertEqual(status_code, 200)
        repos = githubtrending.get_trending_dev_names(tree)
        self.assertEqual(data.TRENDING_REPO_COUNT, len(repos))

    def test_get_trending_dev_repo_names(self):
        tree, status_code = githubtrending.make_etree(data.TRENDING_DEV_URL)
        self.assertEqual(status_code, 200)
        repos = githubtrending.get_trending_dev_repo_names(tree)
        self.assertEqual(data.TRENDING_REPO_COUNT, len(repos))

    def test_get_trending_dev_repo_desc(self):
        tree, status_code = githubtrending.make_etree(data.TRENDING_DEV_URL)
        self.assertEqual(status_code, 200)
        repos = githubtrending.get_trending_dev_repo_desc(tree)
        self.assertEqual(data.TRENDING_REPO_COUNT, len(repos))

    def test_get_trending_devs(self):
        devs = githubtrending.get_trending_devs()
        self.assertEqual(data.TRENDING_REPO_COUNT, len(devs))

if __name__ == '__main__':
    unittest.main()
