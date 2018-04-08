"""
 Created by XThundering on 2018/4/4
"""
from flask import Blueprint

__author__ = 'XThundering'

web = Blueprint('web', __name__)

from app.web import book
from app.web import user
