-- create
CREATE TABLE participants (
  id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  age INT NOT NULL,
  PRIMARY KEY (id)
);

-- insert
INSERT INTO participants (id, name, age) VALUES (1, 'Иван Иванов', 20);
INSERT INTO participants (id, name, age) VALUES (2, 'Петр Петров', 25);
INSERT INTO participants (id, name, age) VALUES (3, 'Анна Сидорова', 35);
INSERT INTO participants (id, name, age) VALUES (4, 'Юлия Птушкина', 18);
INSERT INTO participants (id, name, age) VALUES (5, 'Николай Спиридонов', 36);

-- fetch 
SELECT name FROM participants WHERE age > 18;