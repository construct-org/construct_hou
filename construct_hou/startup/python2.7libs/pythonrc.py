# -*- coding: utf-8 -*-
from __future__ import absolute_import
import logging

import construct
from construct_hou import callbacks, utils
from construct_ui import resources


_log = logging.getLogger('construct.hou.pythonrc')
construct.init()
resources.init()
ctx = construct.get_context()
host = construct.get_host()

_log.debug('Setting workspace: %s' % ctx.workspace.path)
host.set_workspace(ctx.workspace.path)

_log.debug('Registering callbacks')
callbacks.register()

_log.debug('Creating Construct menu...')
# TODO


if utils.show_file_open_at_startup():
    # TODO: Add abstraction around creating ActionForms
    if ctx.workspace and not host.get_filename():
        action = construct.actions.get('file.open')
        parent = host.get_qt_parent()
        form_cls = construct.show_form(action.identifier)
