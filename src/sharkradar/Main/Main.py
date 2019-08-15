"""
Main functions for the project
"""
from termcolor import cprint
from pyfiglet import figlet_format
import sys
from os.path import dirname as opd, realpath as opr
import os
from waitress import serve
import click
import colorama
colorama.init(strip=not sys.stdout.isatty())

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkradar.Controller.Controller import app

@click.command()
@click.option(
    '--addr',
    default="127.0.0.1",
    help="IP address on which sharkradar will be served",
    show_default=True)
@click.option(
    '--port',
    default=16461,
    help="Port number on which sharkradar will be served",
    show_default=True)
def main(addr, port):
    """
            Sharkradar - Command Line Interface (CLI) utility
            ===================================================

            Sharkradar is a lightweight service registry and discovery tool,
            developed keeping in mind the idea of compatibility with any
            HTTP microservice (service framework independent)
    """
    cprint(figlet_format('SHARKRADAR', font='slant'), 'blue', attrs=['bold'])
    try:
        serve(app, listen=addr + ":" + str(port))
    except Exception as e:
        click.echo(
            "Exception occurred while starting sharkradar\nRun 'sharkradar --help' for help")
        sys.exit(5)


if __name__ == "__main__":
    main()
