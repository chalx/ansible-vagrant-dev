# ansible-vagrant-dev
To start:
* ```vagrant up```
* ```vagrant ssh```
* ```cd /vagrant```
* ```ansible-playbook wordpress.yml -i development``` if you want Wordpress

After executing the steps from above edit:
* Windows: ```%systemroot%\system32\drivers\etc\hosts```
* Linux: ```/etc/hosts```

and add the next entry: ```127.0.0.1 wordpress.local```

To use wordpress after executing the steps from above, go to ```http://wordpress.local```

Wordpress default user and password: ```admin/admin```
