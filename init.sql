CREATE DATABASE IF NOT EXISTS app;

CREATE DATABASE IF NOT EXISTS app_dev;

USE app;

CREATE TABLE
    IF NOT EXISTS report (
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT,
        name VARCHAR(125),
        username VARCHAR(50),
        email VARCHAR(125),
        address TEXT,
        phone VARCHAR(15),
        website VARCHAR(125),
        company TEXT,
        title VARCHAR(125),
        body TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );

USE app_dev;
CREATE TABLE
    IF NOT EXISTS report (
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT,
        name VARCHAR(125),
        username VARCHAR(50),
        email VARCHAR(125),
        address TEXT,
        phone VARCHAR(15),
        website VARCHAR(125),
        company TEXT,
        title VARCHAR(125),
        body TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );

FLUSH PRIVILEGES;