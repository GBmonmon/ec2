import getvpcandsubnet
secgrpname = 'aws_gbmonmon1'

try:
    secgrpfilter = [
        {
            'Name': 'group-name', 'Values':[secgrpname]
        }
    ]
    secgroups = getvpcandsubnet.ec2c.describe_security_groups(Filters = secgrpfilter )
    #print(secgroups)
    secgrptouse = secgroups['SecurityGroups'][0]
    secgrpid = secgrptouse['GroupId']

except:
    print('No security group, will create security group' + secgrpname)
    secgrptouse = getvpcandsubnet.ec2c.create_security_group(GroupName = secgrpname,
                                                             Description = 'aws class open ssh, http, https',
                                                             VpcId = getvpcandsubnet.vpcid)
    secgrpid = secgrptouse['GroupId']
    print('Create security group > ', secgrpid)
    portlist = [22,80,443]
    for port in portlist:
        try:
            getvpcandsubnet.ec2c.authorize_security_group_ingress(
                CidrIp='0.0.0.0/0',
                FromPort=port,
                GroupId=secgrpid,
                IpProtocol='tcp',
                ToPort=port
            )
        except:
            print('error opening port: '+ port)
            exit()
if __name__ == '__main__': print(secgrpid)
