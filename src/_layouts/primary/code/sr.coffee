# sr.coffee
# A collection of helpful functions for screen readers

window.sr_status = (msg) ->

	$('.sr-only.status').html msg
