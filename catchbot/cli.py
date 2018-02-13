import sys

from catchbot import CatchBot
import argparse
import logging


def get_parser():

    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description='Catch hook telegram bot')
    subparsers = parser.add_subparsers()

    subparsers.add_parser('start', help='Start the bot', dest='start')
    return parser


def cli():
    parser = get_parser()
    parser.parse_args(sys.argv)

    if parser.start:
        start()


def start():
    CatchBot.from_env().start()


