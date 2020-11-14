# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd
# Import from our lib
from mlproject.tools import haversine
import pytest


def test_haversine():
    dist = haversine(40, 2, 50, 3)
    assert dist > 1116
    assert dist < 1117
