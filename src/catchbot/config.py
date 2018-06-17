import os
import yaml


DIR_TEMPLATES = os.path.abspath(os.path.join(
    os.path.abspath(__file__),
    os.pardir,
    'msg_templates',
))

PATH_MAPPING = os.path.join(
    DIR_TEMPLATES,
    'mapping.yml',
)


def load_mapping():
    with open(PATH_MAPPING, 'r') as f:
        return yaml.load(f)
        
        
