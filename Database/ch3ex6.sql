USE salesbase;
SHOW tables;
#����P
CREATE VIEW salesview AS SELECT sid, goods, price, quantity, price*quantity AS amount FROM saleslist;
SHOW tables;
#����Q
SHOW fields FROM salesview;
#����R
SELECT * FROM salesview;
#����S
SELECT SUM(amount) AS total_amount FROM salesview;
