# Write your MySQL query statement below

SELECT W1.Id AS Id FROM Weather AS w1 INNER JOIN Weather AS w2 ON DATEDIFF(w1.RecordDate, w2.RecordDate)=1 AND w1.Temperature > w2.Temperature
