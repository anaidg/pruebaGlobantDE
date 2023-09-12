# pruebaGlobantDE
se adjuntan dos ficheros, mysql-docker que contiene, que lo que hace es levantar con docker un contenedor de MySQL, con 3 tablas 
-> hired_employees
-> departments 
-> jobs
en una instancia llamada stage donde llegaran los datos de manera estructurada.
para levantar la instancia se ejecuta en la terminal 
sudo docker build -t mysql-docker-image .
sudo docker run -d --name mysql-container -p 3306:3306 mysql-docker-image
sudo docker start <id-contenedor>
sudo docker exec -it mysql-container mysql -u root -p

aca pedira la contraseña de root que se le dio y se encuentra en el dockerfile, esto lo llevara a la consola de Mysql, donde debera cambiar a la BD de stage, con comado 
mysql> USE stage

Para correr el api rest y cargar los archivos que se encuentran en la carpeta de files, es solo correr desde la ruta donde se encuentra el app.py, 
$ python3 app.py
esto levantara el servicio
para probar la carga desde la terminal de linux puede usar el curl con el siguiente comando, asegurece de pasar correctamente la ruta del archivo.
$ curl -X POST -F "files=@files/hired_employees.csv" -F "files=@files/departments.csv" -F "files=@files/jobs.csv" http:/localhost:8000/upload

le debe retornar el siguente mensaje 
{
  "message": "Datos CSV insertados en las tablas de la base de datos correctamente"
}

_____
2. punto
para validar vaya a la consola de mysql que levanto al comienzo y ejecute los queries

--Ejercicio 1
SELECT department, job,SUM(CASE WHEN QUARTER(datetime) = 1 THEN 1 ELSE 0 END) AS Q1, SUM(CASE WHEN QUARTER(datetime) = 2 THEN 1 ELSE 0 END) AS Q2,    SUM(CASE WHEN QUARTER(datetime) = 3 THEN 1 ELSE 0 END) AS Q3,    SUM(CASE WHEN QUARTER(datetime) = 4 THEN 1 ELSE 0 END) AS Q4 FROM     hired_employees  left join departments  ON departments.id = department_id left join jobs  ON jobs.id = job_id WHERE YEAR(datetime) = 2021 GROUP BY department,job ORDER BY   department ;

--Ejercicio 2
SELECT departments.id, department,COUNT(hired_employees.id) AS hired FROM departments LEFT JOIN hired_employees ON departments.id = department_id  WHERE YEAR(datetime) = 2021 GROUP BY department_id,department ;




