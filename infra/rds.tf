# RDS security group
resource "aws_security_group" "rds_sec_group" {
  name        = "rds_sec_group"
  description = "Allow inbound postgres traffic"

  tags {
    Name = "rds_sec_group"
  }
}

resource "aws_security_group_rule" "allow_postgres" {
  type                     = "ingress"
  from_port                = 5432
  to_port                  = 5432
  protocol                 = "tcp"
  security_group_id        = "${aws_security_group.rds_sec_group.id}"
  source_security_group_id = "${aws_security_group.beanstalk_sec_group.id}"
}

# resource "aws_security_group_rule" "allow_outgoing" {
#   type              = "egress"
#   from_port         = 0
#   to_port           = 0
#   protocol          = "-1"
#   security_group_id = "${aws_security_group.rds_sec_group.id}"
#   cidr_blocks       = ["0.0.0.0/0"]
# }

# RDS db
resource "aws_db_instance" "beanstalk_rds" {
  allocated_storage       = 5
  engine                  = "postgres"
  engine_version          = "9.4.9"
  instance_class          = "db.t2.micro"
  identifier              = "db-okthess"
  name                    = "dbokthess"
  username                = "dbuser"
  password                = "dbpassword"
  vpc_security_group_ids  = ["${aws_security_group.rds_sec_group.id}"]
  multi_az                = "false"
  storage_type            = "gp2"
  backup_retention_period = 30
}
