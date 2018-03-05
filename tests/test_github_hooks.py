import requests

def test_github_hooks():
    r = requests.get(_url)
    
    print(r.content)
    assert 0