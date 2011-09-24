import os
import re
from hashlib import md5

def dir_entries( **params ):

    dir_name = params[ 'dir_name' ]
    recursive = params[ 'recursive' ] if 'recursive' in params else False
    extentions = params[ 'extentions' ] if 'extentions' in params else ""


    fileList = []
    for file in os.listdir(dir_name):
        dirfile = os.path.join(dir_name, file)
        if os.path.isfile(dirfile):
            if not extentions:
                fileList.append(dirfile)
            else:
                if os.path.splitext(dirfile)[1][1:] in extentions:
                    fileList.append(dirfile)
        # recursively access file names in subdirectories
        elif os.path.isdir(dirfile) and recursive:
            fileList.extend(dir_entries( dir_name = dirfile, recursive = True, extentions = extentions ))
    return fileList

class Replacer:
	@staticmethod
	def md5_replace_in_file( path, extentions, salt ):
		"""
			Path to file, tuple of extentions, initial salt for md5		
		"""
		result = []
		output = ""

		replacements = {}

		with open( path, 'r' ) as f:
			while True:
				line  = f.readline()
				if line == "":
					break			

				for extention in extentions:

					search_result = re.search( "/*([/0-9\w]*/)*(\w[0-9\w]*)\." + extention, line )
				
					if search_result != None:

						matches = search_result.groups()
	
						filepath = matches[ 0 ]

						if filepath == None:
							filepath = ""
						filename = matches[ 1 ]

						m = md5()

						m.update( filepath )
						m.update( filename )					
						m.update( str( salt ) )
					
						replacement = m.hexdigest()

						filename += '.' + extention
						replacement += '.' + extention

						line = line.replace( filename, replacement )

						replacements.update( { filepath + filename: filepath + replacement } )

						break


				output += line

		with open( path, 'w' ) as f:
			f.write( output )

		return replacements

if __name__ == "__main__":
	print repr( Replacer.md5_replace_in_file( "C:/Users/Serg/Desktop/all/temp/html/index.html", ( "js", "css", ), 23 ) )
	
