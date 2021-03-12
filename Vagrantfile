IMAGE_NAME = "generic/ubuntu1804"
N = 2

Vagrant.configure("2") do |config|
    config.vm.define "monitoring" do |node|

      node.vm.network "private_network", ip: "192.168.50.2"
      node.vm.box = IMAGE_NAME
      node.vm.provision "ansible" do |ansible|
        ansible.playbook = "playbook.yml"
      end

      node.vm.provider "virtualbox" do |v|
        v.memory = 1024
        v.cpus = 1
      end

    end

end


