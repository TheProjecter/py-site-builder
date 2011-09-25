from sitebuilder import SiteBuilder
from config import config

if __name__ == "__main__":
	sB = SiteBuilder( **config )
	sB.build()