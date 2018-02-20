import pytest

@pytest.mark.parametrize('mapping,static_content,loaders,expected', [
    ({}, {}, {}, {}),
    ({'branch': 'get_branch'},
     {'ref': 'refs/heads/master'},
     {'get_branch': lambda content: content['ref'].split('/')[-1]},
     {'branch': 'master'}),
])
def test_dynamic_content(mapping, static_content, loaders, expected):
    from catchbot.message.content import get_dynamic_msg_content

    assert expected == get_dynamic_msg_content(mapping, static_content, loaders)
