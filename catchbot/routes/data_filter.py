from catchbot import load_mapping


_structure = {
    'repository': 'repository.name',
    'compare': 'compare',
    'status_icon': '_status',
    'event': 'event',
    'host': 'host',
    'branch': 'ref',
    'branch_url': 'repository.web_url'
}


OK = '✅'
FAIL = '❌'


def _get_status(json_obj):
    if json_obj['event'] in ['push', 'pull_request']:
        return OK
    
    return FAIL


def _filter_step(json_obj):
    pass


def _get_value_by_path(json_obj, path):
    value = json_obj
    for path_key in path.split('.'):
        value = value[path_key]
    return value


def _fill_msg_content(mapping, json_obj):
    result = {}
    for key, obj in mapping.items():
        if not isinstance(obj, str):
            result[key] = _fill_msg_content(obj, json_obj)
        
        path = obj

        value = None
        try:
            value = _get_value_by_path(json_obj, path)
        except KeyError:
            value = '!' + path
        finally:
            result[key] = value
    
    return result


def filter_important_data_for_user(json_obj):
    msg_content = {}
    mapping = load_mapping()
    host = json_obj['host']
    content = _fill_msg_content(
        mapping['hosts'][host]['static'],
        json_obj,
    )
    
    content.update(_get_dynamic_content(
        mapping['dynamic']
    ))
    
    return content
    
    