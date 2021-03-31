Role Name
=========

linux_tomcat :: Ansible Role used to install Tomcat on Linux Servers.

Requirements
------------

Tomcat is installed from a RPM which is pulled from a Source URL. Post installation we are using Template blocks to configure Tomcat. All Templates are kept under templates directory.

Role Variables
--------------

* tomcat_source_url variable is defined under default/main.yml directory which is used to define the Tomcat version source URL which is to be installed.

* tomcat_ver variable is defined under vars/main.yml directory which is used to define the Tomcat Version is will get installed.

* ui_manager_user variable is defined under vars/main.yml directory which is used to define the Tomcat UI Manager User.

* ui_manager_pwd variable is defined under vars/main.yml directory which is used to define the Tomcat UI Manager User Password.

* ui_admin_user variable is defined under vars/main.yml directory which is used to define the Tomcat Admin User.

* ui_admin_pwd variable is defined under vars/main.yml directory which is used to define the Tomcat Admin Password.

Handlers
--------

Tomcat Service restart handler is added to the configuration and is invoked as required.

Dependencies
------------

Java need to be installed before we proceed with installation of Tomcat.

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
         - { role: linux_tomcat }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
