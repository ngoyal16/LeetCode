# Write your MySQL query statement below
SELECT (
    SELECT Salary FROM Employee GROUP BY Salary ORDER BY Salary desc LIMIT 1, 1
) AS SecondHighestSalary
