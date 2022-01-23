#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 12:42:59 2022

@author: YouCanCallMeAll
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt 

# define ground shipping weight formula
def ground_shipping(weight):
  price = 0
  flat_charge = 20
  if weight <= 2:
    rate = 1.5
    price += ((weight * rate) + flat_charge)
    return price
  elif ((weight > 2) and (weight <= 6)):
    rate = 3
    price += ((weight * rate) + flat_charge)
    return price
  elif ((weight > 6) and (weight <= 10)):
    rate = 4
    price += ((weight * rate) + flat_charge)
    return price
  elif (weight > 10):
    rate = 4.75
    price += ((weight * rate) + flat_charge)
    return price
  else:
    return price

# define ground shipping premium formula
def premium_ground_shipping(weight):
  price = 0
  flat_charge = 125
  if weight > 0:
    price += flat_charge
    return price
  else:
    return price

# define drone shipping formula
def drone_shipping(weight):
  price = 0
  if weight <= 2:
    rate = 4.5
    price += (weight * rate) 
    return price
  elif ((weight > 2) and (weight <= 6)):
    rate = 9
    price += (weight * rate) 
    return price
  elif ((weight > 6) and (weight <= 10)):
    rate = 12
    price += (weight * rate) 
    return price
  elif (weight > 10):
    rate = 14.25
    price += (weight * rate) 
    return price
  else:
    return price

# define function to select cheapest shipping method
def method_selector():
    weight = input("Welcome to Sal's Shipping. We want to help you find the most affordable shipping option for you. What is the weight of your item in pounds? ")
    weight = int(weight)
    if (ground_shipping(weight) < premium_ground_shipping(weight))\
        and (ground_shipping(weight) < drone_shipping(weight)):
            cheapest_method = 'ground shipping'
            cheapest_price = round(ground_shipping(weight), 2)
    elif (premium_ground_shipping(weight) < ground_shipping(weight))\
        and (premium_ground_shipping(weight) < drone_shipping(weight)):
            cheapest_method = 'premium ground shipping'
            cheapest_price = round(premium_ground_shipping(weight), 2)
    elif (drone_shipping(weight) < ground_shipping(weight))\
        and (drone_shipping(weight) < premium_ground_shipping(weight)):
            cheapest_method = 'drone shipping'
            cheapest_price = round(drone_shipping(weight), 2)
    else:
        print("Error, please enter a valid weight.")
        sys.exit()
    print('The cheapest option for shipping is ' + cheapest_method + \
          ' and your shipping costs come out to $' + str(cheapest_price) + '.')

method_selector()


# %%





