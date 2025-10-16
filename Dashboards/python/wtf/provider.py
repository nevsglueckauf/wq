# Factory Klasse für Tab-Content
#
# AUTHOR Sven Schrodt
# SINCE 2025-10-15
import pandas as pd

class Provider:
    """ Data Provider for GUI parameters & Foo
    """
    
    proj = ['equirectangular', 'mercator', 'orthographic', 'natural earth', 'kavrayskiy7', 'miller', 'robinson', 'eckert4', 'azimuthal equal area', 'azimuthal equidistant', 'conic equal area', 'conic conformal', 'conic equidistant', 'gnomonic', 'stereographic', 'mollweide', 'hammer', 'transverse mercator', 'albers usa', 'winkel tripel', 'aitoff', 'sinusoidal']
    #brands = pd.read_csv("../../Data/Norm/brandz.csv")
    
    def get_brands(self):
        return pd.read_csv("../../Data/Norm/brandz.csv")
        
