_header_host_mapping = {
    'X-GitHub-Event': [
        'github',
        lambda x: x,
    ],
    'X-Gitlab-Event': [
        'gitlab',
        lambda x: '_'.join(x.lower().split()[:-1]),
    ],
}

def get_info_from_headers(headers):

    _event = None
    _host = None

    for key, (host, mapping) in _header_host_mapping.items():
        if key not in headers:
            continue
        _event = mapping(headers[key])
        _host = host
        break

    return {'_event': _event, '_host': _host}
