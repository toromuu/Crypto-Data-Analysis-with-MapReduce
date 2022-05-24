# Crypto-Data-Analysis-with-MapReduce


1. Export the variable ID associated to each student on this course:

```
export ID=184
```

2. Run `configure.sh` script to configure the environment:

/bin/bash /home/alucloud$ID/Crypto-Data-Analysis-with-MapReduce/configure.sh

3. Follow manual steps on `ssh-key-readme.md` readme file.

4. Run manually `launch.sh` script:

```
/bin/bash /home/alucloud$ID/Crypto-Data-Analysis-with-MapReduce/launch.sh
```

# Pending:

We would like to run above command in a crontab to be executed every day, but right now we don't have sudo privileges to run cronjobs or check whether the cron can be executed correctly in Hadoop cluster. 

To create the crontab we should apply below commands:

1. Create the crontab:

```
crontab -e
```

2. Choose the editor you want to use for adding the corresponding cron.

3. Add the following line to run the script each day at 00:05 and save the output logs into a file for debuging:

```
5 0 * * * /bin/bash /home/alucloud$ID/Crypto-Data-Analysis-with-MapReduce/launch.sh >> cron_logs.log 2>&1
```

Note: For testing you can change the crontab time to 2 minutes using this: `*/2 * * * *`