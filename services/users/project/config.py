# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 21:18:36 2019

@author: tommy
"""

class BaseConfig:
    """Base configure"""
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass

class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass

