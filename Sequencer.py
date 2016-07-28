# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:05:43 2016

@author: avieux
"""

def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func 