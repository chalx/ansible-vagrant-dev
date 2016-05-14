# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "boxcutter/ubuntu1510"
  config.vm
  config.vm.provision "shell", inline: "sudo apt-get update && sudo apt-get install -y python-pip python-dev && sudo pip install markupsafe && sudo pip install ansible==1.9.2 && sudo cp /usr/local/bin/ansible /usr/bin/ansible"
  config.vm.network "forwarded_port", guest: 80, host: 80
  config.vm.synced_folder "wordpress", "/home/vagrant/wordpress", :owner => "www-data", :group => "www-data"
  config.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
  end
end
