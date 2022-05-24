#!/usr/bin/bash

# Upload files to S3 bucket public to read from anywhere
aws s3 cp query1.png s3://alucloud/192/ --acl public-read
aws s3 cp query2.txt s3://alucloud/192/ --acl public-read
aws s3 cp query3.png s3://alucloud/192/ --acl public-read
aws s3 cp query4.txt s3://alucloud/192/ --acl public-read
aws s3 cp query5.txt s3://alucloud/192/ --acl public-read