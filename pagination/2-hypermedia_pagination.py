#!/usr/bin/env python3
'''0. Simple helper function'''

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''Write a function index_range takes twoarguments page and page_size.
    '''
    res = ((page * page_size) - page_size)
    resp = res + page_size
    r = (res, resp)
    return r


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """fun to verify arguments and to assign start and end"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = self.dataset()
        start, end = index_range(page, page_size)
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """fun to define vraiable"""
        data: int = self.get_page(page, page_size)
        total_page: int = math.ceil(len(self.__dataset) / page_size)

        if (page + 1) > total_page:
            next_page = None
        else:
            next_page: int = page + 1

        if (page - 1) < 1:
            prev_page = None
        else:
            prev_page: int = page - 1

        result = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_page": total_page}
        return result
