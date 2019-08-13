import sys
from os.path import dirname as opd, realpath as opr
import os
from waitress import serve

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkradar.Controller.Controller import app

def main():
	try:
		first_arg = sys.argv[1]
		if first_arg.split("=")[0]!="--bind":
			print("Command argument format : --bind=<IP-addr>:<port>")
			sys.exit(20)
		listen_arg = first_arg.split("=")[1]
		if len(listen_arg.split(":"))!=2:
			print("Command argument format : --bind=<IP-addr>:<port>")
			sys.exit(30)
		print("")
		print("Starting Shark-Radar")
		print("Service Registry and Discovery Server")
		print("on [{0}] for all IP Addresses".format(listen_arg))
		print("")
		serve(app, listen=listen_arg)
	except Exception as e:
		print("Command argument format : --bind=<IP-addr>:<port>")

if __name__ == "__main__":
	main()
