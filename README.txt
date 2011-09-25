HOW TO USE
Edit config.py to custom builder settings. Then run from command line: python build.py. 

CONFIG PARAMETERS
html_extentions -- tuple of file extentions that contain html.
js_extentions -- tuple of javascript file extentions.
static_extentions -- tuple of other static extensions (not javascript) that require to be indexed
source_dir -- directory where download source of project
result_dir -- directory where you want to put a working version of the project
get_sources_command -- command to checkout the project source
stop_commands -- commands to stop web servers before saving working copy of the project to *result_dir*
start_commands -- commands to start web servers after saving working copy of the project to *result_dir*
salt_path -- path to a file for initial parameter to rename static files in your project
additional_replaces -- dictionary with paths to files to replace some string to another string (view an example in config.py)


### Thank you for using the product!
### ---
### Sergey Zakharov, sergzach@gmail.com