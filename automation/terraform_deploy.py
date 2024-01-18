"""
Simple application that do terraform apply
"""
from python_terraform import *

def main():
    """
    Main Function
    :return: None
    """
    # Define Directory
    tf = Terraform(working_dir='/../terraform/aci')
    # Apply
    tf.apply(capture_output='yes', no_color=IsNotFlagged , skip_plan=True)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
