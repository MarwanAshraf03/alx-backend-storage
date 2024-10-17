-- creates a table `users` in a database
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL auto_increment PRIMARY KEY,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255)
);