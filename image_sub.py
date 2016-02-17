'''
python version of image_decals_dr2.pro
Function Name: image_decals
Purpose: get image sub-data within a radius for DECals.
Input: ra, dec
 fileimage: file name of image, for example: 'decals-0001m002-image-g.fits'
 arcsec: radius in units of arcsec
Output: datanew1: 
History: 
 Created: Dec 30 2015
 Author: Qian Yang, PKU/Steward, qianyang.astro@gmail.com
'''
import numpy as np
import pyfits
def image_decals(ra,dec,fileimage,arcsec):
	parr0 = pyfits.open(fileimage)
	hdr = parr0[0].header
	tabler = parr0[0].data
	cd1_1 = hdr['cd1_1']
	cd1_2 = hdr['cd1_2']
	cd2_1 = hdr['cd2_1']
	cd2_2 = hdr['cd2_2']
	matri = np.array([[cd1_1,cd1_2],[cd2_1,cd2_2]])
	CRVAL1 = hdr['CRVAL1']
	CRVAL2 = hdr['CRVAL2']
	ref = np.array([CRVAL1,CRVAL2])
	del_ra = ra-ref[0]
	del_dec = dec-ref[1]
	# A_abs = np.linalg.det(matri)
	anti_matri = np.linalg.inv(matri)
	arr = np.array([del_ra,del_dec])
	resultt = np.dot(anti_matri,arr)
	del_x=resultt[0]
	del_y=resultt[1]
	CRPIX1 = hdr['CRPIX1']
	CRPIX2 = hdr['CRPIX2']
	x = round(CRPIX1+del_x)
	y = round(CRPIX1+del_y)
	off = round(arcsec/0.262)
	x0 = x-off
	x1 = x+off
	y0 = y-off
	y1 = y+off
	if (x0 < 0):
		x0=0
	if (y0 < 0):
		y0=0
	NAXIS1 = hdr['NAXIS1']-1
	NAXIS2 = hdr['NAXIS2']-1
	if (x1 > NAXIS1):
		x1 = NAXIS1
	if (y1 > NAXIS2):
		y1 = NAXIS2
	datanew1 = tabler[y0:y1,x0:x1]
	return datanew1
