# Ansible

## Installation

```shell
pip install -U ansible
```

## Configuration

```ini
# /etc/ansible/ansible.cfg
https://raw.githubusercontent.com/ansible/ansible/devel/examples/ansible.cfg
```

```ini
# /etc/ansible/hosts
localhost ansible_connection=localhost ansible_become_user=1
```
