#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 17:33:54 2018

@author: Paris
"""

import numpy as np


class BayesianLinearRegression:
  """
    Linear regression model: y = (w.T)*x + \epsilon
    w ~ N(0,beta^(-1)I)
    P(y|x,w) ~ N(y|(w.T)*x,alpha^(-1)I)
  """
  def __init__(self, X, y, alpha = 1.0, beta = 1.0):
      
      self.X = X
      self.y = y
      
      self.alpha = alpha
      self.beta = beta
      

  def fit_MLE(self): 
      xTx_inv = np.linalg.inv(np.matmul(self.X.T,self.X))
      xTy = np.matmul(self.X.T, self.y)
      w_MLE = np.matmul(xTx_inv, xTy)
      
      self.w_MLE = w_MLE
      
      return w_MLE
      
  def fit_MAP(self): 
      Lambda = self.alpha*np.matmul(self.X.T,self.X) + self.beta*np.eye(self.X.shape[1])
      Lambda_inv = np.linalg.inv(Lambda)
      xTy = np.matmul(self.X.T, self.y)
      mu = self.alpha*np.matmul(Lambda_inv, xTy)
      
      self.w_MAP = mu
      self.Lambda_inv = Lambda_inv
      
      return mu, Lambda_inv
      
  def predictive_distribution(self, X_star):
      mean_star = np.matmul(X_star, self.w_MAP)
      var_star = 1.0/self.alpha + np.matmul(X_star, np.matmul(self.Lambda_inv, X_star.T))
      return mean_star, var_star