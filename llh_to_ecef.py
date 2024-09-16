# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#  Converts LLH vector components to ECEF
# Parameters:
#  lat_deg: LLH latitude in degrees
#  lon_deg: LLH longitude in degrees
#  hae_km: Height above Ellipsoid in km
# Output:
#  Prints the r_x_km, r_y_km, and r_z_km components of the location
#
# Written by Elise Turka
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.1363
E_E    = 0.081819221456

# helper functions

# initialize script arguments
lat_deg = float('nan') # LLH lat in degrees
lon_deg = float('nan') # LLH lon in degrees
hae_km = float('nan') # height above ellipsoid in km

# parse script arguments
if len(sys.argv)==4:
  lat_deg = float(sys.argv[1])
  lon_deg = float(sys.argv[2])
  hae_km = float(sys.argv[3])
else:
  print(\
   'Usage: '\
   'python3 llh_to_ecef.py lat_deg lon_deg hae_km'\
  )
  exit()

## calc-denom
def calc_denom(ecc, lat_rad):
    return math.sqrt(1.0-math.pow(ecc,2.0) * math.pow(math.sin(lat_rad),2.0))

# calculating helper variables - deg converted to RADIANS
lat_rad = lat_deg * math.pi/180.0
lon_rad = lon_deg * math.pi/180.0
denom = calc_denom(E_E,lat_rad)

c_E = R_E_KM/denom
s_E = (R_E_KM*(1-math.pow(E_E,2)))/denom
r_x_km = (c_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km = (c_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km = (s_E+hae_km)*math.sin(lat_rad)

# print x, y, and z components
print(str(r_x_km))
print(str(r_y_km))
print(str(r_z_km))
