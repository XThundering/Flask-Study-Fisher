"""
 Created by XThundering on 2018/4/3
"""

from app import create_app

__author__ = 'XThundering'

app = create_app()

if __name__ == '__main__':
    # 生产环境nginx+uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8081, threaded=True)
