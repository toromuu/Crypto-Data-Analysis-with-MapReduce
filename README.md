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

# Automation:

To create the crontab we should apply below commands:

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