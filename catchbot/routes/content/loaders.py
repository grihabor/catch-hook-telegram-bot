
OK = '✅'
FAIL = '❌'


def get_loaders():
    arr = [
        get_status_icon
    ]
    return {
        x.__name__: x
        for x
        in arr
    }


def get_status_icon(json_obj):
    if json_obj['event'] in ['push', 'pull_request']:
        return OK

    return FAIL
