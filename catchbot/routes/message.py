_structure = {
    'repository': 'repository.name',
    'event': '_event',
    'compare': 'compare',
    'status_icon': '_status',
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


def _get_status(json_obj):
    if json_obj['event'] in ['push']:
        return OK
    
    return FAIL
    
    
def _get_template_path(json_obj):
    return os.path.join(
        os.path.abspath(__file__),
        os.pardir,
        'template.txt',
    )
    

def _construct_message(json_obj):
    with open('template.txt', 'r') as f:
        template = f.read()
    
    return template.format(**json_obj)
    

def create_message_list_for_user(json_obj, limit=4096):
    json_obj['_status'] = _get_status(json_obj)
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
