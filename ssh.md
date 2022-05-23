# We need first to generate the ssh-keys rsa to access the lab:

```
alucloud184@hadoopmaster:~$ ssh-keygen -b 2048 -t rsa -f access_lab -q -N ""
```

# MANUALLY: Now we will copy the key from Hadoop Cluster to add it in the lab instance.

```
alucloud184@hadoopmaster:~$ cat access_lab.pub
```

# MANUALLY: Inside the lab system add the above key into the .ssh/authorized_keys

```
alucloud184@lab:~$ vim .ssh/authorized_keys 
```

# We can now access from hadoop cluster to lab instance without adding any password:

```
alucloud184@hadoopmaster:~$ ssh -o StrictHostKeyChecking=no -i access_lab alucloud184@lab2.cursocloudaws.net
```

# This will allow us to scp the generated images into the lab instance, from the Lab we will upload those files to S3.

Example copy files from Hadoop to Lab:

```
alucloud184@hadoopmaster:~$ scp -o StrictHostKeyChecking=no -i access_lab hadoop.txt alucloud184@lab2.cursocloudaws.net:/home/alucloud184/.
```

Example uploading files to S3 bucket from Lab:

```
alucloud184@lab:~$ aws s3 cp hadoop.txt s3://alucloud/192/
upload: ./hadoop.txt to s3://alucloud/192/hadoop.txt
```

