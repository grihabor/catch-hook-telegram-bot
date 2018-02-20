from catchbot import load_mapping
from catchbot.routes.content.loaders import get_loaders

_structure = {
    'repository': 'repository.name',
    'compare': 'compare',
    'status_icon': '_status',
    'event': 'event',
    'host': 'host',
    'branch': 'ref',
    'branch_url': 'repository.web_url'
}




def _get_value_by_path(json_obj, path):
    value = json_obj
    for path_key in path.split('.'):
        value = value[path_key]
    return value


def get_static_msg_content(mapping, json_obj):
    result = {}
    for key, value_obj in mapping.items():
        if not isinstance(value_obj, str):
            result[key] = get_static_msg_content(value_obj, json_obj)

        path = value_obj

        value = None
        try:
            value = _get_value_by_path(json_obj, path)
        except KeyError:
            value = '!' + path
        finally:
            result[key] = value

    return result


def get_dynamic_msg_content(mapping, json_obj):
    result = {}

    for key, value in mapping.items():
        if not isinstance(value, str):
            result[key] = get_dynamic_msg_content(value, json_obj)
            continue

        result[key] = get_loaders()[value]

    return result


def get_message_content_for_user(json_obj, static_mapping, dynamic_mapping):
    content = get_static_msg_content(static_mapping, json_obj)
    content.update(
        get_dynamic_msg_content(dynamic_mapping, json_obj)
    )
    return content
    
    