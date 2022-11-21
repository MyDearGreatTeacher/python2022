## 安裝PostgreSQL資料庫
```
C:\Program Files\PostgreSQL\15

C:\Program Files\PostgreSQL\15\data

postgres\@@@ksu2022$%$$%

5432
```
```
Installation Directory: C:\Program Files\PostgreSQL\15
Server Installation Directory: C:\Program Files\PostgreSQL\15
Data Directory: C:\Program Files\PostgreSQL\15\data
Database Port: 5432
Database Superuser: postgres
Operating System Account: NT AUTHORITY\NetworkService
Database Service: postgresql-x64-15
Command Line Tools Installation Directory: C:\Program Files\PostgreSQL\15
pgAdmin4 Installation Directory: C:\Program Files\PostgreSQL\15\pgAdmin 4
Stack Builder Installation Directory: C:\Program Files\PostgreSQL\15
Installation Log: C:\Users\user\AppData\Local\Temp\install-postgresql.log
```
## 啟動 到目錄夾底下C:\Program Files\PostgreSQL\15\bin
```
initdb.exe -D  "C:\Program Files\PostgreSQL\15\data"
```
```
pg_ctl.exe start -N “postgresql-15” -D “C:\Program Files\PostgreSQL\15\data” -w
```

```
C:\Program Files\PostgreSQL\15\bin>initdb.exe -D  "C:\Program Files\PostgreSQL\15\data"
The files belonging to this database system will be owned by user "user".
This user must also own the server process.

The database cluster will be initialized with locale "Chinese (Traditional)_Taiwan.950".
Encoding "BIG5" implied by locale is not allowed as a server-side encoding.
The default database encoding will be set to "UTF8" instead.
initdb: could not find suitable text search configuration for locale "Chinese (Traditional)_Taiwan.950"
The default text search configuration will be set to "simple".

Data page checksums are disabled.

fixing permissions on existing directory C:/Program Files/PostgreSQL/15/data ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... windows
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default time zone ... Asia/Taipei
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok
syncing data to disk ... ok

initdb: warning: enabling "trust" authentication for local connections
initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.

Success. You can now start the database server using:

    pg_ctl -D ^"C^:^\Program^ Files^\PostgreSQL^\15^\data^" -l logfile start


C:\Program Files\PostgreSQL\15\bin>pg_ctl.exe start -N "postgresql-15" -D "C:\Program Files\PostgreSQL\15\data"
waiting for server to start....2022-11-21 20:17:30.319 CST [7384] LOG:  starting PostgreSQL 15.1, compiled by Visual C++ build 1914, 64-bit
2022-11-21 20:17:30.325 CST [7384] LOG:  listening on IPv6 address "::1", port 5432
2022-11-21 20:17:30.325 CST [7384] LOG:  listening on IPv4 address "127.0.0.1", port 5432
2022-11-21 20:17:30.386 CST [12492] LOG:  database system was shut down at 2022-11-21 20:17:18 CST
2022-11-21 20:17:30.399 CST [7384] LOG:  database system is ready to accept connections
 done
server started
```

##
```
createuser -s postgres
```
## 使用內建的資料庫管理psql工具連到PostgreSQL資料庫
```
C:\Program Files\PostgreSQL\15\bin>psql
psql (15.1)
Type "help" for help.

user=# help
You are using psql, the command-line interface to PostgreSQL.
Type:  \copyright for distribution terms
       \h for help with SQL commands
       \? for help with psql commands
       \g or terminate with semicolon to execute query
       \q to quit
user=# h
user-# \h
Available help:
  ABORT                            CREATE USER MAPPING
  ALTER AGGREGATE                  CREATE VIEW
  ALTER COLLATION                  DEALLOCATE
  ALTER CONVERSION                 DECLARE
  ALTER DATABASE                   DELETE
  ALTER DEFAULT PRIVILEGES         DISCARD
  ALTER DOMAIN                     DO
  ALTER EVENT TRIGGER              DROP ACCESS METHOD
  ALTER EXTENSION                  DROP AGGREGATE
  ALTER FOREIGN DATA WRAPPER       DROP CAST
  ALTER FOREIGN TABLE              DROP COLLATION
  ALTER FUNCTION                   DROP CONVERSION
  ALTER GROUP                      DROP DATABASE
  ALTER INDEX                      DROP DOMAIN
  ALTER LANGUAGE                   DROP EVENT TRIGGER
  ALTER LARGE OBJECT               DROP EXTENSION
  ALTER MATERIALIZED VIEW          DROP FOREIGN DATA WRAPPER
  ALTER OPERATOR                   DROP FOREIGN TABLE
  ALTER OPERATOR CLASS             DROP FUNCTION
```
## 使用內建的資料庫管理pgadmin4工具連到PostgreSQL資料庫
```
密碼:
```


## 學習
- [PostgreSQL 15.1 Documentation  Documentation](https://www.postgresql.org/docs/current/index.html) 
