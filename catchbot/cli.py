import subprocess

import os

import argparse
import logging


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)


def get_parser():

    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description='Catch hook telegram bot')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('start', help='Start the bot')
    return parser


def cli():
    parser = get_parser()
    args = parser.parse_args()

    if args.command == 'start':
        host = os.environ['CATCHBOT_HOST']
        port = int(os.environ['CATCHBOT_PORT'])

        subprocess.run([
            'gunicorn',
            '-w', '1',
            '-b', '{}:{}'.format(host, port),
            'catchbot:app',
        ])


if __name__ == '__main__':
    cli()
