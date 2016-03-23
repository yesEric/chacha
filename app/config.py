# -*- coding:utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.163.com' # mail server，should be replaced in the future.
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'rebot@chacha114.com'
    MAIL_PASSWORD ='aBc123456'
    FLASKY_MAIL_SUBJECT_PREFIX = u'[查查网]'
    FLASKY_MAIL_SENDER = u'查查网管理员 <rebot@chacha114.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or 'Admin'
    FLASKY_NUMBER_PER_PAGE=20

    @staticmethod
    def init_app(app):
        pass

u"""
用于开发环境的配置
"""
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

u"""
用于测试环境的配置
"""
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

u"""
用于测试环境的配置
"""
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig # 确实使用了开发环境配置
}
