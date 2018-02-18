import os
from .data_filter import filter_important_data_for_user
from catchbot.config import DIR_TEMPLATES
    

DEFAULT_PATH = os.path.join(
    DIR_TEMPLATES, 'github', 'push.txt'
)
    
    
def _get_template_path(json_obj):
    path = os.path.join(
        DIR_TEMPLATES,
        json_obj['host'],
        '{}.txt'.format(json_obj['event']),
    )
    if not os.path.exists(path):
        path = DEFAULT_PATH
    return path
    

def _construct_message(json_obj):
    with open(_get_template_path(json_obj), 'r') as f:
        template = f.read()
    
    return template.format(**json_obj)
    

def create_message_for_user(json_obj, limit=4096):
    user_data = filter_important_data_for_user(json_obj)
    msg = _construct_message(user_data)
    return (
        msg
        if len(msg) < limit
        else msg[:limit]
    )
