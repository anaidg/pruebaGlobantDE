CREATE TABLE stage.departments (
    id INT,
    department VARCHAR(255)

);

CREATE TABLE stage.hired_employees (
    id INT,
    name VARCHAR(255),
    datetime VARCHAR(255),
    department_id INT,
    job_id INT

);

CREATE TABLE stage.jobs (
    id INT,
    job VARCHAR(255)

);

CREATE VIEW stage.hired_employees_vw AS
SELECT 
 id,
 name,
 datetime,
 SUBSTRING(datetime, 1, 10) AS start_time,
 department_id,
 job_id
FROM stage.hired_employees
;
