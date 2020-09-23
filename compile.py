################################################################################
# /compile.py
# This script will run all the modules under /src through the appropriate
# commands, and distribute the resulting files correctly.

import os
import sys

################################################################################
# Parameters

# Determine what types of files we're compiling
# Compile all of them if mode isn't specified
compile_layout = len(sys.argv) <= 1 or 'l' in sys.argv[1]
compile_style  = len(sys.argv) <= 1 or 's' in sys.argv[1]
compile_code   = len(sys.argv) <= 1 or 'c' in sys.argv[1]

# Source directory
in_dir = 'src'

# Directories for dependencies
dep_html = 'layout'
dep_css  = 'style'
dep_js   = 'code'

# Output directories
out_html = 'endpoints_html'
out_css  = 'public' + os.sep + 'static'
out_js   = 'public' + os.sep + 'static'

################################################################################
# Function to check if compilation should take place
# Return true if source exists... and is newer than destination.
# Also return true if source exists and destination doesn't exist yet.
def should_compile(src, dst, dep_dir = None):

	# Don't compile if source doesn't exist
	if not os.path.exists(src):
		return False

	# Do compile if destination doesn't exist
	if not os.path.exists(dst):
		return True

	# Check dependency folder recursively
	# If we find one dependency that's newer than the destination, then compile
	if dep_dir:
		for fullroot, directories, filenames in os.walk(dep_dir):
			for file in filenames:
				if os.path.getmtime(fullroot + os.sep + file) > os.path.getmtime(dst):
					return True

	# Now check the source against the destination
	return os.path.getmtime(src) > os.path.getmtime(dst)

################################################################################
# Search for compilable files

for fullroot, directories, filenames in os.walk(in_dir):

	# Remove the indir from the beginning of the root
	# This makes it easier to move files around later on
	root = fullroot[len(in_dir):]

	# Compile .pug
	if compile_layout and should_compile(in_dir + root + os.sep + '$.pug', out_html + root + '.php', in_dir + root + os.sep + dep_html):
		print(' ')
		print('======== Compiling: ' + in_dir + root + os.sep + '$.pug -> ' + out_html + root + '.php ========')
		print    ("phug compile-file '" + in_dir + root + os.sep + "$.pug' -o '" + out_html + root + ".php'")
		os.system("phug compile-file '" + in_dir + root + os.sep + "$.pug' -o '" + out_html + root + ".php'")

	# Compile .sass
	if compile_style  and should_compile(in_dir + root + os.sep + '$.sass', out_css + root + '.css', in_dir + root + os.sep + dep_css):
		print(' ')
		print('======== Compiling: ' + in_dir + root + os.sep + '$.sass -> ' + out_css + root + '.css ========')
		print    ("sass --no-source-map --indented --style=compressed --load-path=src --load-path=src/_common --load-path=src/_framework/style '" + in_dir + root + "/$.sass' '" + out_css + root + ".css'")
		os.system("sass --no-source-map --indented --style=compressed --load-path=src --load-path=src/_common --load-path=src/_framework/style '" + in_dir + root + "/$.sass' '" + out_css + root + ".css'")

	# Compile .coffee
	if compile_code   and should_compile(in_dir + root + os.sep + '$.coffee', out_js + root + '.js', in_dir + root + os.sep + dep_js):
		print(' ')
		print('======== Compiling: ' + in_dir + root + os.sep + '$.coffee -> ' + out_js + root + '.js ========')
		print    ("npx webpack --display-error-details --module-bind 'coffee=coffee-loader' --mode 'production' --entry './" + in_dir + root + "/$.coffee' --output '" + out_js + root + ".js'")
		os.system("npx webpack --display-error-details --module-bind 'coffee=coffee-loader' --mode 'production' --entry './" + in_dir + root + "/$.coffee' --output '" + out_js + root + ".js'")

################################################################################
# Hard-coded exceptions

if compile_layout and should_compile(in_dir + '/$-template-bridge.pug', out_html + '/$-template-bridge.php'):
	print('Compiling: ' + in_dir + '/$-template-bridge.pug -> ' + out_html + '/$-template-bridge.php')
	os.system("/home/reid/vendor/bin/phug compile-file '" + in_dir + "/$-template-bridge.pug' -o '" + out_html + "/$-template-bridge.php'")
