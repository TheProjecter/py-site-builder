
from entries import dir_entries, Replacer
from jstools.jsmin import jsmin
from subprocess import call
from shutil import rmtree, copytree
from os import mkdir, path, rename
from salter import Salter

class SiteBuilder:

	ATTRIBUTES = (	'html_extentions', 
					'js_extentions', 
					'static_extentions',
					'source_dir',
					'result_dir',
					'get_sources_command',
					'stop_commands',
					'start_commands',
					'salt_path',
					)

	def __init__( self, **params ):
		for attr in SiteBuilder.ATTRIBUTES:
			setattr( self, '_' + attr, params[ attr ] )			

	def _is_js_extention( self, path ):
		
		for js_extention in self._js_extentions:
			if path[-len(js_extention):] == js_extention:
				return True		
		return False

	@staticmethod
	def rm( directory ):
		if path.exists( directory ):
			rmtree( directory )		
	
	@staticmethod
	def rm_and_mk( directory ):
		SiteBuilder.rm( directory )
		mkdir( directory )

	@staticmethod
	def _call( commands ):
		call( commands, shell = True )

	def _get_source_path( self, source ):
		return self._source_dir + source

	def build( self ):

		SiteBuilder.rm_and_mk( self._source_dir )
		self._call( "{0}".format(	self._get_sources_command	) )
		html_files_paths = dir_entries( dir_name = self._source_dir, recursive = True, extentions = self._html_extentions )
		extentions = self._js_extentions + self._static_extentions
		replaced_resource_paths = {}
		salter = Salter( self._salt_path )
		for html_file_path in html_files_paths:
			replaced_resource_paths.update( Replacer.md5_replace_in_file( html_file_path, extentions, salter.get() ) )
		for source, result in replaced_resource_paths.iteritems():
			
			source_static_path = self._get_source_path( source )
			result_static_path = self._get_source_path( result )

			if path.exists( source_static_path ):			
				if self._is_js_extention( source ):
					with open( source_static_path, 'r' ) as f:
						source_content = f.read()
					min_source_content = jsmin( source_content )
					with open( source_static_path, 'w' ) as f:
						f.write( min_source_content )
				rename( source_static_path, result_static_path )
			else:
				print "[warning] File not found: {0}".format( source_static_path )

		self._call( self._stop_commands )
		SiteBuilder.rm( self._result_dir )
		copytree( self._source_dir, self._result_dir )

		self._call( self._start_commands )
			
			
		

		
		
		

