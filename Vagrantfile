# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "boxcutter/ubuntu1510"
  config.vm
  config.vm.provision "shell", path: "scripts/ansible.sh"
  config.vm.network "forwarded_port", guest: 80, host: 80
  config.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
  end

  config.vm.define "wordpress" do |wordpress|
    wordpress.vm.provision :ansible_local do |ansible|
      ansible.extra_vars = {ansible_ssh_user: 'vagrant', vagrant: true}
      ansible.verbose = 'v'
      ansible.playbook = "wordpress.yml"
      ansible.inventory_path = "development"
    end
  end
end
