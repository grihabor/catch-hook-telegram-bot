_structure = {
    'repository': 'repository.name',
    'event': '_event',
    'compare': 'compare',
    'status_icon': '_status',
}


def _filter_step(json_obj):
    pass


def _get_value_by_path(json_obj, path):
    value = json_obj
    for path_key in path.split('.'):
        value = value[path_key]
    return value


def filter_important_data_for_user(json_obj):
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
    