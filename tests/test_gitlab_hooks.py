import json

import pytest
import requests
from bs4 import BeautifulSoup

_url = 'https://docs.gitlab.com/ce/user/project/integrations/webhooks.html'


def load_examples():
    r = requests.get(_url)
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


@pytest.mark.parametrize('headers,json_obj', load_examples())
def test_gitlab_hooks(headers, json_obj):
    from catchbot.message import create_message_for_user

    create_message_for_user(headers, json_obj)

