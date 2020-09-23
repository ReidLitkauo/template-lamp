# form.coffee
# Generic form handling logic

################################################################################
$ ->

	# Register my custom function as the submit handler!
	$('form').submit submitFormAjax

################################################################################
# submitFormAjax
# Custom submit handler

submitFormAjax = (e) ->

	# === === === === === === === === === === === === === === === === === === ==
	# Initialization

	# First thing's first ... stop normal form submission.
	e.preventDefault()

	# Call user-provided before-submit hook.
	xcall e.target.dataset.hookBeforeSubmit, e

	# Grab form data (to help with submitting images in the future)
	# https://developer.mozilla.org/en-US/docs/Web/API/FormData/Using_FormData_Objects
	formdata = new FormData e.target

	# === === === === === === === === === === === === === === === === === === ==
	# Make the ajax submission

	$.ajax e.target.action, {

		method: e.target.method

		# https://stackoverflow.com/questions/2320069/jquery-ajax-file-upload
		# Don't have JQuery process form data for us, I did this above already
		processData: false
		contentType: false
		data: formdata
		dataType: 'json'

		# User-provided success & error hooks
		success: (data, textstatus, jqxhr) ->
			xcall e.target.dataset.hookSuccess, data, textstatus, jqxhr
		error: (jqxhr, textstatus, error) ->
			xcall e.target.dataset.hookError, jqxhr, textstatus, error

	}

	# === === === === === === === === === === === === === === === === === === ==
	# Cleanup

	false
