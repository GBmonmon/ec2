import boto3
import getip
import json
from getip import get_all_running_Instance_ID, get_all_stopped_Instance_ID




def stop_all_instances(ec2c,instances_ids):
    #turn them to list of string
    all_id_list = list()
    for id in instances_ids:
        start_pos = str(id).find('\'')
        end_pos = str(id)
        end_pos = end_pos[start_pos+1:].find('\'') + start_pos+1
        inst_id = str(id)
        inst_id = inst_id[start_pos+1:end_pos]
        #print(inst_id, 'hahahaahaha')
        all_id_list.append(inst_id)


    for instances_id in all_id_list:
        stop_resp=ec2c.stop_instances(InstanceIds=[instances_id])
        print(json.dumps(stop_resp, indent=2, separators = (',',':')))

def terminate_all_instances(ec2c,instances_ids):
    #turn them to list of string
    all_id_list = list()
    for id in instances_ids:
        start_pos = str(id).find('\'')
        end_pos = str(id)
        end_pos = end_pos[start_pos+1:].find('\'') + start_pos+1
        inst_id = str(id)
        inst_id = inst_id[start_pos+1:end_pos]
        #print(inst_id, 'hahahaahaha')
        all_id_list.append(inst_id)

    for instance_id in all_id_list:
        terminate_resp = ec2c.terminate_instances(InstanceIds = [instance_id])
        print(json.dumps(terminate_resp, indent = 2, separators = (',',':')))


if __name__ == '__main__':
    ec2c = boto3.client('ec2','us-west-1')
    ec2_resource = boto3.resource('ec2', 'us-west-1')


    while True:
        ipt=input('Please only type in <stop> of <terminate> : ')
        if ipt == 'stop' or ipt == 'terminate':
            break
        else:
            continue



    if ipt.lower() ==  'stop':
        a = get_all_running_Instance_ID(ec2_resource)
        stop_all_instances(ec2c,a)
    elif ipt.lower() == 'terminate':
        c = get_all_running_Instance_ID(ec2_resource)
        terminate_all_instances(ec2c, c)
        b = get_all_stopped_Instance_ID(ec2_resource)
        terminate_all_instances(ec2c, b)





#instid = get_all_Running_Instance_ID(ec2c, region)
#resp=ec2c.stop_instances(InstanceIds=[instid])
#print(json.dumps(resp,indent=2,separators=(',',':')))
#resp=ec2c.terminate_instances(InstanceIds=[instid])
#print(json.dumps(resp,indent=2,separators=(',',':')))
