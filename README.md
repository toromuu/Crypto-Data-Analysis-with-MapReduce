# Manual actions to use this project:

0. Clone this repository and access to the main folder

```
git clone https://github.com/toromuu/Crypto-Data-Analysis-with-MapReduce.git

cd Crypto-Data-Analysis-with-MapReduce/
```

1. Export the variable ID associated to each student on this course:
For example:

```
alucloud$ID@hadoopmaster:~/Crypto-Data-Analysis-with-MapReduce$ export ID=184
```

2. Run `configure.sh` script to configure the environment:

```
alucloud$ID@hadoopmaster:~/Crypto-Data-Analysis-with-MapReduce$ sh configure.sh
```

**Note: Since Hadoop's Cluster has not AWS CLI installed and we do not have sudo privileges we need to send the generated Graphs and Tables to S3 bucket, we need to follow below steps**

3. Manually copy the public key generated in previous script:

```
alucloud$ID@hadoopmaster:~$ cat access_lab.pub
```

4. Access AWS LAB instance via ssh

```
ssh alucloud$ID@lab2.cursocloudaws.net
```

5. Add `access_lab.pub` key into `.ssh/authorized_keys`:

```
alucloud$ID@lab:~$ vim .ssh/authorized_keys 
```

6. Retun to Hadoop cluster and run `launch.sh` script to generate the custom database, generate the 5 different queries and upload the results to S3:

```
alucloud$ID@hadoopmaster:~/Crypto-Data-Analysis-with-MapReduce$ sh launch.sh
```

7. Results will be uploaded into below links:



# Automation:

To automate this project you can create a crontab in Hadoop cluster following below steps:

1. Create the crontab:

```
crontab -e
```

2. Choose the editor you want to use for adding the corresponding cron.

```
Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.basic
  3. /usr/bin/vim.tiny
  4. /bin/ed

Choose 1-4 [1]: 
```

3. Add the commands from `crontab` file

**Note: Crontab logs will be saved in `cron_logs.log`**