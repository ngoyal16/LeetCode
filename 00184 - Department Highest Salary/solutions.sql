# Write your MySQL query statement below

SELECT 
    d.Name AS Department,
    e.Name as Employee,
    e.Salary as Salary
FROM 
    Employee AS e, Department AS d
WHERE
    e.DepartmentId = d.Id
    AND e.Salary = (
        SELECT
            MAX(Salary)
        FROM
            Employee
        WHERE
            Employee.DepartmentId = d.Id
    )
