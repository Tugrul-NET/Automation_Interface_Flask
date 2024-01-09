variable "aci_tenant_name" {
  description = "describe Tenant name"
  default = "Terraform_Tenant"
}

variable aci_username {
  default = "admin"
}

variable aci_password {
  default = "So_Secret_P@ssword"
}

variable aci_url {
  default = "https://<INSERT_IP_ADRESS_HERE>"
}

variable "timeout" {
  description = "The timeout, in minutes, to wait for the virtual machine clone to complete."
  type        = number
  default     = 30
}

locals {
    static_vlan_start       = "vlan-900"
    static_vlan_end         = "vlan-999"
    access_port             = "10"
    access_leaf             = "101"
    PC_port_1               = "5"
    PC_port_2               = "7"
    PC_leaf                 = "102"
    tdn_1                   = "topology/pod-1/paths-101/pathep-[eth1/10]"
    tdn_2                   = "topology/pod-1/paths-102/pathep-[eth1/5]"
    vlan_1                  = "vlan-950"
    vlan_2                  = "vlan-970" 
}

