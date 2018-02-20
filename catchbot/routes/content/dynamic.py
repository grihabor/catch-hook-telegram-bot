from .loaders import get_loaders


def get_dynamic_msg_content(mapping, static_content):
    result = {}

    for key, value in mapping.items():
        if not isinstance(value, str):
            result[key] = get_dynamic_msg_content(value, static_content)
            continue

        result[key] = get_loaders()[value]

    return result
