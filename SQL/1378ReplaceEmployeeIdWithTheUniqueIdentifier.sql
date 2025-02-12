# Write your MySQL query statement below

select EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id;

# return all ids and name of employees that have unique ids