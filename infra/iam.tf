# Beanstalk IAM instance profile
resource "aws_iam_instance_profile" "okthess_beanstalk_ec2" {
  name = "okthess-beanstalk-ec2-user"
  role = "${aws_iam_role.okthess_beanstalk_ec2.name}"
}

# Beanstalk IAM role
resource "aws_iam_role" "okthess_beanstalk_ec2" {
  name = "okthess-beanstalk-ec2-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}
