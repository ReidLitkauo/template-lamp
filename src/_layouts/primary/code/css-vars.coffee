# css-vars.coffee
# Various odds and ends related to setting css variables

$ ->

	# Scrolling

	# Defaults
	document.documentElement.style.setProperty '--js-scroll-x', Math.max window.scrollX / $(window).width(), 0
	document.documentElement.style.setProperty '--js-scroll-y', Math.max window.scrollY / $(window).height(), 0

	# Updating
	$(window).scroll (e) ->
		document.documentElement.style.setProperty '--js-scroll-x', Math.max window.scrollX / $(window).width(), 0
		document.documentElement.style.setProperty '--js-scroll-y', Math.max window.scrollY / $(window).height(), 0

	# Aspect ratio

	# Defaults
	document.documentElement.style.setProperty '--js-aspect-ratio', $(window).width() / $(window).height()

	# Updating
	$(window).resize (e) ->
		document.documentElement.style.setProperty '--js-aspect-ratio', $(window).width() / $(window).height()
