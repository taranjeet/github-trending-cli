import unittest

from githubtrending import trending as githubtrending

from . import data

class TestGithubTrending(unittest.TestCase):

    def test_read_page(self):
        for each in data.READ_PAGE_DATA:
            url = each.get('url')
            expected_status_code = each.get('status_code')
            response, status_code = githubtrending.read_page(url)
            self.assertEqual(status_code, expected_status_code)


if __name__ == '__main__':
    unittest.main()