## AWS prerequisites
1. Before you run this program, make sure you have a aws account and have it configured to your system using cli <aws configure>
You will need AWSAccessKeyId and AWSSecretKey for that.
2. You will need your .pem file.
3. You need to import time, boto3, json, etc...

## Program objective: Create instance then stop or terminate the instances we created
There are several files. But you only need to run "load.py", <Usage python load.py> 
1. It will execute the getvpcandsubnet.py file to get your vpc id and subnet id. 
2. It will get your security group id needed for create the instances. If you don't have one, it will create a new security for you. 
3. It will launch the instances doing the API call. For the image we use, we can not create more than 20 instances.  
4. It will get the those running instances's id and instance's ip for you as a list containning tuple with id and ip.
5. It will give your a choice as to wanting those stopped or terminated.    
