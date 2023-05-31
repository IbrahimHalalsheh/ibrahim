
SELECT AVG(T_Height) as Mean_height
from Measurements
WHERE Product_Code = 'LIF001_B';

SELECT AVG(T_Weight) AS Mean_weight
FROM Measurements
WHERE Product_Code = 'LIF001_B';


SELECT AVG(T_Height) as Mean_height
from Measurements
WHERE Product_Code = 'LIF001_Y';

SELECT AVG(T_weight) AS Mean_weight
FROM Measurements
WHERE Product_Code = 'LIF001_Y';

SELECT AVG(T_height) as Mean_height
from Measurements
WHERE Product_Code = 'LIF001_R';

SELECT AVG(T_Weight) AS Mean_weight
FROM Measurements
WHERE Product_Code = 'LIF001_R';

SELECT AVG(T_Height) as Mean_height
from Measurements
WHERE Product_Code = 'LIF002_Y';

SELECT AVG(T_Weight) AS Mean_weight
FROM Measurements
WHERE Product_Code = 'LIF002_Y';







SELECT Lot_No, Unit_No, T_Weight
FROM Measurements
WHERE Product_Code = 'LIF001_B'
AND Measurements.T_Weight < (
  SELECT MIN(LSL)
  FROM Specifications
  WHERE T_Name = 'T_weight' AND Product_Code = 'LIF001_B'
);



SELECT Lot_No, Unit_No, T_Weight
FROM Measurements
WHERE Product_Code = 'LIF001_Y'
AND Measurements.T_Weight < (
  SELECT MIN(LSL)
  FROM Specifications
  WHERE T_Name = 'T_weight' AND Product_Code = 'LIF001_Y'
);

SELECT Lot_No, Unit_No, T_Weight
FROM Measurements
WHERE Product_Code = 'LIF001_R'
AND Measurements.T_Weight < (
  SELECT MIN(LSL)
  FROM Specifications
  WHERE T_Name = 'T_weight' AND Product_Code = 'LIF001_R'
);


SELECT Lot_No, Unit_No, T_Weight
FROM Measurements
WHERE Product_Code = 'LIF002_Y'
AND Measurements.T_Weight < (
  SELECT MIN(LSL)
  FROM Specifications
  WHERE T_Name = 'T_weight' AND Product_Code = 'LIF002_Y'
);









SELECT Product_Code, AVG(T_Height) AS Mean_height
FROM Measurements
GROUP BY Product_Code
ORDER BY Mean_height DESC
LIMIT 2;







