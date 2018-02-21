
def get_dynamic_msg_content(mapping, static_content, loaders):
    result = {}

    for key, value in mapping.items():
        if not isinstance(value, str):
            result[key] = get_dynamic_msg_content(value, static_content, loaders)
            continue

        loader = loaders[value]
        x = loader(static_content)
        result[key] = x

    return result
