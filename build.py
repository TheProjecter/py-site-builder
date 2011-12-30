from sitebuilder import SiteBuilder
from config import config
from sys import argv

if __name__ == "__main__":
	sB = SiteBuilder( **config[ argv[ 1 ] ] )
	sB.build()