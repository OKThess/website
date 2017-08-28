import os, urllib


def is_ec2_linux():
    """
    Detect if we are running on an EC2 Linux Instance
    See http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify_ec2_instances.html
    """
    system_uuid_filename = '/sys/hypervisor/uuid'
    if os.path.isfile(system_uuid_filename):
        with open(system_uuid_filename) as f:
            uuid = f.read()
            print('is_ec2_linux = true')
            return uuid.startswith('ec2')
    print('is_ec2_linux = false')
    return False

def get_linux_ec2_private_ip():
    """
    Get the private IP Address of the machine if running on an EC2 linux server
    See http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-data-retrieval
    """
    if not is_ec2_linux():
        print('this is not ec2 linux')
        return None

    print('this is indeed ec2 linux')
    response = None
    try:
        response = urllib.request.urlopen('http://169.254.169.254/latest/meta-data/local-ipv4')
        contents = response.read()
        print('req contents:', contents)
        return contents
    except:
        print('req exception')
        return None
    finally:
        print('req finally')
        if response:
            print('close response')
            response.close()
