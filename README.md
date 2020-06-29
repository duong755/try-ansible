# Ansible

## Installation

- Ansible, Boto3 (AWS python sdk)

```shell
pip install -U ansible
pip install -U boto3
```

- AWS CLI

## Configuration

```ini
# /etc/ansible/ansible.cfg
# https://raw.githubusercontent.com/ansible/ansible/devel/examples/ansible.cfg
```

```ini
# ~/.aws/config
[default]
region=REGION
```

```ini
# ~/.aws/credentials
[default]
aws_access_key_id=ACCESS_KEY_ID_FULL_ACCESS_EC2
aws_secret_access_key=SECRET_KEY
```
