import argparse
import logging


def cli():

    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description='Catch hook telegram bot')
    subparsers = parser.add_subparsers()

    subparsers.add_parser('start', help='Start the bot')
    subparsers.add_parser('stop', help='Stop the bot')


