# Write your MySQL query statement below
SELECT e.name as name, b.bonus as bonus FROM Employee as e LEFT JOIN Bonus as b ON e.empId=b.empId WHERE b.bonus is NULL or b.bonus < 1000
