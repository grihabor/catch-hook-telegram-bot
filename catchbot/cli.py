from .catchbot import CatchBot
import argparse
import logging


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
        start()


def start():
    CatchBot.from_env().start()


