import sys
from os.path import dirname as opd, realpath as opr
import os
from waitress import serve

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkradar.Controller.Controller import app

CLI_ARG_ERROR_HELP = "***\nCommand argument format : sharkradar --bind=<IP-addr>:<port>\n***"

def main():
	try:
		first_arg = sys.argv[1]
		if first_arg.split("=")[0]!="--bind":
			print(CLI_ARG_ERROR_HELP)
			sys.exit(20)
		listen_arg = first_arg.split("=")[1]
		if len(listen_arg.split(":"))!=2:
			print(CLI_ARG_ERROR_HELP)
			sys.exit(30)
		print("")
		print("Starting Shark-Radar")
		print("Service Registry and Discovery Server")
		print("on {0}".format(listen_arg))
		print("")
		serve(app, listen=listen_arg)
	except Exception as e:
		print(CLI_ARG_ERROR_HELP)

if __name__ == "__main__":
	main()
