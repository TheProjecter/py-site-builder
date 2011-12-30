configs = 
{
	'dargent-ru':	{	'html_extentions': ( "html", ), 
						'js_extentions': ( "js", ), 
						'static_extentions': ( "css", ),
						'source_dir': "/root/dargent/",
						'result_dir': "/www/dargent_root/dargent/",
						'get_sources_command': "svn checkout http://dargent-ru.googlecode.com/svn/trunk/dargent/ /root/dargent/",
						'stop_commands': "/etc/init.d/apache2 stop;",
						'start_commands': "chown -R www-data /www/dargent_root/dargent/static/user/; /usr/local/nginx/sbin/nginx -s reload; /etc/init.d/apache2 start",
						'salt_path': './salt',
						'additional_replaces':	{
													'settings.py': ( "localhost", "mosdargent.ru" )
												}
					}
}						


