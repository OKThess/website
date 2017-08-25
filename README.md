# OK!Thess

Django application, powers [okthess.gr](http://okthess.gr/).


## Setup

Install requirements:
```
pip3 install -r requirements.txt
```

Then, migrate your database:
```
python3 manage.py migrate
```

Finally, run the Django server:
```
python3 manage.py runserver
```

The Django project is `okthess`. There is one Django app, `main`, which includes
all business logic.

This project uses PostgreSQL.


## Infrastructure

> Notes for my future self

This project is deployed to AWS Elastic Beanstalk using [Terraform](https://www.terraform.io/) (v0.10.2).
The infrastructure resources are described at the [`infra`](/infra) directory.
Those resource assume the default VPC exists (including subnets, route tables, ACLs, internet gateway, etc).

```sh
cd infra
terraform init  # initialize terraform project
terraform validate -var-file terraform.tfvars  # validate tf files
terraform fmt  # format tf files in the default, not very useful, way
terraform plan  # see what will happen if you apply the infra now
terraform plan -var-file production.tfvars  # plan against production secret variables
terraform apply  # apply the infra now, aka make the current resources described in the tf files a reality
```
