# coding:utf-8
'''
@author: 猫大白
Project:
'''
import csv
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def users():
    f = open(r"D:\LTTest_Study\Day_6\file\users.csv",encoding='utf-8')
    reader = csv.DictReader(f)
    data = list(reader)
    print(data)
    f.close()
    return data


@pytest.fixture(scope='session')
def csv_data():
    def func(path:str):
        with open(path,encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        return data
    return func

