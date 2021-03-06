#!/usr/bin/python

import os,sys
import lcm
import time
from lcm import LCM
import math

home_dir =os.getenv("HOME")
#print home_dir
sys.path.append(home_dir + "/drc/software/build/lib/python2.7/site-packages")
sys.path.append(home_dir + "/drc/software/build/lib/python2.7/dist-packages")
from drc.robot_state_t import robot_state_t
from drc.atlas_raw_imu_batch_t import atlas_raw_imu_batch_t
from drc.atlas_state_t import atlas_state_t
########################################################################################


def on_imu_batch(channel, data):
  m = atlas_raw_imu_batch_t.decode(data)
  for i in range(0,m.num_packets-1):
    print i , m.raw_imu[i].utime , " ", m.raw_imu[i].delta_rotation[0]
  print " ",m.utime
  print " "

  
#################################################################################

lc = lcm.LCM()
print "started"

lc.subscribe("ATLAS_IMU_BATCH", on_imu_batch)
  
while True:
  ## Handle LCM if new messages have arrived.
  lc.handle()

