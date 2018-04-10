"""
 Created by XThundering on 2018/4/4
"""
from flask import Blueprint

__author__ = 'XThundering'

web = Blueprint('web', __name__)

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
