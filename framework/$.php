<? #############################################################################
# framework/$.php
# Entry point for including all private framework files.

################################################################################
# Secret

# This webapp requires access to certain secret information, things like
# passwords, credentials, salts, and private keys. The below file will create
# a publicly-available $secret variable and load all required information as
# key-value pairs:

# Obviously I won't show you this file.

require_once ROOT_DIR . '/secret/$.php';

################################################################################
# First-party

require_once '_x/html.php';

################################################################################
# Third-party
