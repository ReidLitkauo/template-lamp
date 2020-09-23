<? #############################################################################
# /controller.php
# Main controller for ALL site traffic.

################################################################################
# Globally-accessible constants

define('ROOT_DIR', __DIR__);

################################################################################
# Framework include

require_once ROOT_DIR . '/framework/$.php';

################################################################################
# urlconf
# Patterns against which URI requests are tested, are mapped to the endpoints
# those URI requests should be sent to.
# Drop all leading and trailing slashes from test and endpoint.
# As an example, use the following entry:
# '/^posts\/(.*)$/' => 'posts/render',
# The request '/posts/my-post' would match the above,
# and $urlparams would contain 'my-post'.
# Alternatively, just have a plain ol' string without any key,
# and it'll just do a direct string comparison to the request URI.

$urlconf = [

	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Webpages

	# General
	'/^$/' => 'index',
	'phpinfo',

];

################################################################################
# Process the client's request

# Grab/filter the request URI, trimming leading and trailing slashes
# and removing the query string
$request_uri = explode('?', trim($_SERVER['REQUEST_URI'], '/'))[0];

# Test all urlconf options, include the appropriate file
foreach ($urlconf as $urltest => $endpoint) {

	# If the key is a string, then it's a regex to test
	if (is_string($urltest) && preg_match($urltest, $request_uri, $urlparams)) {
		require_once ROOT_DIR . "/endpoints/$endpoint.php";
		exit();
	}

	# If the key is a number, just do an exact match on the endpoint
	if (is_numeric($urltest) && strcmp($request_uri, $endpoint) === 0) {
		require_once ROOT_DIR . "/endpoints/$endpoint.php";
		exit();
	}

}

# No pattern matched, handle 404
http_response_code(404);
exit();
