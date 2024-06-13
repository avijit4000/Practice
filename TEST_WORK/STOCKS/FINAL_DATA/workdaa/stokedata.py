print("avijit")
# from yahoo_fin.stock_info import *
import pandas as pd
import numpy as np
from datetime import date
import nsepy
nsepy.get_history(symbol="SBI",start=date(2023,04,01),end=date(2024,1,1),series="EQ")

