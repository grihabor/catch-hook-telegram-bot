from pkg_resources import resource_stream
import yaml
import catchbot


def load_structure():
	path = 'etc/hook.yaml'
	with resource_stream(catchbot.__name__, path) as f:
		return yaml.load(f)
		