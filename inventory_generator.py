'''
inventory generator
'''
import boto3

ec2 = boto3.resource('ec2')

mysql = ec2.Instance('i-03b28edebfdfdb895')
wordpress = ec2.Instance('i-04827f4c58e62a4e0')

def generate_inventory():
    '''
    generate inventory from instance ids
    '''
    mysql_pub_ip = mysql.public_ip_address
    wordpress_pub_ip = wordpress.public_ip_address

    inventory_template = '''[homework]

[mysql]
{}

[wordpress]
{}

[homework:children]
mysql
wordpress

[homework:vars]
ansible_ssh_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/wordpress.pem'''

    print(inventory_template.format(mysql_pub_ip, wordpress_pub_ip))

generate_inventory()
