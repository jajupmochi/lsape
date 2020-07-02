#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:28:42 2020

@author: ljia
"""

def hungarianLSAPE(C, nrows, ncols, rho, varrho, u, v, init_type=1, forb_assign=False):
	"""
  // -----------------------------------------------------------
  // Main function: Hungarian algorithm for LSAPE
  // -----------------------------------------------------------
  /**
   * \brief Compute a solution to the LSAPE (minimal-cost error-correcting bipartite graph matching) with the Hungarian method
   * \param[in] C nrowsxncols edit cost matrix represented as an array if size \p nrows.ncols obtained by concatenating its columns, column \p nrows-1 are the costs of removing the elements of the 1st set, and the row \p ncols-1 represents the costs of inserting an element of the 2nd set
   * \param[in] nrows Number of rows of \p C
   * \param[in] ncols Number of columns of \p C
   * \param[out] rho Array of size \p nrows-1 (must be previously allocated), rho[i]=j indicates that i is assigned to j (substituted by j if j<ncols-1, or removed if j=ncols-1)
   * \param[out] varrho Array of size \p m (must be previously allocated), varrho[j]=i indicates that j is assigned to i (substituted to i if i<nrows-1, or inserted if i=nrows)
   * \param[out] u Array of dual variables associated to the 1st set (rows of \p C), of size \p nrows
   * \param[out] v Array of dual variables associated to the 2nd set (columns of \p C), of size \p ncols
   * \param[in] forb_assign If true, forbidden assignments are marked with negative values in the cost matrix
   * \details A solution to the LSAPE is computed with the primal-dual version of the Hungarian algorithm, as detailed in:
   * \li <em>S. Bougleux and L. Brun, Linear Sum Assignment with Edition, Technical Report, Normandie Univ, GREYC UMR 6072, 2016</em>
   *
   * This version updates dual variables \c u and \c v, and at each iteration, the current matching is augmented by growing only one Hungarian tree until an augmenting path is found. Our implementation uses a Bread-First-like strategy to construct the tree, according to a FIFO strategy to select the next element at each iteration of the growing process.
   *
   * Complexities:
   * \li O(min{n,m}²max{n,m}) in time (worst-case)
   * \li O(nm) in space
   *
   * \remark
   * Template \p DT allows to compute a solution with integer or floating-point values. Note that rounding errors may occur with floating point values when dual variables are updated but this does not affect the overall process.
   */
	"""
	n, m = nrows - 1, ncols - 1
	
	if init_type == 0:
		pass
	
	if forb_assign:
		pass # @todo
	else:
		pass