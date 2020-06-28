"""Inventory file"""
import boto3

ec2 = boto3.resource('ec2')

instance = ec2.Instance('i-04827f4c58e62a4e0')
instance2 = ec2.Instance('i-087bc4f5e2d3ef2a1')

print(instance.public_ip_address, instance2.public_ip_address)
