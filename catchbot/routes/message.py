import os
from .data_filter import filter_important_data_for_user
    
    
def _get_template_path(json_obj):
    return os.path.abspath(os.path.join(
        os.path.abspath(__file__),
        os.pardir,
        'templates',
        'github',
        '{}.txt'.format(json_obj['event']),
    ))
    

def _construct_message(json_obj):
    with open(_get_template_path(json_obj), 'r') as f:
        template = f.read()
    
    return template.format(**json_obj)
    

def create_message_list_for_user(json_obj, limit=4096):
    user_data = filter_important_data_for_user(json_obj)
    msg = _construct_message(user_data)
    
    msg_list = []
    msg_list.append(
        msg
        if len(msg) < limit
        else msg[:limit]
    )
    return msg_list
