#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Product class  module '

__author__ = 'haixiang'

class Product(object):
  
  def __init__(self, prodId, model, color, ram):
    self.__prodId = prodId
    self.__model = model
    self.__color = color
    self.__ram = ram

  def __init__(self, line):
    prodInfo = line.split(',')
    self.__prodId = prodInfo[0]
    self.__model = prodInfo[1]
    self.__color = prodInfo[2]
    self.__ram = prodInfo[3]

  def getProdId(self):
    return self.__prodId

  def getModel(self):
    return self.__model

  def getColor(self):
    return self.__color

  def getRam(self):
    return self.__ram

  def printProd(self):
    print("product:%s,%s%s%s" % (self.__prodId, self.__model, self.__color, self.__ram))
