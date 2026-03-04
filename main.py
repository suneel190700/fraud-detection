"""
Real-Time Fraud Detection with Explainable AI
Author: Suneel Kalva
"""

import os
import numpy as np
import pandas as pd
import shap
import joblib
import logging
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
