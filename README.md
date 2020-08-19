Ansible Role: VictoriaMetrics vmagent
=========

Deploy and configure single-node [victoria-metrics](https://victoriametrics.github.io)

Requirements
------------

Ansible

Role Variables
--------------

All variables which can be overridden are stored in defaults/main.yml

Example Playbook
----------------

```text
---
- hosts: vm
  connection: ssh
  become: yes
  roles: 
    - ansible-sn-victoriametrics
```

License
-------

BSD
