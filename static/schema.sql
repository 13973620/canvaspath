CREATE TABLE students (
  id       INT          NOT NULL AUTO_INCREMENT,
  email    VARCHAR(100) NOT NULL,
  password VARCHAR(100) NOT NULL,
  name,
  age,
  gender,
  major,
  street,
  zipcode,
  PRIMARY KEY (id)
);