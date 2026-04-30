-- cteare user and gave all grants.
CREATE IF NOT EXISTS USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;
GRANT ALL PRIVILEGES ON *.* TO 'username'@'%';
FLUSH PRIVILEGES;
