
OK = '✅'
FAIL = '❌'


def get_loaders():
    arr = [
        get_status_icon,
        get_status_text,
        get_branch_url,
        get_branch_name,
    ]
    return {
        x.__name__: x
        for x
        in arr
    }


def get_status_icon(content):
    if content['event'] in ['push', 'pull_request']:
        return OK

    return FAIL


def get_branch_name(content):
    return content['ref']


def get_branch_url(content):
    return content['ref']


def get_status_text(content):
    return content['action']

