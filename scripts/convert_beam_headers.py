import glob
from astropy.io import fits

# Converts FITS headers of MeerKAT primary beam model created with Eidos into format required for ddf-pipeline
g=glob.glob('primary_beam*.fits')

for f in g:
    print('Doing',f)
    hdu=fits.open(f)
    hdu[0].header['CTYPE1']='X'
    hdu[0].header['CTYPE2']='Y'
    hdu.writeto('fixed_'+f,overwrite=True)
