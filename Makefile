all:
	ansible all -m ping

setup.local:
	ansible all -m setup

setup.aws: # gathering all facts
	ansible aws -i ./inventory/default.ini -m setup

ping.aws.ini:
	ansible aws -i ./inventory/default.ini -m ping

ping.aws.yaml:
	ansible aws -i ./inventory/default.yaml -m ping

play.local:
	ansible-playbook -i /etc/ansible/hosts ./playbooks/local.yaml -l local

play.aws:
	ansible-playbook -i ./inventory/default.yaml ./playbooks/default.yaml -l aws

