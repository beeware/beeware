import argparse
import subprocess
import sys

# Examples of valid version strings
# __version__ = '1.2.3.dev1'  # Development release 1
# __version__ = '1.2.3a1'     # Alpha Release 1
# __version__ = '1.2.3b1'     # Beta Release 1
# __version__ = '1.2.3rc1'    # RC Release 1
# __version__ = '1.2.3'       # Final Release
# __version__ = '1.2.3.post1' # Post Release 1

__version__ = '0.1.1'


def new_project():
    cmd = ['cookiecutter', 'https://github.com/pybee/briefcase-template.git']
    print('Creating new BeeWare project using the Briefcase Template...')
    print('>>>', ' '.join(cmd))
    print()
    subprocess.run(cmd)


def build_project(target):
    cmd = ['setup.py', target]
    print('Running Briefcase...')
    print('>>> python', ' '.join(cmd))
    print()
    subprocess.run([sys.executable] + cmd)


def run_project(target):
    cmd = ['setup.py', target, '-s']
    print('Running Briefcase...')
    print('>>> python', ' '.join(cmd))
    print()
    subprocess.run([sys.executable] + cmd)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='sub-command help', dest='command')

    # beeware new
    new_parser = subparsers.add_parser('new')

    # beeware build
    build_parser = subparsers.add_parser('build')
    build_parser.add_argument('target', help='The platform to build')

    # beeware run
    run_parser = subparsers.add_parser('run')
    run_parser.add_argument('target', help='The platform on which to run')

    args = parser.parse_args()

    if args.command == 'new':
        new_project()
    elif args.command == 'build':
        build_project(args.target.lower())
    elif args.command == 'run':
        run_project(args.target.lower())
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
