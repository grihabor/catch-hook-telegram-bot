import os
from pprint import pprint
from pkg_resources import resource_string

from catchbot.message.header_parser import get_info_from_headers
from .content import get_message_content_for_user
from catchbot.config import DIR_TEMPLATES, load_mapping


DEFAULT_PATH = os.path.join(
    DIR_TEMPLATES, 'default.md'
)
    
    
def _get_template_string(json_obj):
    path = '/'.join([
        'etc',
        json_obj['host'],
        '{}.md'.format(json_obj['event']),
    ])
    if not os.path.exists(path):
        path = 'etc/default.md'
    return resource_string('catchbot', path)
    

def _render_template(json_obj, path):
    with open(path, 'r') as f:
        template = f.read()

    return template.format(**json_obj)
    

def _get_msg_content(headers, json_obj):

    json_obj.update(get_info_from_headers(headers))

    mapping = load_mapping()
    host = json_obj['host']

    return get_message_content_for_user(
        json_obj,
        static_mapping=mapping['hosts'][host]['static'],
        dynamic_mapping=mapping['dynamic'],
    )


def create_message_for_user(headers, json_obj, limit=4096):
    msg_content = _get_msg_content(headers, json_obj)
    template_string = _get_template_string(msg_content)
    msg = _render_template(msg_content, template_string)
    return (
        msg
        if len(msg) < limit
        else msg[:limit]
    )
