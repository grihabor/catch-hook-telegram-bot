_structure = {
    'repository': 'repository.name',
    'event': '_event',
}


OK = '✅'
FAIL = '❌'


def _filter_step(json_obj):
    pass


def _get_value_by_path(json_obj, path):
    value = json_obj
    for path_key in path.split('.'):
        value = value[path_key]
    return value


def _filter_important_data_for_user(json_obj):
    result = {}

    for key, path in _structure.items():
        if not isinstance(path, str):
            continue

        value = None
        try:
            value = _get_value_by_path(json_obj, path)
        except KeyError:
            value = '!' + path
        finally:
            result[key] = value

    return result


def _construct_message(json_obj):
    return '\n'.join([
        json_obj['repository'],
        json_obj['event'],
    ])
    

def create_message_list_for_user(json_obj, limit=4096):
    msg = _construct_message(
        _filter_important_data_for_user(
            json_obj
        )
    )
    return [
        msg
        if len(msg) < limit
        else msg[:limit]
    ]
