# Beanstalk IAM instance profile
resource "aws_iam_instance_profile" "okthess_beanstalk_ec2" {
  name = "okthess-beanstalk-ec2-user"
  role = "${aws_iam_role.okthess_beanstalk_ec2.name}"
}

# Beanstalk IAM role
resource "aws_iam_role" "okthess_beanstalk_ec2" {
  name = "okthess-beanstalk-ec2-role"
  assume_role_policy = "${file("aws_iam_role_policies/okthess-beanstalk-ec2-policy.json")}"
}
