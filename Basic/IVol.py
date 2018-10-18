#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:26:06 2018

@author: songqsh
"""


from scipy import optimize
import BsmOption as BO

def IVol(Option, MarketPrice):
    """
    Inputs:
    =======    
        Option: BO.BsmEuOptions class
        MarketPrice: float, price quoted from market
    Outputs:
    ========
        float,
        Implied volatility
    """
    InitVol = .3
    error = lambda vol: (Option.BsmPrice(vol) - MarketPrice)**2
    opt = optimize.fmin(error, InitVol, disp = False);
    return opt[0]


    
if __name__ == "__main__":
    iOpt = BO.BsmEuOptions(\
                        Spot = 290.68, Strike = 288, Rate = 0.02, \
                        Vol = 0.3, Maturity = 1/12, Type = 'Call'\
                        )
    MarketPrice = 9.23
    print('Implied Volatility is', IVol(iOpt, MarketPrice))