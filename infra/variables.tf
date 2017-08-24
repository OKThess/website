variable "profile" {
  description = "Name of your profile inside ~/.aws/credentials"
}

variable "application_name" {
  description = "Name of your application"
}

variable "application_description" {
  description = "Sample application based on Elastic Beanstalk"
}

variable "application_environment" {
  description = "Deployment stage e.g. 'staging', 'production', 'test', 'integration'"
}

variable "region" {
  default     = "eu-central-1"
  description = "Defines where your app should be deployed"
}

variable "instance_type" {
  default     = "t2.micro"
  description = "Defines the instance type for EB EC2 instances"
}

variable "autoscaling_size" {
  default     = "2"
  description = "Defines the instance type for EB autoscaling max size"
}
