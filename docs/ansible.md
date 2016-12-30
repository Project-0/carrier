# Using Ansible with Carrier Strains

## Preparing the Remote End

When getting ready to run Ansible, you need to have a user account configured on the target machine that can accept an SSH login from the deployment machine's user that is authenticated with an RSA public key.  So on the remote machine:

```
sudo useradd -m LOGIN
sudo -iu LOGIN
mkdir .ssh
touch .ssh/authorized_keys
```

and add your public key(s) to that file.

___
#### External References

*  [Official Documentation](http://docs.ansible.com/ansible/index.html)
