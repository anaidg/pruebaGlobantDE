--queries para corren en la consola de mysql
--Ejercicio 1
SELECT department, job,SUM(CASE WHEN QUARTER(datetime) = 1 THEN 1 ELSE 0 END) AS Q1, SUM(CASE WHEN QUARTER(datetime) = 2 THEN 1 ELSE 0 END) AS Q2,    SUM(CASE WHEN QUARTER(datetime) = 3 THEN 1 ELSE 0 END) AS Q3,    SUM(CASE WHEN QUARTER(datetime) = 4 THEN 1 ELSE 0 END) AS Q4 FROM     hired_employees  left join departments  ON departments.id = department_id left join jobs  ON jobs.id = job_id WHERE YEAR(datetime) = 2021 GROUP BY department,job ORDER BY   department ;

--Ejercicio 2
SELECT departments.id, department,COUNT(hired_employees.id) AS hired FROM departments LEFT JOIN hired_employees ON departments.id = department_id  WHERE YEAR(datetime) = 2021 GROUP BY department_id,department ;


