# -*- coding: utf-8 -*-
# @Time    : 2018/10/15  10:56
# @Author  : MissA
# @File    : tools.py

"""
读取yaml测试数据
"""

import yaml
import os
import os.path


def parse():
    """
    加载/Params_DS/Param -- yaml测试数据
    :return:
    """
    path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/Params_DS/Param'
    pages = {}
    for root, dirs, files in os.walk(path_ya):
        for name in files:
            watch_file_path = os.path.join(root, name)
            with open(watch_file_path, 'r') as f:
                page = yaml.safe_load(f)
                pages.update(page)
        return pages



class GetPages:
    @staticmethod
    def get_page_list():
        _page_list = {}
        pages = parse()
        for page, value in pages.items():
            parameters = value['parameters']
            # print(parameters)
            data_list = []
            for parameter in parameters:
                data_list.append(parameter)
            _page_list[page] = data_list
        return _page_list


if __name__ == '__main__':
    lists = GetPages.get_page_list()

