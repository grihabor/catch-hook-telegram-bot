import requests
from bs4 import BeautifulSoup
from pprint import pprint


_url = 'https://developer.github.com/v3/activity/events/types/'


def load_github_samples():
    r = requests.get(_url)
    soup = BeautifulSoup(r.content)
    code_samples = soup.find_all('code')

    text_samples = (
        sample.text
        for sample
        in code_samples
    )
    
    prev = text_samples[0]
    for sample in text_samples[1:]:
        if sample.strip().startswith('{'):
            content = json.loads(sample)
            headers = {'': prev}
            yield headers, content
        
        prev = sample
        

def test_github_hooks():
    load_github_samples()
    assert 0
    