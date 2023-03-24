CREATE TABLE students (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL,
age INT NOT NULL,
address VARCHAR(255) NOT NULL
);

INSERT INTO students (id, name, age, address) VALUES (001, 'Иванов Иван', 20, 'ул. Ленина, д. 10');
INSERT INTO students (id, name, age, address) VALUES (002, 'Петров Петр', 21, 'ул. Гагарина, д. 5');

SELECT * FROM students WHERE age >= 20;