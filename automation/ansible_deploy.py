"""
Simple application that do ansible run for creation
"""
import ansible_runner

def main():
    """
    Main Function
    :return: None
    """
    # Apply
    ansible_runner.run_command(executable_cmd='ansible-playbook', cmdline_args=['/../ansible/create_tenant.yaml', '-i', '/../ansible/inventory.ini', '-vvvv'])

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
