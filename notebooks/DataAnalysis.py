from notebooks.Database import Database
from notebooks.Utilities import Utilities

import pandas as pd
import plotly.express as px
from copy import copy
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go


class DataAnalysis:
    def __init__(self):
        self.db = Database()
        self.ut = Utilities()