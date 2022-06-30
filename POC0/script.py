# from paramiko import SSHClient, AutoAddPolicy
# #___ssh to Ansible machine
# ssh = SSHClient()
import paramiko

#___ssh to Ansible machine

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(hostname='52.37.52.105', port=22 ,timeout=3, username='ec2-user', key_filename='/home/vinh/.ssh/id_rsa')

#___copy playbook files from local machine to Ansible machine
localpath = "/home/vinh/Documents/user_password.xml"
filepath = "/home/ec2-user/user_password.xml"

localpath2 = "/home/vinh/Documents/ansible/intall_TOMCAT.yml"
filepath2 = "/home/ec2-user/playbook.yml"

#copy file user_password.xml to Ansible machine
ftp_client = ssh.open_sftp()
ftp_client.put(localpath, filepath)

#copy file my_playbook.yml to Ansible machine
ftp_client = ssh.open_sftp()
ftp_client.put(localpath2, filepath2)

ftp_client.close()

#___run the playbook
#ssh.exec_command(comm2)

stdin, stdout, stderr = ssh.exec_command("ansible-playbook -i /etc/ansible/hosts /home/ec2-user/playbook.yml ")
print(stdout.read().decode("ascii"))
print(stderr.read().decode("ascii"))

print("Run play-book successfully")

ssh.close()
