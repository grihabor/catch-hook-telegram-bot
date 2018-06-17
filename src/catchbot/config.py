import os
import yaml
from pkg_resources import resource_string


DIR_TEMPLATES = os.path.abspath(os.path.join(
    os.path.abspath(__file__),
    os.pardir,
    'msg_templates',
))


def load_mapping():
    path = resource_string('catchbot', 'etc/mapping.yml')
    with open(path, 'r') as f:
        return yaml.load(f)
