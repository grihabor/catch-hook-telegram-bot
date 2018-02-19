import yaml


def test_mapping_yml():
    path = 'catchbot/msg_templates/mapping.yml'
    
    with open(path, 'r') as f:
        content = yaml.load(f)
 
    print(content)
    assert 0
    