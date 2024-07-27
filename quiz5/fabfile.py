from fabric.api import env, run, sudo, put, task

# Set the name of the user login to the remote host
env.user = 'student'
env.port = '7200'  # Replace with your actual port number
env.hosts = ['myvmlab.senecacollege.ca']

@task
def get_hostname():
    """
    Task to get the hostname of the remote machine.
    """
    name = run("hostname")
    print("The host name is:", name)

@task
def install_package(pkg='dummy'):
    """
    Task to install a package on the remote machine using yum.
    """
    cmd = 'yum install ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

@task
def remove_package(pkg='dummy'):
    """
    Task to remove a package from the remote machine using yum.
    """
    cmd = 'yum remove ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

@task
def update_package(pkg=''):
    """
    Task to update packages on the remote machine using yum.
    If no package name is given, all packages will be updated.
    """
    if pkg:
        cmd = 'yum update ' + pkg + ' -y'
    else:
        cmd = 'yum update -y --skip-broken'
    status = sudo(cmd)
    print(status)

@task
def make_user():
    """
    Task to create a new user 'ops445p' with sudo privileges and set up SSH keys.
    """
    # Create the user and home directory
    sudo('useradd -m -d /home/ops445p -s /bin/bash ops445p')

    # Add the user to the wheel group
    sudo('usermod -aG wheel ops445p')

    # Create .ssh directory
    sudo('mkdir -p /home/ops445p/.ssh')
    sudo('chmod 700 /home/ops445p/.ssh')

    # Copy the public key to the authorized_keys file
    put('id_rsa.pub', '/home/ops445p/.ssh/authorized_keys', use_sudo=True)
    sudo('chmod 600 /home/ops445p/.ssh/authorized_keys')
    sudo('chown -R ops445p:ops445p /home/ops445p/.ssh')

# Example public key to be added
with open('id_rsa.pub', 'w') as f:
    f.write('ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD3... user@domain')

@task
def deploy():
    """
    Task to deploy the backup script and set up the cron job.
    """
    install_package('rsync')
    copy_backup_script()
    setup_cron_job()

def copy_backup_script():
    """
    Task to copy the backup script to the /root/bin directory on the remote machine.
    """
    sudo('mkdir -p /root/bin')
    put('/mnt/backup.py', '/root/bin/backup.py', use_sudo=True)
    sudo('chmod 755 /root/bin/backup.py')
    sudo('chown root:root /root/bin/backup.py')

def setup_cron_job():
    """
    Task to set up a cron job to run backup.py every Friday at 2am.
    """
    cron_job = "0 2 * * 5 /root/bin/backup.py"
    sudo(f'(crontab -l 2>/dev/null; echo "{cron_job}") | crontab -')
