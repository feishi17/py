'''
python version similar with download_image_decals_dr2.pro
Function Name: testimage
Purpose: give DECals dr2 image name from http://portal.nersc.gov/project/cosmo/data/legacysurvey/dr2/
Input: ra, dec, filter
Output: 
 fileimage1: downloaded image file name, for example: 'decals-0001m002-image-g.fits'
History: 
 Created: Dec 30 2015
Author: Qian Yang, PKU/Steward, qianyang.astro@gmail.com
'''
import numpy as np
import pyfits
def testimage(ra,dec,filter):
	fileimage1='noyq'
	filer='decals-bricks-dr2.fits'
	# http://portal.nersc.gov/project/cosmo/data/legacysurvey/dr2/decals-bricks-dr2.fits
	parr = pyfits.open(filer)
	tabler = parr[1].data
	ra1 = tabler['ra1']
	dec1 = tabler['dec1']
	ra2 = tabler['ra2']
	dec2 = tabler['dec2']
	bricks = tabler['brickname']
	rac = tabler['ra']
	decc = tabler['dec']
	ra_in=np.array((ra1-ra)*(ra2-ra))
	dec_in=np.array((dec1-dec)*(dec2-dec))
	ind=np.where((ra_in <= 0)&(dec_in <= 0))
	ntp = np.shape(ind)
	print('------- Process -------')
	ntp = ntp[1]
	if (ntp > 0):
		if (ntp == 1):
			print('Found one brick...')
			brick=bricks[ind]
			brick=brick[0]
			brick3=brick[0:3]
			fileimage1='http://portal.nersc.gov/project/cosmo/data/legacysurvey/dr2/coadd/'+brick3+'/'+brick+'/decals-'+brick+'-image-'+filter+'.fits'
		else:
			print('Found a few bricks...')
			rac=rac[ind]
			decc=decc[ind]
			bricks=bricks[ind]
			ra_rad=np.multiply(ra,np.pi/180.0)
			rac_rad=np.multiply(rat,np.pi/180.0)
			dec_rad=np.multiply(dec,np.pi/180.0)
			decc_rad=np.multiply(dect,np.pi/180.0)
			result = np.arccos(np.add(np.multiply(np.sin(dec_rad),np.sin(decc_rad)),np.multiply(np.multiply(np.cos(dec_rad),np.cos(decc_rad)),np.cos(np.subtract(ra_rad,rac_rad)))))
			result = np.multiply(result,180.0*3600.0/np.pi)
			id = np.argmin(result)
			brick=bricks[id]
			brick=brick[0]
			brick3=brick[0:3]
			fileimage1='http://portal.nersc.gov/project/cosmo/data/legacysurvey/dr2/coadd/'+brick3+'/'+brick+'/decals-'+brick+'-image-'+filter+'.fits'
	else:
		print('No such objects in Tractor CCD bricks...')
	return fileimage1
