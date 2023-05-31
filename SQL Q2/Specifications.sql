CREATE TABLE Specifications (
  Product_Code VARCHAR(20),
  T_Name VARCHAR(20),
  LSL INT(3,2),
  USL INT(4,2),
  Target INT(3,2)
);

SELECT * FROM Specifications;
DROP TABLE Specifications;
INSERT INTO Specifications VALUES ('LIF001_B', 'T_height', 7.22, 10.57, 8.78);
INSERT INTO Specifications VALUES ('LIF001_Y', 'T_height', 6.78, 10.07, 8.36);
INSERT INTO Specifications VALUES ('LIF001_R', 'T_height', 7.22, 10.57, 8.78);
INSERT INTO Specifications VALUES ('LIF002_Y', 'T_height', 6.78, 10.07, 8.36);
INSERT INTO Specifications VALUES ('LIF001_B', 'T_weight', 360, 470, 410);
INSERT INTO Specifications VALUES ('LIF001_Y', 'T_weight', 329, 500, 410);
INSERT INTO Specifications VALUES ('LIF001_R', 'T_weight', 329, 500, 385);
INSERT INTO Specifications VALUES ('LIF002_Y', 'T_weight', 329, 500, 410);
