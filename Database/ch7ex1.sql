# データベースを作成，データの入力と表示
# データベース名：ecsiteinvoicedb
# データベース作成
CREATE DATABASE ecsiteinvoicedb;
SHOW databases;
USE ecsiteinvoicedb;
# テーブルcustomer作成，データ挿入
CREATE TABLE customer(customer_id CHAR(10), postcode CHAR(20), address CHAR(100), tel CHAR(20), name CHAR(20));
INSERT INTO customer VALUES('C1', '106-0023', '東京都港区高輪台9-9-99', '03-1234-5678', '東海 太郎');
INSERT INTO customer VALUES('C2', '123-2300', '東京都渋谷区松濤台9-9-99', '03-5678-1234', '東海 花子');
INSERT INTO customer VALUES('C3', '213-2010', '東京都千代田区花松9-9-99', '03-1111-2222', '高輪 幸子');
SELECT * FROM customer;
# テーブルgoods作成，データ挿入
CREATE TABLE goods(goods_id CHAR(10), name CHAR(20), price INT);
INSERT INTO goods VALUES('G1', 'シャツM',3150);
INSERT INTO goods VALUES('G2', 'シューズLR1',7600);
INSERT INTO goods VALUES('G3', 'アメリカンビーフ',4200);
INSERT INTO goods VALUES('G4', 'スニーカー',7600);
INSERT INTO goods VALUES('G5', 'ケーキ',980);
INSERT INTO goods VALUES('G6', 'カーディガン',12000);
INSERT INTO goods VALUES('G7', 'フライパン',1024);
INSERT INTO goods VALUES('G8', '靴下TT',650);
INSERT INTO goods VALUES('G9', 'マフラー',1500);
SELECT * FROM goods;
# テーブルrequest作成，データ挿入
CREATE TABLE request(request_id CHAR(10), customer_id CHAR(10), order_date DATE, goods_id CHAR(10), amount INT, shipping_date DATE);
INSERT INTO request VALUES('R1', 'C1', '2020-1-1', 'G1', 2, '2020-1-6');
INSERT INTO request VALUES('R2', 'C1', '2020-1-4', 'G2', 1, '2020-1-9');
INSERT INTO request VALUES('R3', 'C1', '2020-1-8', 'G3', 3, '2020-1-12');
INSERT INTO request VALUES('R4', 'C1', '2020-1-8', 'G4', 2, '2020-1-15');
INSERT INTO request VALUES('R5', 'C2', '2020-1-5', 'G5', 2, '2020-1-9');
INSERT INTO request VALUES('R6', 'C2', '2020-1-6', 'G6', 1, '2020-1-12');
INSERT INTO request VALUES('R7', 'C2', '2020-1-8', 'G4', 2, '2020-1-15');
INSERT INTO request VALUES('R8', 'C3', '2020-2-5', 'G7', 2, '2020-2-9');
INSERT INTO request VALUES('R9', 'C3', '2020-2-6', 'G8', 1, '2020-2-12');
INSERT INTO request VALUES('R10', 'C3', '2020-2-8', 'G9', 2, '2020-2-15');
INSERT INTO request VALUES('R11', 'C3', '2020-2-10', 'G1', 1, '2020-2-16');
SELECT * FROM request;
