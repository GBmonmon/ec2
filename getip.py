import boto3
import json
import sys
import getvpcandsubnet

def get_all_running_Instance_ID(ec2_resource):
    all_instances = list()
    instances = ec2_resource.instances.filter(Filters = [{'Name':'instance-state-name', 'Values':['running']}])
    count = 0
    for instance in instances:
        all_instances.append(instance)
        count +=1
    print('Number of running instances returned > ', count)
    return all_instances


def get_all_terminated_Instance_ID(ec2_resource):
    all_terminated = list()
    get_sleeping_terminated_Instance_ID = list()
    instances = ec2_resource.instances.filter(Filters = [ {'Name':'instance-state-name', 'Values':['terminated'] } ])
    count = 0
    for i in instances:
        all_terminated.append(i)
        count +=1
    print('Number of terminated instances returned > ', count)
    return all_terminated


def get_all_stopped_Instance_ID(ec2_resource):
    all_stopped = list()
    get_sleeping_terminated_Instance_ID = list()
    instances = ec2_resource.instances.filter(Filters = [ {'Name':'instance-state-name', 'Values':['stopped'] } ])
    count = 0
    for i in instances:
        all_stopped.append(i)
        count +=1
    print('Number of stopped instances returned > ', count)
    return all_stopped


def get_running_ID_IP_pair(ec2c,lst_of_instanceID):
    #test = ec2c.describe_instances(InstanceIds = lst_of_instanceID[0])

    #turn them to list of string
    all_id_list = list()
    for id in lst_of_instanceID:
        start_pos = str(id).find('\'')
        end_pos = str(id)
        end_pos = end_pos[start_pos+1:].find('\'') + start_pos+1
        inst_id = str(id)
        inst_id = inst_id[start_pos+1:end_pos]
        #print(inst_id, 'hahahaahaha')
        all_id_list.append(inst_id)

    all_id_ip_pair = list()
    for each_id in all_id_list:
        reservations = ec2c.describe_instances(InstanceIds = [each_id])
        public_ip = reservations['Reservations'][0]['Instances'][0]['PublicIpAddress']
        all_id_ip_pair.append((each_id, public_ip))

    return all_id_ip_pair





if __name__ == '__main__':
    ec2c = boto3.client('ec2', 'us-west-1')
    ec2_resource = boto3.resource('ec2')
    running = get_all_running_Instance_ID(ec2_resource)
    #stopped = get_all_stopped_Instance_ID(ec2_resource)
    #terminated = get_all_terminated_Instance_ID(ec2_resource)
    id_ip = get_running_ID_IP_pair(ec2c = ec2c, lst_of_instanceID = running)
    print(id_ip)
