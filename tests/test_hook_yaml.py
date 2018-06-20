from pkg_resources import resource_stream
import yaml
import pytest


def test_hook_yaml():
    import catchbot

    with resource_stream(catchbot.__name__, 'etc/hook.yaml') as f:
        assert yaml.load(f)


def test_hook_tree_load():
    import catchbot.hook.tree
	
	assert catchbot.hook.tree.load()
	

@pytest.mark.parametrize('hook_tree', [])
def test_hook_tree_validate_errors(hook_tree):
	import catchbot.hook.tree
	
	with pytest.raises(hook.tree.HookTreeError):
		catchbot.hook.tree.validate(hook_tree)
	