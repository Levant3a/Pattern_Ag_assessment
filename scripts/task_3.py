"""
Task: First compute the weighted average of horizontal layers for each
component (see formula below). Using your output, then compute the
weighted average of components for each map unit (using comppct).

Horizontal layer weights: abs(hzdept - hzdepb) / hzdepb

Desired data: soil attributes (om, cec, and ph) by mukey.
Please save as a csv file with the
following headers: mukey, mukey_geometry, om, cec, ph.
"""

import pandas as pd
import os
import datetime
