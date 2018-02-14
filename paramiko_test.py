import paramiko
from paramiko_expect import SSHClientInteraction
prompt = "ubuntu@afd44a6918e5:~\$\s+"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(hostname="10.1.1.11", username="ubuntu", key_filename='/home/ubuntu/.ssh/id_rsa')
ssh.connect(hostname="10.1.1.11", username="ubuntu")

#stdin, stdout, stderr = ssh.exec_command('ls')
#print stdout.readlines()

interact = SSHClientInteraction(ssh, timeout=10, display=True)
interact.expect(prompt)

# Run the first command and capture the cleaned output, if you want the output
# without cleaning, simply grab current_output instead.
interact.send('ls /home/ubuntu')
interact.expect(prompt)
cmd_output = interact.current_output_clean
print(cmd_output)

interact.send("git clone https://github.com/bitelxux/anagrams.git")
interact.expect(prompt)
cmd_output = interact.current_output_clean
print(cmd_output)

interact.send('exit')

print("Saliendo")
ssh.close()
print("Terminado")

