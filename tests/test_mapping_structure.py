import yaml
from pkg_resources import resource_string


def test_mapping_yml():
    path = resource_string('catchbot', 'msg_templates/mapping.yml')
    
    with open(path, 'r') as f:
        assert yaml.load(f)
    