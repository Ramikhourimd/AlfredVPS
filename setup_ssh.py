import pexpect
import os

key_path = os.path.expanduser("~/.ssh/id_rsa.pub")

child = pexpect.spawn(f'ssh-copy-id -i {key_path} root@136.244.106.48', encoding='utf-8')

while True:
    try:
        idx = child.expect(['password:', '(?i)yes/no', pexpect.EOF], timeout=15)
        if idx == 0:
            child.sendline('aZ9}qd]Z+@7?hzyj')
        elif idx == 1:
            child.sendline('yes')
        elif idx == 2:
            break
    except pexpect.TIMEOUT:
        break

print("Done ssh setup")
