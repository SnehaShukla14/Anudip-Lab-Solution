mysql> Create Database SQL_LAB;
Query OK, 1 row affected (0.01 sec)

mysql> use SQL_LAB;
Database changed
mysql> -- Lab Assignment 1
mysql> -- Database Schema: BankAccount Table
mysql> -- Table Columns: account_id (Primary Key), account_holder_name, account_balance
mysql>
mysql> -- Create Table: BankAccount
mysql> -- Purpose: Define the BankAccount table schema
mysql> CREATE TABLE BankAccount (
    -> account_id INT PRIMARY KEY,
    -> account_holder_name VARCHAR(100) NOT NULL,
    -> account_balance DECIMAL(15, 2) NOT NULL
    -> );
Query OK, 0 rows affected (0.03 sec)

mysql> show tables;
+-------------------+
| Tables_in_sql_lab |
+-------------------+
| bankaccount       |
+-------------------+
1 row in set (0.00 sec)

mysql> desc bankaccount;
+---------------------+---------------+------+-----+---------+-------+
| Field               | Type          | Null | Key | Default | Extra |
+---------------------+---------------+------+-----+---------+-------+
| account_id          | int           | NO   | PRI | NULL    |       |
| account_holder_name | varchar(100)  | NO   |     | NULL    |       |
| account_balance     | decimal(15,2) | NO   |     | NULL    |       |
+---------------------+---------------+------+-----+---------+-------+
3 rows in set (0.01 sec)

mysql> -- Task 1: Insert Data Write an SQL INSERT statement to insert data into the BankAccount table.
mysql> -- Purpose: Insert data into the BankAccount table
mysql> INSERT INTO BankAccount (account_id, account_holder_name, account_balance)
    -> VALUES (101, 'Sneha', 45000.00),
    ->        (102, 'Janhavi', 25000.00),
    ->        (103, 'Aanchal', 32000.00),
    ->        (104, 'Sonali', 15000.00),
    ->        (105, 'Rutuja', 60000.00);
Query OK, 5 rows affected (0.02 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from bankaccount;
+------------+---------------------+-----------------+
| account_id | account_holder_name | account_balance |
+------------+---------------------+-----------------+
|        101 | Sneha               |        45000.00 |
|        102 | Janhavi             |        25000.00 |
|        103 | Aanchal             |        32000.00 |
|        104 | Sonali              |        15000.00 |
|        105 | Rutuja              |        60000.00 |
+------------+---------------------+-----------------+
5 rows in set (0.00 sec)

mysql> -- Task 2: Retrieving Data Write an SQL SELECT statement to retrieve the account_holder_name and account_balance of all account holders from the BankAccount table.
mysql> -- Purpose: Retrieve the account_holder_name and account_balance of all account holders
mysql> SELECT account_holder_name, account_balance
    -> FROM BankAccount;
+---------------------+-----------------+
| account_holder_name | account_balance |
+---------------------+-----------------+
| Sneha               |        45000.00 |
| Janhavi             |        25000.00 |
| Aanchal             |        32000.00 |
| Sonali              |        15000.00 |
| Rutuja              |        60000.00 |
+---------------------+-----------------+
5 rows in set (0.00 sec)

mysql> -- Task 3: Filtering Data Write an SQL SELECT statement to retrieve the account_holder_name and account_balance where the account_balance is more than 30,000.
mysql> -- Purpose: Retrieve account_holder_name and account_balance where account_balance is more than 30,000
mysql> SELECT account_holder_name, account_balance
    -> FROM BankAccount
    -> WHERE account_balance > 30000;
+---------------------+-----------------+
| account_holder_name | account_balance |
+---------------------+-----------------+
| Sneha               |        45000.00 |
| Aanchal             |        32000.00 |
| Rutuja              |        60000.00 |
+---------------------+-----------------+
3 rows in set (0.00 sec)

mysql> -- Task 4: Updating Data Write an SQL UPDATE statement to change the account_balance of the account holder whose ID is 101.
mysql> -- Purpose: Update the account_balance of the account holder with account_id = 101
mysql> UPDATE BankAccount
    -> SET account_balance = 50000.00
    -> WHERE account_id = 101;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from BankAccount;
+------------+---------------------+-----------------+
| account_id | account_holder_name | account_balance |
+------------+---------------------+-----------------+
|        101 | Sneha               |        50000.00 |
|        102 | Janhavi             |        25000.00 |
|        103 | Aanchal             |        32000.00 |
|        104 | Sonali              |        15000.00 |
|        105 | Rutuja              |        60000.00 |
+------------+---------------------+-----------------+
5 rows in set (0.00 sec)

mysql>