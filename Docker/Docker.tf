# Create subnet
resource "azurerm_subnet" "myterraformsubnet1" {
    name                 = "mySubnet"
    resource_group_name  = "test1"
    virtual_network_name = "test1-vnet"
    address_prefix       = "10.0.1.0/24"
}

# Create public IPs
resource "azurerm_public_ip" "myterraformpublicip1" {
    name                         = "myPublicIP"
    location                     = "westeurope"
    resource_group_name          = "test1"
    allocation_method            = "Dynamic"

    tags = {
        environment = "Terraform Demo"
    }
}

# Create Network Security Group and rule
resource "azurerm_network_security_group" "myterraformnsg1" {
    name                = "myNetworkSecurityGroup"
    location            = "westeurope"
    resource_group_name = "test1"
    
    security_rule {
        name                       = "SSH"
        priority                   = 1001
        direction                  = "Inbound"
        access                     = "Allow"
        protocol                   = "Tcp"
        source_port_range          = "*"
        destination_port_range     = "22"
        source_address_prefix      = "*"
        destination_address_prefix = "*"
    }

    tags = {
        environment = "Terraform Demo"
    }
}

# Create network interface
resource "azurerm_network_interface" "myterraformnic1" {
    name                      = "myNIC"
    location                  = "westeurope"
    resource_group_name       = "test1"
    network_security_group_id = "${azurerm_network_security_group.myterraformnsg1.id}"

    ip_configuration {
        name                          = "myNicConfiguration"
        subnet_id                     = "${azurerm_subnet.myterraformsubnet1.id}"    
        private_ip_address_allocation = "Dynamic"
        public_ip_address_id          = "${azurerm_public_ip.myterraformpublicip1.id}"
    }

    tags = {
        environment = "Terraform Demo"
    }
}

data "azurerm_resource_group" "image" {
  name = "test1"
}

data "azurerm_image" "image" { 
  name                = "myImage1"                                        #!!! myImageDocker
  resource_group_name = "${data.azurerm_resource_group.image.name}"
}


# Create virtual machine (now it CentOS)
resource "azurerm_virtual_machine" "myterraformvm1" {
    name                  = "DockerTerraform"
    location              = "westeurope"
    resource_group_name   = "test1"
    network_interface_ids = ["${azurerm_network_interface.myterraformnic1.id}"]
    vm_size               = "Standard_DS1v2"

    storage_os_disk {
        name              = "myOsDisk"
        caching           = "ReadWrite"
        create_option     = "FromImage"
        managed_disk_type = "Premium_LRS"
    }

    storage_image_reference {
        publisher = "OpenLogic"
        offer     = "CentOS"
        sku       = "7.5"
        version   = "latest"
    }

    os_profile {
        computer_name  = "myvm"
        admin_username = "alex"
    }

    os_profile_linux_config {
        disable_password_authentication = true
        ssh_keys {
            path     = "/home/alex/.ssh/authorized_keys"
            key_data = "ssh-rsa-key" 
        }
    }

    provisioner "local-exec" {                   # start comand on machine
        command = "sudo python3 config.py"
    }

    tags = {
        environment = "Terraform Demo"
    }
}