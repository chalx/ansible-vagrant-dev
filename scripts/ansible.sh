if [ ! -f /usr/bin/ansible-playbook ]
  then
    apt-get install software-properties-common
    apt-add-repository ppa:ansible/ansible
    apt-get update
    apt-get install -y ansible
fi

cp /vagrant/development /home/vagrant/development
chmod a-x /home/vagrant/development
ansible-playbook /vagrant/wordpress.yml -i /home/
