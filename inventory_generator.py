'''
inventory generator
'''
import sys
import boto3

ec2 = boto3.resource('ec2')

MYSQL_INSTANCE_ID = 'i-03b28edebfdfdb895'
WORDPRESS_INSTANCE_ID = 'i-04827f4c58e62a4e0'

def generate_inventory(database, webserver):
    '''
    generate inventory from instance ids
    '''
    mysql = ec2.Instance(MYSQL_INSTANCE_ID)
    wordpress = ec2.Instance(WORDPRESS_INSTANCE_ID)

    mysql_pub_ip = mysql.public_ip_address
    wordpress_pub_ip = wordpress.public_ip_address

    if mysql_pub_ip is None:
        print('Instance {} is not running'.format(database))
        sys.exit(1)

    if wordpress_pub_ip is None:
        print('Instance {} is not running'.format(webserver))
        sys.exit(1)

    inventory_template = '''[homework]

[mysql]
{}

[wordpress]
{}

[homework:children]
mysql
wordpress

[homework:vars]
ansible_python_interpreter=/usr/bin/python
ansible_ssh_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/homework.pem'''

    print(inventory_template.format(mysql_pub_ip, wordpress_pub_ip))

generate_inventory(MYSQL_INSTANCE_ID, WORDPRESS_INSTANCE_ID)
