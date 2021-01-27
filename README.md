# verint

Dev-Ops Tech Interview exercise 

* The playbook.yml file consists in multiple tasks that put toghether the containers and the servers configuration.
* inventory file has the declaration of target host and a few variables needed at runtime.
* In templates/ directory contains the j2 templates of the configuration files of apache and nginx servers.
* vars/ directory has a few variable declarations that are used by the playbook and the tempates.
* In tests/ directory there is a small python script that captures the response of the apache servers, and checks if the nginx serves the requests in "round robin" mode. This script is user during jenkins run.
