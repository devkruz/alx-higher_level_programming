-- creates the MySQL server user user_0d_1
--   have all privileges on your MySQL server

CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANTS ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
