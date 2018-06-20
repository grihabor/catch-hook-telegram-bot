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
	

@pytest.mark.parametrize('message,hook_tree', [
    ("HookTree must provide a 'types' attribute", {}),
    ("HookTree must provide a 'hook' attribute", {"types": []}),
    ("HookTree must provide a 'types' attribute", {"hook": {}}),
    ('', {"hook": {"repository": "project"}, "types": []}),
])
def test_hook_tree_validate_errors(message, hook_tree):
    import catchbot.hook.tree
    from catchbot.hook.tree import HookTreeError

    with pytest.raises(HookTreeError) as excinfo:
        catchbot.hook.tree.validate(hook_tree)
   
    assert message in str(excinfo.value)
	