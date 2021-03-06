import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_is_os_packages_installed(host):
    packages = ["unzip"]
    for p in packages:
        assert host.package(p).is_installed
