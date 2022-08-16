variable "location" {
  type        = string
  description = "Azure region where the resource group and resources will be deployed"
  default     = "Australia Southeast"
}

variable "rgname" {
  description = "Resource group name"
}

variable "acr" {
  description = "acr name"
}

# Service Principle
variable "client_id" {
  description = "Azure Client id"
}

variable "client_secret" {
  description = "Azure Client secret"
}

variable "tenant_id" {
  description = "Azure tenant id"
}

variable "subscription_id" {
  description = "Azure Subscription id"
}

# AKS
variable "aks_cluster_name" {
  description = "Name used for both AKS Cluster and DNS Prefix"
}

variable "kubernetes_version" {
  default = "1.24.0"
}