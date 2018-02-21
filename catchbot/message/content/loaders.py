from furl import furl

OK = '✅'
FAIL = '❌'
OPEN = '🆕'


def get_loaders():
    arr = [
        get_status_icon,
        get_status_text,
        get_branch_url,
        get_branch_name,
        get_gitlab_create_merge_request_url,
    ]
    return {
        x.__name__: x
        for x
        in arr
    }


_ok_response = [
    'push',
    'build',
    'wiki_page',
    'note',
    'tag_push',
]


def get_status_icon(content):
    if content['event'] in _ok_response:
        return OK

    if content['event'] == 'pipeline' and content['status']['text'] == 'success':
        return OK

    if any([content['event'] == 'merge_request' and content['merge']['action'] == 'open',
            content['event'] == 'issue' and content['issue']['action'] == 'open']):
        return OPEN

    return FAIL


def get_branch_name(content):
    return content['ref']


def get_branch_url(content):
    return content['ref']


def get_status_text(content):
    return content['action']


def get_gitlab_create_merge_request_url(content):
    url = content['repository']['url']
    new_mr_url = '/'.join([url, 'merge_requests', 'new'])

    result = furl(new_mr_url)

    result.args = {
        'utf8': '✓',
        'merge_request[source_project_id]': content['merge']['source']['repository_id'],
        'merge_request[source_branch]': content['merge']['source']['branch'],
        'merge_request[target_project_id]': content['merge']['target']['repository_id'],
        'merge_request[target_branch]': content['merge']['target']['branch'],
    }

    return result
