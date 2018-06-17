import os
from setuptools import find_packages, setup


NAME = 'catchbot'
DESCRIPTION = 'Telegram bot to catch your hooks from Github, Gitlab and more'
URL = 'https://github.com/grihabor/catch-hook-telegram-bot'
EMAIL = 'grihabor@gmail.com'
AUTHOR = 'Borodin Gregory'

REQUIRED = [
    'python-telegram-bot',
    'flask',
    'gunicorn',
    'celery',
    'pyyaml',
    'beautifulsoup4',
    'requests',
    'furl',
]


def _get_project_path():
    return os.path.abspath(os.path.join(__file__, os.pardir))


def get_version():
    project_path = _get_project_path()
    init_path = os.path.join(project_path, 'src', NAME, '__init__.py')
    with open(init_path, 'r') as f:
        for line in f:
            if line.startswith('__version__'):
                version_string = line.split('=')[-1].strip()
                return version_string.strip("'")


def get_readme():
    project_path = _get_project_path()
    readme_path = os.path.join(project_path, 'README.rst')
    with open(readme_path, 'r') as f:
        return f.read()


def main():
    setup(
        name=NAME,
        version=get_version(),
        description=DESCRIPTION,
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        package_dir={'': 'src'},
        packages=find_packages('src'),
        install_requires=REQUIRED,
        setup_requires=[
            'pytest-runner',
        ],
        tests_require=[
            'pytest',
            'pytest-cov',
        ],
        include_package_data=True,
        package_data={
            '': ['*.md', '*.md',],
        },
        license='MIT',
        long_description=get_readme(),
        classifiers=[
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
        ],
    )


if __name__ == '__main__':
    main()
