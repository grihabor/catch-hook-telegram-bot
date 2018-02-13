import argparse


def cli():
    parser = argparse.ArgumentParser(description='Catch hook telegram bot')
    subparsers = parser.add_subparsers()

    subparsers.add_parser('start', help='Start the bot')
    subparsers.add_parser('stop', help='Stop the bot')


