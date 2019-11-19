variable "client_id" {}
variable "client_secret" {}

variable "agent_count" {
    default = 1                     # Original Error: Code="QuotaExceeded" Message="Provisioning of resource(s) for container service k8stest in resource group azure-k8stest failed. Message: The operation couldn't be completed as it results in exceeding quota limit of Core.
}

variable "ssh_public_key" {
    default = "~/.ssh/id_rsa.pub"
}

variable "dns_prefix" {
    default = "k8stest"
}

variable cluster_name {
    default = "k8stest"
}

variable resource_group_name {
    default = "azure-k8stest"
}

variable location {
    default = "westeurope"
}

variable log_analytics_workspace_name {
    default = "testLogAnalyticsWorkspaceName"
}

# refer https://azure.microsoft.com/global-infrastructure/services/?products=monitor for log analytics available regions
variable log_analytics_workspace_location {
    default = "westeurope"
}

# refer https://azure.microsoft.com/pricing/details/monitor/ for log analytics pricing 
variable log_analytics_workspace_sku {
    default = "PerGB2018"
}