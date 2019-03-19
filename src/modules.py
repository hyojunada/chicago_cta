# modules
from datetime import datetime
import pandas as pandas
import math
import numpy as np
from ast import literal_eval
from geopy.geocoders import Nominatim

def str_to_date(x, str_format='%m/%d/%Y'):
    if type(x) == float:
        return None
    else:
        return datetime.strptime(x, '%m/%d/%Y')



def find_color(row):
    """
    Assign color to each stations
    """
    # color dictionary for each L lines,
    # color of the lines will correspond to the color it will be represented
    color_dict = {'red':'red', 
                'blue':'blue', 
                'g':'green', 
                'brn':'brown', 
                'p':'purple', 
                'pexp':'purple',
                'y': 'gold', 
                'pnk': 'fuchsia',
                'o': 'orange'}
    # get the columns that have color values, True/False
    row_color = row[['red', 'blue', 'g', 'brn', 'p', 'pexp', 'y', 'pnk', 'o']]
    # find the line name, where the color will be 'True'
    line = row_color.index[row_color.values].tolist()
    colors = []
    for l in line:
        colors.append(color_dict[l])
    return colors

def merc(Coords):
    Coordinates = literal_eval(Coords)
    lat = Coordinates[0]
    lon = Coordinates[1]
    
    r_major = 6378137.000
    x = r_major * math.radians(lon)
    scale = x/lon


    y = 180.0/math.pi * math.log(math.tan(math.pi/4.0 + 
        lat * (math.pi/180.0)/2.0)) * scale
    return (
        x, y)


def find_zipcode(x):
    """
    Find zip code using the latitude and longitude locations
    """
    geolocator = Nominatim(user_agent="zipcode")
    location = geolocator.reverse(literal_eval(x))
    return location.raw['address']['postcode']