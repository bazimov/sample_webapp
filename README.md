# Launch new instance from community AMIs select fedora cloud, for example: ami-56a08841
## Download this repo.
### Put your ec2 instance IP into inventory/hosts file
### Run following command to in the server first
```bash
dnf install -y python python2-dnf python-devel

### Then from the repo you run following ansible command
```bash
ansible-playbook playbooks/main-playbook.yml -i inventory/hosts --limit=web-server

