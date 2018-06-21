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
    ("Types restriction is not satisfied, got: {'repository'}", {
        "hook": {"repository": "project"}, 
        "types": [],
    }), ("Types restriction is not satisfied, got: {'project'}", {
        "hook": {"project": [{}, {}]},
        "types": [],
    }), ("Types restriction is not satisfied, got: {'name'}", {
        "hook": {"project": [{"id": "id"}, {"name": "name"}]},
        "types": [],
    }),
])
def test_hook_tree_validate_errors(message, hook_tree):
    import catchbot.hook.tree
    from catchbot.hook.tree import HookTreeError

    with pytest.raises(HookTreeError) as excinfo:
        catchbot.hook.tree.validate(hook_tree)
   
    assert message == str(excinfo.value)


@pytest.mark.parametrize('hook_tree', [
    ({"hook": {}, "types": []}),
])
def test_hook_tree_validate(hook_tree):
    import catchbot.hook.tree
    
    catchbot.hook.tree.validate(hook_tree)
	
	
