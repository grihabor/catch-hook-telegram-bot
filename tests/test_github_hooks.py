import requests
from bs4 import BeautifulSoup
from pprint import pprint


_url = 'https://developer.github.com/v3/activity/events/types/'


def test_github_hooks():
    r = requests.get(_url)
    soup = BeautifulSoup(r.content)
    code_samples = soup.find_all('code')

    pprint([sample.text for sample in code_samples])
    assert 0
    