from pkg_resources import resource_stream
import yaml
import pytest


def test_hook_yaml():
    import catchbot

    with resource_stream(catchbot.__name__, 'etc/hook.yaml') as f:
        assert yaml.load(f)


def test_hook_tree_load():
	from catchbot import hook
	
	assert hook.tree.load()
	

@pytest.mark.parametrize('hook_tree', [])
def test_hook_tree_validate_errors(hook_tree):
	from catchbot import hook
	
	with pytest.raises(hook.tree.HookTreeError):
		hook.tree.validate(hook_tree)
	