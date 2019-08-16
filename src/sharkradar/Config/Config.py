"""
config for the project
"""
import sys
from os.path import dirname as opd, realpath as opr
import os

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

class Config:
	""" Config class for the whole project"""

	DB_PATH = ""
	ALGORITHM = ""

	@staticmethod
	def getDbPath():
		"""
			Getter for Dbpath
		"""
		return Config.DB_PATH

	@staticmethod
	def setDbPath(db_path=os.path.join(basedir,"sharkradar/Util")):
		"""
			Setter for Dbpath
		"""
		Config.DB_PATH = os.path.join(db_path, "sharkradar_service.db")

	@staticmethod
	def getAlgorithm():
		"""
			Getter for algorithm
		"""
		return Config.ALGORITHM

	@staticmethod
	def setAlgorithm(algorithm="wpmc"):
		"""
			Setter for algorithm
			====================
			List of algorithms : 
			1. wpmc = Weighted Priority on Memory Usage and CPU usage
			2. wprs = Weighted Priority on Success Rate and Req Active Ratio
		"""
		Config.ALGORITHM = algorithm