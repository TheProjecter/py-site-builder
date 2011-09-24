
class Salter:

	def __init__( self, path ):

		try:
			with open( path, 'r' ) as f:
				try:
					self._salt = int( f.readline() )
				except ValueError:
					self._salt = 0
		except IOError:
			self._salt = 0
		self._path = path

	def get( self ):

		result = self._salt
		self._salt += 1	

		return result

	def __del__( self ):		
		with open( self._path, 'w' ) as f:
			f.write( str( self._salt ) )