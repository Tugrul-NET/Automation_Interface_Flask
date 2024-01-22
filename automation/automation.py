from flask import Flask, render_template, request
from time import sleep
app = Flask(__name__)
import terraform_deploy
import terraform_undeploy
import ansible_deploy
import ansible_undeploy

@app.route("/")
def my_form():
    return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Deploy: Terraform') == 'Deploy: Terraform':
            result=check_update(method="Terraform", deploy=True)
            if not result:
                terraform_deploy.main()
                print("Deploy: Terraform")
            else:
                return render_template('index.html', value1="Already Deployed with " + result + " , Undeploy it first")
            return render_template('index.html', value1="Deployed: Terraform")
        elif request.form.get('Undeploy: Terraform') == 'Undeploy: Terraform':
            result=check_update(method="Terraform", deploy=False)
            if not result:
                terraform_undeploy.main()
                print("Undeploy: Terraform")
            else:
                if result == "Not Deployed":
                    return render_template('index.html', value1=result)
                return render_template('index.html', value1="Already Deployed with " + result + " , Undeploy it first")
            return render_template('index.html', value1="Undeployed: Terraform")
        elif request.form.get('Deploy: Ansible') == 'Deploy: Ansible':
            result=check_update(method="Ansible", deploy=True)
            if not result:
                ansible_deploy.main()
                print("Deploy: Ansible")
            else:
                return render_template('index.html', value2="Already Deployed with " + result + " , Undeploy it first")
            return render_template('index.html', value2="Deployed: Ansible")
        elif request.form.get('Undeploy: Ansible') == 'Undeploy: Ansible':
            result=check_update(method="Ansible", deploy=False)
            if not result:
                ansible_undeploy.main()
                print("Undeploy: Ansible")
            else:
                if result == "Not Deployed":
                    return render_template('index.html', value2=result)
                return render_template('index.html', value2="Already Deployed with " + result + " , Undeploy it first")
            return render_template('index.html', value2="Undeployed: Ansible")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html")

def check_update(method, deploy):
    """
    Check and update Function
    :return: string
    """
    with open('./checker.txt', 'r') as file :
        filedata = file.read()
    filedata = filedata.strip()

    if filedata:
        if deploy == False:
            print(filedata)
            print(method)
            if filedata == method:
                print(filedata)
                print(method)
                with open('./checker.txt', 'w') as file:
                    file.write('')
                return ''
            else:
                return filedata
        return filedata
    else:
        if deploy == True:
            with open('./checker.txt', 'w') as file:
                file.write(method)
            return ''
        if deploy == False:
            return 'Not Deployed'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1234', debug=True)
