from pkg_resources import resource_stream
import yaml


def test_hook_yaml():
    with resource_stream('catchbot', 'etc/hook.yaml') as f:
        hook_tree = yaml.load(f)

