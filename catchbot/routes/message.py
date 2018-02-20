import os
from .content import get_message_content_for_user
from catchbot.config import DIR_TEMPLATES, load_mapping


DEFAULT_PATH = os.path.join(
    DIR_TEMPLATES, 'github', 'push.md'
)
    
    
def _get_template_path(json_obj):
    path = os.path.join(
        DIR_TEMPLATES,
        json_obj['host'],
        '{}.md'.format(json_obj['event']),
    )
    if not os.path.exists(path):
        path = DEFAULT_PATH
    return path
    

def _render_template(json_obj):
    with open(_get_template_path(json_obj), 'r') as f:
        template = f.read()
    
    return template.format(**json_obj)
    

def create_message_for_user(json_obj, limit=4096):

    mapping = load_mapping()
    host = mapping['host']

    msg_content = get_message_content_for_user(
        json_obj,
        static_mapping=mapping['hosts'][host]['static'],
        dynamic_mapping=mapping['dynamic'],
    )

    msg = _render_template(msg_content)
    return (
        msg
        if len(msg) < limit
        else msg[:limit]
    )
