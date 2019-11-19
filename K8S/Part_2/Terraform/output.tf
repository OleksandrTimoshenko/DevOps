output "client_key" {
    value = "${azurerm_kubernetes_cluster.k8s.kube_config.0.client_key}"
}

output "client_certificate" {
    value = "${azurerm_kubernetes_cluster.k8s.kube_config.0.client_certificate}"
}

output "cluster_ca_certificate" {
    value = "${azurerm_kubernetes_cluster.k8s.kube_config.0.cluster_ca_certificate}"
}

output "cluster_username" {
    value = "${azurerm_kubernetes_cluster.k8s.kube_config.0.username}"
}

output "cluster_password" {
    value = "${azurerm_kubernetes_cluster.k8s.kube_config.0.password}"
}

output "kube_config" {
    value = "${azurerm_kubernetes_cluster.k8s.kube_config_raw}"
}

output "host" {
    value = "${azurerm_kubernetes_cluster.k8s.kube_config.0.host}"
}

resource "aws_instance" "web" {
  provisioner "file" {
    content     = "client_key: ${azurerm_kubernetes_cluster.k8s.kube_config.0.client_key}"
    destination = "/home/oleksandr/clouddrive/terraform-aks-k8s/res"
  }
   provisioner "file" {
    content     = "client_certificate: ${azurerm_kubernetes_cluster.k8s.kube_config.0.client_certificate}"
    destination = "/home/oleksandr/clouddrive/terraform-aks-k8s/res"
  }
   provisioner "file" {
    content     = "cluster_ca_certificate: ${azurerm_kubernetes_cluster.k8s.kube_config.0.cluster_ca_certificate}"
    destination = "/home/oleksandr/clouddrive/terraform-aks-k8s/res"
  }
   provisioner "file" {
    content     = "cluster_username: ${azurerm_kubernetes_cluster.k8s.kube_config.0.username}"
    destination = "/home/oleksandr/clouddrive/terraform-aks-k8s/res"
  }
   provisioner "file" {
    content     = "cluster_password: ${azurerm_kubernetes_cluster.k8s.kube_config.0.password}"
    destination = "/home/oleksandr/clouddrive/terraform-aks-k8s/res"
  }
   provisioner "file" {
    content     = "kube_config: ${azurerm_kubernetes_cluster.k8s.kube_config_raw}"
    destination = "/home/oleksandr/clouddrive/terraform-aks-k8s/res"
  }
   provisioner "file" {
    content     = "host: ${azurerm_kubernetes_cluster.k8s.kube_config.0.host}"
    destination = "/home/oleksandr/clouddrive/terraform-aks-k8s/res"
  }
}