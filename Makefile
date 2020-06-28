all:

homework.ini:
	python3 ./inventory_generator.py > homework.ini

ping: homework.ini
	ansible homework -i ./homework.ini -m ping

play: homework.ini
	ansible-playbook -i ./homework.ini ./homework.yaml

