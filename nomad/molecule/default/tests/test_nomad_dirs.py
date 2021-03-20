import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nomad_folders(host):
    assert host.file("/etc/nomad").is_directory
    assert host.file("/etc/nomad").mode == 0o755
    assert host.file("/etc/nomad").user == "nomad"
