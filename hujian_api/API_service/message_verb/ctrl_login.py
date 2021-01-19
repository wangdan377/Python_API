import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

from message_verb.login import off_reg
from message_verb.login import off_login


if __name__ == "__main__":
    off_reg("testHujian001")
    off_reg("testHujian002")
    off_reg("testHujian003")
    off_reg("testHujian004")
    off_reg("testHujian005")

    off_login("testHujian001")
    off_login("testHujian002")
    off_login("testHujian003")
    off_login("testHujian004")
    off_login("testHujian005")

