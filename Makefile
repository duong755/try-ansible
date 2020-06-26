all:
	ansible all -m ping

ping.ini:
	ansible aws -i ./inventory/default.ini -m ping

ping.yaml:
	ansible aws -i ./inventory/default.yaml -m ping

play.default:
	ansible-playbook -i ./inventory/default.yaml ./playbooks/default.yaml -l aws

