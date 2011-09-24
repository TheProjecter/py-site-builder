config = {	'html_extentions': ( "tmpl", ), 
			'js_extentions': ( "js", ), 
			'static_extentions': ( "css", ),
			'source_dir': "/root/dargent/",
			'result_dir': "/www/dargent_root/dargent/",
			'get_sources_command': "svn checkout http://dargent.googlecode.com/svn/trunk/dargent/ /root/dargent/",
			'stop_commands': "/etc/init.d/apache2 stop; /usr/local/nginx/sbin/nginx -s stop",
			'start_commands': "/usr/local/nginx/sbin/nginx; /etc/init.d/apache2 start",
			'salt_path': './salt',
			'additional_replaces':	{
										'settings.py': ( "localhost", "mosdargent.ru" )
									}
		}	


