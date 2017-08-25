# RDS db
resource "aws_db_instance" "okthess_beanstalk_rds" {
  allocated_storage       = 5
  engine                  = "postgres"
  engine_version          = "9.4.9"
  instance_class          = "db.t2.micro"
  identifier              = "db-okthess"
  name                    = "dbokthess"
  username                = "${var.rds_username}"
  password                = "${var.rds_password}"
  publicly_accessible     = true
  skip_final_snapshot     = true
  vpc_security_group_ids  = ["${aws_security_group.okthess_rds_sg.id}"]
  multi_az                = "false"
  storage_type            = "gp2"
  backup_retention_period = 30
}
