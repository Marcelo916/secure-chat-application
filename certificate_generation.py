#!/usr/bin/env python3

import subprocess
from python_hosts import Hosts, HostsEntry


def prompt_for_common_name():
    return input("What is the common name for your chat server? ")


def write_common_name(common_name):
    with open('common_name.txt', 'w') as f:
        print(common_name, file=f)


def update_host_file(common_name):
    hosts = Hosts(path='/etc/hosts')
    hosts.remove_all_matching(address='10.0.0.4')
    new_entry = HostsEntry(entry_type='ipv4', address='10.0.0.4', names=[common_name])
    hosts.add([new_entry])
    hosts.write()


def generate_private_key():
    # STEP 5
    cmd = "sudo openssl genrsa -out chatserver-key.pem 2048"
    subprocess.run(cmd.split(" "), capture_output=True)


def generate_CSR(common_name):
    # STEP 6
    cmd = ("sudo openssl req -nodes -new -config /etc/ssl/openssl.cnf -key chatserver-key.pem "
           "-out chatserver.csr -subj /C=US/ST=California/L=Monterey/O=Team3/OU=PA4/CN={common_name}"
           )
    subprocess.run(cmd.split(" "), capture_output=True)


def generate_cert_from_CSR():
    # STEP 7
    cmd = ("sudo openssl x509 -req -days 365 -in chatserver.csr -CA /etc/ssl/demoCA/cacert.pem "
           "-CAkey /etc/ssl/demoCA/private/cakey.pem -CAcreateserial -out chatserver-cert.pem"
           )
    subprocess.run(cmd.split(" "), capture_output=False)


def put_into_place():
    cmd = "sudo mv chatserver-cert.pem /etc/ssl/demoCA/newcerts/."
    subprocess.run(cmd.split(" "), capture_output=False)
    cmd = "sudo mv chatserver-key.pem /etc/ssl/demoCA/private/."
    subprocess.run(cmd.split(" "), capture_output=False)
    cmd = "sudo mv chatserver.csr /etc/ssl/demoCA/."
    subprocess.run(cmd.split(" "), capture_output=False)


if __name__ == "__main__":

    common_name = prompt_for_common_name()
    write_common_name(common_name)
    update_host_file(common_name)
    generate_private_key()
    generate_CSR(common_name)
    generate_cert_from_CSR()
    put_into_place()
