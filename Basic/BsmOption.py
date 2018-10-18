#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:22:51 2018

@author: songqsh
"""

import numpy as np
import scipy.stats as ss


class BsmEuOptions:
    def __init__(self, Type = 'Call', 
                 Strike = 100., 
                 Maturity = 1., 
                 Spot = 100., 
                 Vol = 0.1, 
                 Rate = 0.02,
                 #MarketPrice = 10.
                ):
        '''

        Initialize Black-Scholes-Merton European option parameters
        ==========
        Type: 'Call' or 'Put'
        Strike: float
                strike price
        Maturity: float
                Time to maturity in year
        Spot: float
                Initial Stock price
        Vol: float
            Volatility
        Rate: float
            interest rate
        Market Price: float
            Present option price quoted by market
        '''             
        
        self.Type = Type
        self. Strike = Strike
        self.Maturity = Maturity
        self.Spot = Spot
        self.Vol = Vol
        self.Rate = Rate





    '''
    Payoff function
    
    '''        
    def Payoff(self, ST):
        '''
           ================
           Inputs:
               ST: float
               Exercise stock price
               
               Returns:
                   float, 
                   Payoff value
           ================
        '''
        if self.Type == 'Call':
            return np.max([0, ST - self.Strike])
        else:
            return np.max([0, - ST + self.Strike])

    '''    
    Calculation of option price by BSM formula
    ===============
    Inputs:
        Vol: optional, float, by default is 100
            Volatility override
    Returns:
        float,
        BSM price, if Vol is given with a float less than 1, then 
        that Volatility will be used for computation
    '''
    def BsmPrice(self, Vol=100):
        if Vol >1:
            Vol = self.Vol

        d1 = (np.log(self.Spot / self.Strike) + \
              (self.Rate + 0.5 * Vol ** 2) * \
              self.Maturity) / (Vol * np.sqrt(self.Maturity))
        d2 = d1 - Vol * np.sqrt(self.Maturity)
        call_value = self.Spot * ss.norm.cdf(d1) - \
            np.exp(-self.Rate * self.Maturity) * self.Strike * ss.norm.cdf(d2)
        if self.Type == 'Call':
            return call_value
        else:
            return call_value - self.Spot + \
                np.exp(-self.Rate * self.Maturity) * self.Strike
                
  
        
        
        
    
if __name__ == "__main__":
    iOpt = BsmEuOptions(\
                        Spot = 100, Strike = 110, Rate = 0.0475, \
                        Vol = 0.2, Maturity = 1., Type = 'Put'\
                        )
    print('BSM %s option price is %f' %(iOpt.Type, iOpt.BsmPrice()))
    
    