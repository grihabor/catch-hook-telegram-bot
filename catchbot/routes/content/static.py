

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

