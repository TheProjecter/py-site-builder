from sitebuilder import SiteBuilder
from configs import configs
from sys import argv

if __name__ == "__main__":
	try:
		sB = SiteBuilder( **config[ argv[ 1 ] ] )
	except IndexError:
		print "Usage: python build.py config_key"
		exit()
	sB.build()