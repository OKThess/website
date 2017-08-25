# Configure AWS Credentials & Region
provider "aws" {
  profile = "${var.profile}"
  region  = "${var.region}"
}
