# Database setup
* To create tables, run the ddl.sql script
* Next, to insert sample data into the tables, run sample_data.sql
* versions/ contains incremental scripts that were used to build the DB from initial tate to final state

## Steps to access the DB on NCSU VCL server

1. ssh unityid@remote.eos.ncsu.edu (put password as unity-id password)
2. /mnt/apps/public/CSC/Mysql-Shell/bin/mysql -u your_mysql_acct -p -h classdb2.csc.ncsu.edu (replace your_mysql_acct with your assigned mysql acct which would match your unity ID)
3. Put Student-ID as password here
4. Shift to sql mode by typing '\sql'
5. List available databases using SHOW DATABASES;
6. USE unityid; database
7. run SQL script using command - SOURCE edugrid/db/<script_name>.sql
