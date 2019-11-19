import os
import paramiko
# terraform start
os.system("cd ~/clouddrive/terraform-aks-k8s && az storage container create -n tfstate --account-name csbca02541675a2x4c58xb1a --account-key Z0rEp9EYaNgifcNLsQTjubdW3nQwQQvhA/drum4GDTj4d5GoCZ5aogXvHyrWvnpy9DC1pY0JLLgVZz95QIz3Lg==")
os.system('cd ~/clouddrive/terraform-aks-k8s && terraform init -backend-config="storage_account_name=csbca02541675a2x4c58xb1a" -backend-config="container_name=tfstate" -backend-config="access_key=Z0rEp9EYaNgifcNLsQTjubdW3nQwQQvhA/drum4GDTj4d5GoCZ5aogXvHyrWvnpy9DC1pY0JLLgVZz95QIz3Lg==" -backend-config="key=codelab.microsoft.tfstate" -reconfigure')
os.system("cd ~/clouddrive/terraform-aks-k8s && export TF_VAR_client_id=d6723eb2-1e25-4d2d-8e6a-ac90fd704329 && export TF_VAR_client_secret=b0dc4dd7-f6b9-4cb1-9366-fd3817e50b13")
os.system("cd ~/clouddrive/terraform-aks-k8s && terraform plan -out out.plan")
os.system("cd ~/clouddrive/terraform-aks-k8s && terraform apply out.plan")

