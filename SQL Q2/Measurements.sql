CREATE TABLE Measurements (
  Lot_No VARCHAR(20),
  Unit_No INT,
  Product_Code VARCHAR(20),
  T_Height INT(4,3),
  T_Weight INT(5,2)
);

SELECT * FROM Measurements;
DROP TABLE Measurements;
INSERT INTO Measurements VALUES ('DLS0081', 1, 'LIF001_B', 8.644, 384.63);
INSERT INTO Measurements VALUES ('DLS0081', 2, 'LIF001_B', 9.228, 384.63);
INSERT INTO Measurements VALUES ('DLS0081', 3, 'LIF001_B', 8.811, 385.19);
INSERT INTO Measurements VALUES ('DLS0081', 4, 'LIF001_B', 9.08, 385.19);
INSERT INTO Measurements VALUES ('DLS0082', 1, 'LIF001_Y', 10.549, 375);
INSERT INTO Measurements VALUES ('DLS0082', 2, 'LIF001_Y', 10.524, 378.89);
INSERT INTO Measurements VALUES ('DLS0082', 3, 'LIF001_Y', 9.028, 386.11);
INSERT INTO Measurements VALUES ('DLS0082', 4, 'LIF001_Y', 10.973, 391.3);
INSERT INTO Measurements VALUES ('DNM0021', 1, 'LIF001_R', 10.571, 289.19);
INSERT INTO Measurements VALUES ('DNM0021', 2, 'LIF001_R', 8.7, 320.43);
INSERT INTO Measurements VALUES ('DNM0021', 3, 'LIF001_R', 8.652, 323.2);
INSERT INTO Measurements VALUES ('DNM0021', 4, 'LIF001_R', 9.308, 326.07);
INSERT INTO Measurements VALUES ('DNM0022', 1, 'LIF002_Y', 8.455, 516.11);
INSERT INTO Measurements VALUES ('DNM0022', 2, 'LIF002_Y', 7.521, 521.48);
INSERT INTO Measurements VALUES ('DNM0022', 3, 'LIF002_Y', 8.301, 526.48);
INSERT INTO Measurements VALUES ('DNM0022', 4, 'LIF002_Y', 8.482, 531.11);