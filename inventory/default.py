"""Inventory file"""
import boto3

ec2 = boto3.resource('ec2')

instance = ec2.Instance('i-0366b36be9d957c3d')

print(instance.public_ip_address)
