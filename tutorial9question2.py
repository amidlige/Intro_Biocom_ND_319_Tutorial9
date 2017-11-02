#Import Packages
import pandas
import numpy
from scipy.optimize import minimize
from scipy.stats import norm
import re
import os
from plotnine import *

data = pandas.read_csv("mMarinumGrowth.csv",header=0,sep='\t')

def Monod(p,obs):
    uMax=p[0]
    K=p[1]
    sigma=p[2]
    
    expected=uMax* (x/(x+K))
    nll=-1+norm(expected,sigma).logpdf(obs.y).sum
    return nll
    
    initialGuess=numpy.array([1,1,1])
    fit-minimize(Monod,initialGuess,method="Monod Equation",options={'disp':True},args=data)

    print(fit.x)


