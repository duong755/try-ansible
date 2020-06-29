'''
get wordpress public ip
'''
import sys
import boto3

ec2 = boto3.resource('ec2')

WORDPRESS_INSTANCE_ID = 'i-04827f4c58e62a4e0'

def get_public_ip(webserver):
    '''
    generate wordpress public ip
    '''
    wordpress = ec2.Instance(WORDPRESS_INSTANCE_ID)

    wordpress_pub_ip = wordpress.public_ip_address

    if wordpress_pub_ip is None:
        print('Instance {} is not running'.format(webserver))
        sys.exit(1)

    print(wordpress_pub_ip)

get_public_ip(WORDPRESS_INSTANCE_ID)
