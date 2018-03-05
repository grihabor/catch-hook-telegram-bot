import requests
from bs4 import BeautifulSoup


_url = 'https://developer.github.com/v3/activity/events/types/'


def test_github_hooks():
    r = requests.get(_url)
    soup = BeautifulSoup(r.content)
    code_samples = soup.find_all('code')

    print(code_samples)
    assert 0
    