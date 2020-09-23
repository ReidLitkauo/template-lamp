# junk.coffee
# General junk drawer

################################################################################
# xcall
# Call a function the easy way! Type doesn't matter

window.xcall = (f, ...argv) ->

	# If passed a function... just call it.
	# Pass the function as its own "this" context.
	if typeof(f) == 'function'
		return f.apply f, argv

	# Passed a string representing a function
	if typeof(f) == 'string'

		# If the function exists globally, call it (same method as above)
		if window[f]
			return window[f].apply window[f], argv

	# If we made it here, either we couldn't find the function, or we were
	# passed a nonsensical value.
	return

################################################################################
# sleep
# Non-blocking waiting function
# await sleep 1000

window.sleep = (ms) ->
  new Promise (resolve) ->
    window.setTimeout resolve, ms
