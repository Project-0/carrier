Atlanta-Carrier Documentation
=============================

*Author*: https://github.com/kvorak

Summary
-------

The Atlanta-Carrier project aims to provide a python application that will 
injest a pre-written Jinja template for a Docker-Compose file, perform certain
variable replacement, and then present the file for download from a Flask 
service.

This will run in a Docker Container which will be part of a Swarm of other
Atlanta services like Samba, FTP, Database Projection, and any number of other
containeraized options.
