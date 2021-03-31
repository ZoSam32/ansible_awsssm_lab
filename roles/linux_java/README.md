Role Name
=========

linux_java :: Ansible Role used to install Java on Linux Servers.

Requirements
------------

Java is installed using YUM. In case of RHEL, Satellite integration is required.

Role Variables
--------------

jdk_version variable is defined under vars/main.yml directory which is used to define the jdk version which is to be installed.

Dependencies
------------

N.A.

Molecule Testing
----------------

Configuration files have been added to test the ansible playbook on a Docker environment using a Centos8 base image. Following files are used to validate the Playbook convergence,

  * converge.yml: Contains list of Roles which need to be tested within a single Molecule test. We can add multiple Roles to single config file.
  * molecule.yml: Contains information of Provider used for Molecule testing and supported OS. Here we are using Docker with pre-build Centos-8 images.
  * verify.yml: Contain list of test which need to be run against the playbook.

Example Playbook
----------------

Include Role within the playbook in the following way:

    - hosts: servers
      roles:
         - { role: linux_java }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
