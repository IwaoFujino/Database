USE salesbase;
SHOW tables;
#è¨ñ‚ÇP
CREATE VIEW salesview AS SELECT sid, goods, price, quantity, price*quantity AS amount FROM saleslist;
SHOW tables;
#è¨ñ‚ÇQ
SHOW fields FROM salesview;
#è¨ñ‚ÇR
SELECT * FROM salesview;
#è¨ñ‚ÇS
SELECT SUM(amount) AS total_amount FROM salesview;
