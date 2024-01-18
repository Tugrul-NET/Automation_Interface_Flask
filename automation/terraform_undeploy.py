"""
Simple application that do terraform destroy
"""
from python_terraform import *

def main():
    """
    Main Function
    :return: None
    """
    # Define Directory
    tf = Terraform(working_dir='/../terraform/aci')
    # Destroy
    tf.destroy(capture_output='yes', no_color=IsNotFlagged, force=IsNotFlagged, auto_approve=True)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
