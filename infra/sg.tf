# Beanstalk app security group
resource "aws_security_group" "okthess_beanstalk_sg" {
  name        = "okthess_beanstalk_sg"
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
    Name = "okthess_beanstalk_sg"
  }
}

# RDS security group
resource "aws_security_group" "okthess_rds_sg" {
  name        = "okthess_rds_sg"
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
    security_groups = ["${aws_security_group.okthess_beanstalk_sg.id}"]
  }

  tags {
    Name = "okthess_rds_sg"
  }
}
