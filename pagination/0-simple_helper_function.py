#!/usr/bin/env python3
'''0. Simple helper function'''


def index_range(page: int, page_size: int) -> tuple:
    '''Write a function index_range takes twoarguments page and page_size.'''
    res = ((page * page_size) - page_size)
    resp = res + page_size
    r = (res, resp)
    return r
