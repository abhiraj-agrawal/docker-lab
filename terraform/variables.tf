variable "aws_region" {
  type        = string
}

variable "cluster_name" {
  type        = string
}

variable "cluster_version" {
  type        = string
}

variable "node_group_instance_types" {
  type        = list(string)
}

variable "node_group_desired_size" {
  type        = number
}

variable "node_group_max_size" {
  type        = number
}

variable "node_group_min_size" {
  type        = number
}

variable "use_default_vpc" {
  type        = bool
  default     = true
}