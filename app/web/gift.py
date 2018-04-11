"""
 Created by XThundering on 2018/4/9
"""
from flask_login import login_required

from . import web

__author__ = 'XThundering'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
