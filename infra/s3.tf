# S3 Bucket for storing Elastic Beanstalk task definitions
resource "aws_s3_bucket" "beanstalk_deploys" {
  bucket = "beanstalk-${var.application_name}-deployments"
}
