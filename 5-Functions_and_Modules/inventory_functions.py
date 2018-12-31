# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 06:23:56 2018

@author: Nick
"""

def Compute_EOQ(annual_demand, order_cost, holding_cost):
    '''
    This function computes the Economic Order Quantity (EOQ) 
    for a specified annual demand, ordering cost, and holding cost.
    
    Arguments:
    annual_demand - a numeric value representing the annual demand
    
    order_cost - a numeric value representing the ordering cost
    
    holding_cost - a numeric value representing the holding cost
    
    Returns:
    EOQ - a numeric value representing the Economic Order Quantity
    
    Dependencies:
    This function depends on the NumPy package
    
    Example:
    
    > Compute_EOQ(1000, 25, 2)
    
    158.11388300841898    
    
    '''
    import numpy as np
    
    EOQ = np.sqrt((2*annual_demand*order_cost)/holding_cost)
    
    return EOQ




def Compute_EOQ_TAC(EOQ, annual_demand, order_cost, holding_cost, unit_cost):
    '''
    This function computes the Total Annual Cost for a specified 
    Economic Order Quantity (EOQ), annual demand, ordering cost, 
    and holding cost.
    
    Arguments:
    EOQ - a numeric value representing the Economic Order Quantity
    
    annual_demand - a numeric value representing the annual demand
    
    order_cost - a numeric value representing the ordering cost
    
    holding_cost - a numeric value representing the holding cost
    
    unit_cost - a numeric value representing the unit cost
    
    Returns:
    TAC - a numeric value representing the Total Annual Cost
    
    Dependencies:
    No dependencies
    
    Example:
    
    > Compute_EOQ(1000, 25, 2)
    
    158.11388300841898   
    
    > Compute_EOQ_TAC(158.11388300841898, 1000, 25, 2, 8)
    
    8316.227766016838
    
    '''
    
    TAC = (annual_demand/EOQ)*order_cost + (EOQ/2)*holding_cost + unit_cost*annual_demand
    
    return TAC
