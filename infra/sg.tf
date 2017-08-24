# Beanstalk app security group
resource "aws_security_group" "beanstalk_sec_group" {
  name        = "beanstalk_sec_group"
  description = "OKThess beanstalk security group"

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags {
    Name = "beanstalk_sec_group"
  }
}

# RDS security group
resource "aws_security_group" "rds_sec_group" {
  name        = "rds_sec_group"
  description = "DB security group"

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    self        = true
  }

  ingress {
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = ["${aws_security_group.beanstalk_sec_group.id}"]
  }

  tags {
    Name = "rds_sec_group"
  }
}
