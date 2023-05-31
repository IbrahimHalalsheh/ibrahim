CREATE TABLE Production_Sequence ( 
  Order_id INT, 
  Date DATE,
  Product_Family VARCHAR(20),
  Variant VARCHAR(1)
);

SELECT * FROM Production_Sequence;

INSERT INTO Production_Sequence VALUES (1, '5/14/2022', 'LIF001', 'B');
INSERT INTO Production_Sequence VALUES (2, '6/2/2022', 'LIF001', 'Y');
INSERT INTO Production_Sequence VALUES (3, '6/17/2022', 'LIF001', 'B');
INSERT INTO Production_Sequence VALUES (4, '7/1/2022', 'LIF003', 'B');
INSERT INTO Production_Sequence VALUES (5, '7/17/2022', 'LIF002', 'R');
INSERT INTO Production_Sequence VALUES (6, '8/5/2022', 'LIF002', 'Y');
INSERT INTO Production_Sequence VALUES (7, '8/19/2022', 'LIF002', 'G');
INSERT INTO Production_Sequence VALUES (8, '9/1/2022', 'LIF001', 'G');
INSERT INTO Production_Sequence VALUES (9, '9/15/2022', 'LIF002', 'Y');
