# remove-class-matching.coffee
# Tiny JQuery plugin to remove all classes matching regex

$.fn.removeClassMatching = (p) ->

	this.removeClass (a,b) ->
		b.split ' '
			.filter (val) -> p.test val
			.join ' '

	# For chaining
	this
