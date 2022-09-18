#小問１
CREATE DATABASE salesbase;
USE salesbase;
CREATE TABLE saleslist(sid CHAR(10) NOT NULL, goods CHAR(30), price INT, quantity INT, PRIMARY KEY (sid));
SHOW tables;
SHOW fields FROM saleslist;
INSERT INTO saleslist VALUES('T01', 'テレビ', 198000, 1);
INSERT INTO saleslist VALUES('T02', '冷蔵庫', 125000, 2);
INSERT INTO saleslist VALUES('T03', '洗濯機', 104000, 2);
INSERT INTO saleslist VALUES('T04', '掃除機', 125000, 1);
INSERT INTO saleslist VALUES('T05', 'パソコン', 179800, 4);
INSERT INTO saleslist VALUES('T06', 'カメラ', 58900, 3);
SELECT * FROM saleslist;
#小問２
SELECT sid, goods, price, quantity, price*quantity AS amount FROM saleslist;
#小問３
SELECT SUM(price*quantity) AS total_amount FROM saleslist;
