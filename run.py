import json
import boto3
import time
from securitygrp import secgrpid
from getvpcandsubnet import subnetid
ec2c = boto3.client('ec2', 'us-west-1')

amiid = 'ami-824c4ee2'
insttype = 't2.micro'
secgrpidlist = [secgrpid]
sshkeypair= 'first_key_pair'
imin = 1
while True:
    imax = int(input('Number of instances you want(No more than 20) > '))
    if imax > 20: continue
    else: break

resp = ec2c.run_instances(
    ImageId = amiid,
    InstanceType = insttype,
    KeyName = sshkeypair,
    SecurityGroupIds = secgrpidlist,
    SubnetId = subnetid,
    MaxCount = imax,
    MinCount = imin
)

inst = resp['Instances']
print(len(inst),'============')

all_pending_inst_id = list()
for i in inst:
    pending_instance_id = i['InstanceId']
    all_pending_inst_id.append(pending_instance_id)

print('Waiting for intances to go into running state...')
for inst_id in all_pending_inst_id:
    control = True
    while control:
        rz = ec2c.describe_instance_status(InstanceIds = [inst_id])
        time.sleep(4)
        if not bool(rz): continue
        if len(rz['InstanceStatuses']) == 0: continue

        inststate = rz['InstanceStatuses'][0]['InstanceState']
        print(json.dumps(inststate,indent=2,separators=(',',':')))
        state = inststate['Name']
        if state == 'running':
            control = False
