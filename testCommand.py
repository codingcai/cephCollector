import json
import os
import glob
import subprocess


ceph_binary = './bin/ceph'
name = '/home/cai/ceph/build/out/mon.a.asok'
command = 'cd /home/cai/ceph/build/ &&'+ceph_binary+' --admin-daemon '+name+' perf'+' dump'+" && cd /home/cai"


print(command)
result=subprocess.check_output(['cd /home/cai/ceph/build/ &&', './bin/ceph', ' --admin-daemon ', '/home/cai/ceph/build/out/osd.2.asok', ' perf', ' dump', ' && cd /home/cai'],shell=True)
print(result)
