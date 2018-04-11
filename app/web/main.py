"""
 Created by XThundering on 2018/4/9
"""
from . import web

__author__ = 'XThundering'


@web.route('/')
def index():
    return 'hello'


@web.route('/personal')
def personal_center():
    pass
