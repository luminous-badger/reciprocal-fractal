#!/usr/bin/python3

# Plot 'brot using PIL / Pillow. Plots x,y, not y,x as does pylab.
# JM Mon  5 Jan 2015 15:11:32 GMT
# For 1, L, and I images, use integers. For RGB images, use a 3-tuple containing integer values. 
# For F images, use integer or floating point values.
# Plot of set for Z^2 + 1/(z ):
# Doesn't work as get Div by zero error.
# JM Tue 17 Oct 2017 14:32:56 BST
# Cured div 0 error by setting Z to 0.001. if (Z): wasn't working as Z was Z=(0,0).
# Still getting maxiter colour. 1/Z very large ?
# JM Thu  8 Nov 2018 15:46:56 GMT
# 1/Z is indeed larger. Try 0.001/Z 
# Making numnerator larger gives smaller size image.
# JM Thu  8 Nov 2018 16:19:02 GMT
# Zoom in to RHS.

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list
import sys

start = timer()

X_MIN = -1.16
X_MAX = -0.91
Y_MIN = -0.1
Y_MAX =  0.1
offset     = 0.001
maxiter    = 950
calc_count = 0
rnum       = 93
lenlc      = len( colour_list )
Znumerator = 0.0024

# create a new X*Y pixel image surface
# make the background white (default bg=black)
X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1

X_SIZE = int( X_SIZE )
Y_SIZE = int( Y_SIZE )

print ( 'X: ', X_SIZE ,' Y: ', Y_SIZE  )
if ( len( sys.argv ) == 2 ):
        sys.exit()


white      = (255,255,255)
randcolour = ( 255, 255, 230 )
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

mycolour = ( 100, 150, 200 ) 
x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( 0.001, 0.0 )
		C = complex ( X, Y )
		iter_count = 0

		while ( abs ( Z**2 ) < 4 and iter_count < maxiter ):
			
			#Z = Z**2 + C
			Z = Z**2 + ( Znumerator / Z ) + C
			#print( Z, C, '   ', iter_count, abs ( Z**2 ) )
			iter_count = iter_count + 1
		
			calc_count = calc_count + 1  
		#mycolour = ( 13 * iter_count, 23 * iter_count, 33 * iter_count ) 
		if ( iter_count + rnum  >= lenlc ):
			mycolour = colour_list[ iter_count % lenlc ]
		else:   
			mycolour = colour_list[ iter_count + rnum  ]
		if ( iter_count <= 2 ):
			img.putpixel( ( x_pixel,  y_pixel ), white )
		elif ( iter_count == maxiter ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

MsgText = 'Brot for Z^2 + ' + str( Znumerator ) + '/Z'
fname = 'Zm_RHS_Recip_Brot_' + str( Znumerator ) + '.png'
draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/usr/share/fonts/truetype/ubuntu/UbuntuMono-B.ttf", 12 )
draw.text( ( 0, 0 ),  MsgText, ( 139,0,0 ), font=font )

print ( MsgText )
print ( 'Fname:', fname )
print ( 'X_MIN: ', X_MIN, 'X_MAX: ', X_MAX  )
print ( 'Y_MIN: ', Y_MIN, 'Y_MAX: ', Y_MAX  )
print ( 'Test Iter and Rand:', rnum, 'created in %f s' % dt )
print ( 'Calc: ', calc_count )
img.show()
#img.save( fname )

