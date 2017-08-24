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
