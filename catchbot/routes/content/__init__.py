from .dynamic import get_dynamic_msg_content
from .static import get_static_msg_content


def get_message_content_for_user(json_obj, static_mapping, dynamic_mapping):
    static_content = get_static_msg_content(static_mapping, json_obj)
    dynamic_content = get_dynamic_msg_content(dynamic_mapping, static_content)

    content = {}
    content.update(static_content)
    content.update(dynamic_content)
    return content

