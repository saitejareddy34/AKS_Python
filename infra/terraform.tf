terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">3.0.1"
    }
  }
  backend "azurerm" {
    resource_group_name  = "Tfstate_rg"
    storage_account_name = "tfstatepythonaksstorage"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}