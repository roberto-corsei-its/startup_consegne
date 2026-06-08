import numpy as np
import pandas as pd
from flask import Blueprint, request, jsonify
import os


REVIEW = os.getenv('REVIEW')


df = pd.read_csv(REVIEW)



def inserimento_recensione(data):
