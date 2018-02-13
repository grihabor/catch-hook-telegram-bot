import argparse


def main():
    parser = argparse.ArgumentParser(description='Catch hook telegram bot')
    subparsers = parser.add_subparsers()

    subparsers.add_subparsers('start', help='Start the bot')
    subparsers.add_subparsers('stop', help='Stop the bot')


if __name__ == '__main__':
    main()
