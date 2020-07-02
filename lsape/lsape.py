#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:20:53 2020

@author: ljia
"""
from lsape.hungarian_lsape import hungarianLSAPE

# -----------------------------------------------------------
# case with cost matrix of size (n+1)x(m+1)=nrxnc

def lsapeSolver(C, nr, nc, rho, varrho, u, v, lsape_model='ECBP', init_type=1):
	if lsape_model == 'ECBP':
		hungarianLSAPE(C, nr, nc, rho, varrho, u, v, init_type=1)
	elif lsape_model == 'FLWC':
		lsapeFLWC(C, nr, nc, rho, varrho, u, v, init_type=1)
	elif lsape_model == 'EBP':
		lsapeEBP(C, nr, nc, rho, varrho, u, v, init_type=1)
	elif lsape_model == 'FLCC':
		lsapeFLCC(C, nr, nc, rho, varrho, u, v, init_type=1)
	elif lsape_model == 'FBP':
		lsapeFBP(C, nr, nc, rho, varrho, u, v, init_type=1)
	elif lsape_model == 'FBP0':
		lsapeFBP0(C, nr, nc, rho, varrho, u, v, init_type=1)
	elif lsape_model == 'SFBP':
		lsapeSFBP(C, nr, nc, rho, varrho, u, v, init_type=1)
	else:
		raise Exception('LSAPE_MODEL unknown in lsapeSolver(...)')