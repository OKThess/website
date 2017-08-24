# Security group for beanstalk env
resource "aws_security_group" "beanstalk_sec_group" {
  name        = "beanstalk_sec_group"
  description = "OKThess beanstalk security group"

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags {
    Name = "beanstalk_sec_group"
  }
}

# Beanstalk Application
resource "aws_elastic_beanstalk_application" "beanstalk_application" {
  name        = "${var.application_name}"
  description = "${var.application_description}"
}

# Beanstalk Environment
resource "aws_elastic_beanstalk_environment" "beanstalk_application_environment" {
  name                = "${var.application_name}-${var.application_environment}"
  application         = "${aws_elastic_beanstalk_application.beanstalk_application.name}"
  solution_stack_name = "64bit Amazon Linux 2017.03 v2.5.0 running Python 3.4"
  tier                = "WebServer"

  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "InstanceType"
    value     = "${var.instance_type}"
  }

  setting {
    namespace = "aws:autoscaling:asg"
    name      = "MaxSize"
    value     = "${var.autoscaling_size}"
  }

  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "EC2KeyName"
    value     = "okthess-two"
  }

  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "IamInstanceProfile"
    value     = "${aws_iam_instance_profile.beanstalk_ec2.name}"
  }

  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "SecurityGroups"
    value     = "${aws_security_group.beanstalk_sec_group.name}, ${aws_security_group.rds_sec_group.name}"
  }

  setting {
    namespace = "aws:rds:dbinstance"
    name      = "DBEngine"
    value     = "postgres"
  }

  setting {
    namespace = "aws:rds:dbinstance"
    name      = "DBEngineVersion"
    value     = "9.4.9"
  }

  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "RDS_USERNAME"
    value     = "${aws_db_instance.beanstalk_rds.username}"
  }

  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "RDS_PASSWORD"
    value     = "${aws_db_instance.beanstalk_rds.password}"
  }

  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "RDS_DB_NAME"
    value     = "${aws_db_instance.beanstalk_rds.name}"
  }

  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "RDS_HOSTNAME"
    value     = "${aws_db_instance.beanstalk_rds.endpoint}"
  }
}
