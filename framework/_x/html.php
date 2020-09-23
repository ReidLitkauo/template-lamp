<? #############################################################################
# /framework/_x/html.php
# Handle all html rendering logic

function render_html($args = []) {

	global $endpoint;

	require_once ROOT_DIR . "/endpoints_html/$endpoint.php";

}
