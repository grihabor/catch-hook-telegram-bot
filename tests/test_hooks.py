import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pytest
import itertools
import json


_github_url = 'https://developer.github.com/v3/activity/events/types/'
_gitlab_url = 'https://docs.gitlab.com/ce/user/project/integrations/webhooks.html'


def load_github_samples():
    r = requests.get(_github_url)
    soup = BeautifulSoup(r.content)
    code_samples = soup.find_all('code')

    text_samples = [
        sample.text
        for sample
        in code_samples
    ]
    
    prev = text_samples[0]
    for sample in text_samples[1:]:
        if sample.strip().startswith('{'):
            content = json.loads(sample)
            headers = {'X-GitHub-Event': prev}
            yield headers, content
        
        prev = sample
        

def load_gitlab_samples():
    r = requests.get(_gitlab_url)
    soup = BeautifulSoup(r.content)
    code_samples = soup.find_all('code')

    headers = None

    for sample in code_samples:
        code = sample.get_text()
        if code.startswith('X-Gitlab-Event'):
            key, value = code.split(':')
            headers = {key.strip(): value.strip()}
            continue

        try:
            content = json.loads(code)
        except json.decoder.JSONDecodeError:
            continue

        yield (headers, content)


def load_all_samples():
    return itertools.chain(
        load_github_samples(),
        load_gitlab_samples(),
    )


@pytest.mark.parametrize('headers,json_obj', load_all_samples())
def test_hooks(headers, json_obj):
    from catchbot.message import create_message_for_user

    msg = create_message_for_user(headers, json_obj)

    print(msg)
    assert '!' not in msg
    
    
    