from fabric.api import *
import os

# Set the name of the user login to the remote host
env.user = 'acimafranca'
env.hosts = ['fedora2']
env.port = '22'  # Adjust if you're using a different port

# Define the task to get the hostname of remote machines
def getHostname():
    name = run("hostname")
    print("The host name is:", name)

# Define the task to install a package
def installPackage(pkg='dummy'):
    cmd = 'dnf install ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

# Define the task to remove a package
def removePackage(pkg=''):
    if pkg == '':
        cmd = 'dnf remove dummy -y'
    else:
        cmd = 'dnf remove ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

# Define the task to update packages
def updatePackage(pkg=''):
    if pkg == '':
        cmd = 'dnf update -y --skip-broken'
    else:
        cmd = 'dnf update ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)


# Define the task to create a new user and configure SSH access
def makeUser():
    username = 'ops445p'
    home_dir = '/home/{}'.format(username)
    ssh_dir = '{}/.ssh'.format(home_dir)
    auth_keys_file = '{}/authorized_keys'.format(ssh_dir)
    
    # Create the new user with home directory
    sudo('useradd -m -d {} {}'.format(home_dir, username))
    
    # Add the new user to the sudo group 'wheel'
    sudo('usermod -aG wheel {}'.format(username))
    
    # Create .ssh directory and set permissions
    sudo('mkdir -p {}'.format(ssh_dir))
    sudo('chown {}:{} {}'.format(username, username, ssh_dir))
    sudo('chmod 700 {}'.format(ssh_dir))
    
    # Check if the public key file exists
    if os.path.exists('ops445p_key.pub'):
        # Upload the SSH public key to the authorized_keys file
        put('ops445p_key.pub', '/tmp/authorized_keys')
        sudo('mv /tmp/authorized_keys {}'.format(auth_keys_file))
        sudo('chown {}:{} {}'.format(username, username, auth_keys_file))
        sudo('chmod 600 {}'.format(auth_keys_file))
        print('User {} created and configured with SSH access.'.format(username))
    else:
        print('Error: ops445p_key.pub not found.')

# Define the task to delete a user
def deleteUser(username='ops445p'):
    # Remove the user and their home directory
    sudo('userdel -r {}'.format(username))
    print('User {} deleted.'.format(username))
