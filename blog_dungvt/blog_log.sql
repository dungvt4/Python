DROP DATABASE IF EXISTS blog_log;

CREATE DATABASE IF NOT EXISTS blog_log;

CREATE TABLE IF NOT EXISTS blog_log.posts (
	id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    content VARCHAR(500),
    created_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=1001;