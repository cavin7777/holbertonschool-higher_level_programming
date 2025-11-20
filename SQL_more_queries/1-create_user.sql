-- CREATE, ALL PRI, TO NEW USER
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

--ALL PRIVILEGES
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Recomadation : To reload the grant tables to ensure that the new privileges are put into effect
FLUSH PRIVILEGES;
