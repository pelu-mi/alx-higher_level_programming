-- Change Encoding of database, table and field to UTF8
USE `hbtn_0c_0`
-- Change encoding of table as it is the only content of the db
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;
