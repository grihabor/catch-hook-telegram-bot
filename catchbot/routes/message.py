_structure = {
    'repository': 'repository.name',
}


def filter_important_data_for_user(json_obj):
    repo = json_obj['repository']

    return '\n'.join([
        'Name',
        '----',
        repo['name'],
    ])


def create_message_list_for_user(json_obj, limit=4096):
    json_obj = filter_important_data_for_user(json_obj)
    return
