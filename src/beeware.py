import argparse
import subprocess

# Examples of valid version strings
# __version__ = '1.2.3.dev1'  # Development release 1
# __version__ = '1.2.3a1'     # Alpha Release 1
# __version__ = '1.2.3b1'     # Beta Release 1
# __version__ = '1.2.3rc1'    # RC Release 1
# __version__ = '1.2.3'       # Final Release
# __version__ = '1.2.3.post1' # Post Release 1

__version__ = '0.3.0.dev1'


def new_project():
    cmd = [
        'cookiecutter',
        'https://github.com/beeware/briefcase-template.git',
        '--checkout', 'v0.3'
    ]
    print('Creating new BeeWare project using the Briefcase Template...')
    print('>>>', ' '.join(cmd))
    print()
    subprocess.run(cmd)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='sub-command help', dest='command')

    # beeware new
    subparsers.add_parser('new')

    args = parser.parse_args()

    if args.command == 'new':
        new_project()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
