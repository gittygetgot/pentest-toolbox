import argparse
import subprocess
import sys

def run_subcommand(script, args):
    subprocess.run(["python3", script] + args)

def main():
    parser = argparse.ArgumentParser(description='Pentest toolbox commands')
    subparsers = parser.add_subparsers(dest='command')

    # Define your subcommands
    subparsers.add_parser('com1', help='Run com1 command')
    subparsers.add_parser('com2', help='Run com2 command')
    subparsers.add_parser('com3', help='Run com3 command')

    # Parse only the first argument (the subcommand)
    args, unknown_args = parser.parse_known_args(sys.argv[1:2])
    if args.command:
        # Run the corresponding function with additional arguments
        run_subcommand(args.command + '.py', sys.argv[2:])
    else:
        # No subcommand was provided
        parser.print_help()

if __name__ == "__main__":
    main()
