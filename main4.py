import rasterio
from rasterio.plot import show

# Open the Red and Near-Infrared (NIR) bands of your satellite image
with rasterio.open('RED_BAND.tif') as red:
    RED = red.read()

with rasterio.open('NIR_BAND.tif') as nir:
    NIR = nir.read()

# Calculate NDVI
NDVI = (NIR.astype(float)-RED.astype(float))/(NIR+RED)

# Display NDVI
show(NDVI)
