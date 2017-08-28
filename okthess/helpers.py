import os
from urllib import request

def is_ec2_linux():
    """
    Detect if we are running on an EC2 Linux Instance.
    See http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify_ec2_instances.html
    """
    system_uuid_filename = '/sys/hypervisor/uuid'
    if os.path.isfile(system_uuid_filename):
        with open(system_uuid_filename) as f:
            uuid = f.read()
            return uuid.startswith('ec2')
    return False

def get_linux_ec2_private_ip():
    """
    Get the private IP Address of the machine if running on an EC2 linux server.
    See http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-data-retrieval
    """
    if not is_ec2_linux():
        return None

    try:
        response = request.urlopen('http://169.254.169.254/latest/meta-data/local-ipv4')
        private_ip = response.read().decode('UTF-8')
        return private_ip
    except:
        return None
    finally:
        if response:
            response.close()
