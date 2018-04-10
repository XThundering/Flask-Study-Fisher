"""
 Created by XThundering on 2018/4/9
"""
from . import web

__author__ = 'XThundering'


@web.route('/my/gifts')
def my_gifts():
    pass


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
