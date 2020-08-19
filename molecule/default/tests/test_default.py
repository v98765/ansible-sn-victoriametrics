import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("files", [
    "/lib/systemd/system/victoria-metrics.service",
    "/usr/local/bin/victoria-metrics-prod"
])

def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file

def test_service(host):
    s = host.service("victoria-metrics")
    # assert s.is_enabled
    assert s.is_running

def test_socket(host):
    s = host.socket("tcp://0.0.0.0:8428")
    assert s.is_listening
