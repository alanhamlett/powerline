# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import, print_function)

try:
	import vim
except ImportError:
	vim = object()

from powerline.bindings.vim import vim_func_exists
from powerline.theme import requires_segment_info


@requires_segment_info
def wakatime(pl, segment_info):
	'''Shows today's coding time if WakaTime plugin enabled.
	'''
	if not vim_func_exists('WakaTimeStatusLine'):
		return None
	return vim.eval('WakaTimeStatusLine()')
