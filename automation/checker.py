"""
Simple application for checking automation status
"""

def main(method):
    """
    Main Function
    :return: None
    """
    
    check_update(method)

def check_update(method):
    """
    Check and update Function
    :return: string
    """
    with open('./checker.txt', 'r') as file :
        filedata = file.read()

    if filedata:
        return filedata
    else:
        with open('./checker.txt', 'w') as file:
            file.write(method)
        return ''

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
