# hopstools
tools to convert data from the HOPS format

=============================

To run: 

python hops2uvfits.py 

Flags: 
--skip_bl: skip regenerating each baseline uvfits files
--rot_rate: rotate back in time to the original values. Do not do this if you want to average in time after loading the uvfits files. 
--rot_delay: rotate back in frequencies to the original values. Do not do this if you want to average down in frequency after loading the uvfits files. 

=============================

For Katie: 

cd /Users/klbouman/Research/vlbi_imaging/software/hops/build
source hops.bash

run this file from: /Users/klbouman/Research/vlbi_imaging/software/hops/eat