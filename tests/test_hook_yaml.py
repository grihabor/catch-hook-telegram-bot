from pkg_resources import resource_stream
import yaml


def test_hook_yaml():
	import catchbot

    with resource_stream(catchbot.__name__, 'etc/hook.yaml') as f:
        obj = yaml.load(f)

