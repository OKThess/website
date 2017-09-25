# S3 buckets and their policies
resource "aws_s3_bucket" "elasticbeanstalk-eu-central-1-084940027265" {
  bucket        = "elasticbeanstalk-eu-central-1-084940027265"
  acl           = "private"
  force_destroy = "false"
}

resource "aws_s3_bucket" "okthess-static" {
  bucket = "okthess-static"
  acl    = "private"

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["GET", "HEAD", "PUT", "POST"]
    allowed_origins = ["*"]
    expose_headers  = ["ETag"]
    max_age_seconds = 3000
  }
}

resource "aws_s3_bucket_policy" "elasticbeanstalk-eu-central-1-084940027265" {
  bucket = "${aws_s3_bucket.elasticbeanstalk-eu-central-1-084940027265.id}"
  policy = "${file("aws_s3_bucket_policies/okthess-elasticbeanstalk-policy.json")}"
}

resource "aws_s3_bucket_policy" "okthess-static" {
  bucket = "${aws_s3_bucket.okthess-static.id}"
  policy = "${file("aws_s3_bucket_policies/okthess-static-policy.json")}"
}
