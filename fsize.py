#!/usr/bin/python3

# Zoom in to RHS. Test of auto re-size.
# JM Tue  4 Dec 2018 10:38:20 GMT

import numpy as nm
import cmath
import sys
from timeit import default_timer as timer
from lc import colour_list

start = timer()

X_MIN = -1.09
X_MAX = -1.04
Y_MIN = -0.02
Y_MAX =  0.02
offset     = 0.0001
maxiter    = 1950
rnum       = 93
Znumerator = complex( 0.0025, 0.0 )
lenlc      = len( colour_list )
# Using a complex znum gives a blank output.
# Put the sodding Real part in the right place and it works !!
#Znumerator = 0.0025 

# create a new X*Y pixel image surface
# make the background white (default bg=black)
X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1

X_SIZE = int( X_SIZE )
Y_SIZE = int( Y_SIZE )


def proc_picture( X_MIN, X_MAX, Y_MIN, Y_MAX, new_offset ):
	calc_count = 0
	print( 'Y_MAX:', Y_MAX, ' Y_MIN:', Y_MIN, end='\n' )
	print( 'X_MAX:', X_MAX, ' X_MIN:', X_MIN, end='\n' )
	print( 'NewOff:', new_offset, end='\n' )
	fname = 'tst_Zm_RHS_Recip_Brot_' + str( Znumerator ) + '_' + \
	str( round( X_MIN, 3 ) ) + '_' + str( round( X_MAX, 3 ) ) + '_' + str( round( Y_MIN, 3 ) ) + '_' + str( round( Y_MAX, 3 ) ) + '_' + '.png'
	print(  'Fname:', fname,  end='\n' )
	x_pixel = 0
	for X in nm.arange ( X_MIN, X_MAX, new_offset ):
		y_pixel = 0
		for Y in nm.arange ( Y_MIN, Y_MAX, new_offset ):
			Z = complex ( 0.001, 0.0 )
			C = complex ( X, Y )
			iter_count = 0

			while ( abs ( Z**2 ) < 4 and iter_count < maxiter ):
				
				#Z = Z**2 + C
				Z = Z**2 + ( Znumerator / Z ) + C
				#print( Z, C, ' Abs:  ', abs ( Z**2 ), ' I:', iter_count, end='\n' )
				iter_count = iter_count + 1
			
				calc_count = calc_count + 1  
			y_pixel += 1
			if ( iter_count == maxiter ):
				print( 'x', end=' ' )
			else:	
				print( '.', end=' ' )

		x_pixel += 1
		print( '\n' )
	print(  'Calc: ', calc_count, end='\n'  )
	print( '\n' )



yoffset = 0.001
while ( Y_MAX > 0.017 and Y_MIN < 0.001 ):
	#print 'Y_MAX:', Y_MAX, ' Y_MIN:', Y_MIN,
	#print 'X_MAX:', X_MAX, ' X_MIN:', X_MIN,
	Y_MAX -= yoffset
	Y_MIN += yoffset
	X_MAX -= yoffset
	X_MIN += yoffset
	Y_SIZE = ( Y_MAX - Y_MIN ) / offset
	X_SIZE = ( X_MAX - X_MIN ) / offset
	#print 'X: ', X_SIZE ,' Y: ', Y_SIZE 
	new_offset = ( Y_MAX - Y_MIN ) / 500.0
	#print 'NewOff:', new_offset
	proc_picture( X_MIN, X_MAX, Y_MIN, Y_MAX, new_offset )

dt = timer() - start

print( 'Recip Brot created in {0:.5f}'.format( dt ), 'Secs', end='\n' )

