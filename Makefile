all:

FORCE:

homework.ini: FORCE
	python3 ./inventory_generator.py > homework.ini

ping: homework.ini
	ansible homework -i ./homework.ini -m ping

play: homework.ini
	ansible-playbook -i ./homework.ini \
	--vault-id mysql_root_password@~/.ansible/default_vault_password \
	--vault-id mysql_database@~/.ansible/default_vault_password \
	--vault-id mysql_user@~/.ansible/default_vault_password \
	--vault-id mysql_password@~/.ansible/default_vault_password \
	--vault-id wordpress_db_name@~/.ansible/default_vault_password \
	--vault-id wordpress_db_user@~/.ansible/default_vault_password \
	--vault-id wordpress_db_password@~/.ansible/default_vault_password \
	./homework.yaml

open:
	$(eval IP = $(shell python3 ./wordpress_address.py))
	xdg-open http://$(IP)

uninstall: homework.ini
	ansible-playbook -i ./homework.ini ./uninstall.yaml
