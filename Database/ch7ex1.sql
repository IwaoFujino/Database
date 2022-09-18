# �f�[�^�x�[�X���쐬�C�f�[�^�̓��͂ƕ\��
# �f�[�^�x�[�X���Fecsiteinvoicedb
# �f�[�^�x�[�X�쐬
CREATE DATABASE ecsiteinvoicedb;
SHOW databases;
USE ecsiteinvoicedb;
# �e�[�u��customer�쐬�C�f�[�^�}��
CREATE TABLE customer(customer_id CHAR(10), postcode CHAR(20), address CHAR(100), tel CHAR(20), name CHAR(20));
INSERT INTO customer VALUES('C1', '106-0023', '�����s�`�捂�֑�9-9-99', '03-1234-5678', '���C ���Y');
INSERT INTO customer VALUES('C2', '123-2300', '�����s�a�J�揼����9-9-99', '03-5678-1234', '���C �Ԏq');
INSERT INTO customer VALUES('C3', '213-2010', '�����s���c��ԏ�9-9-99', '03-1111-2222', '���� �K�q');
SELECT * FROM customer;
# �e�[�u��goods�쐬�C�f�[�^�}��
CREATE TABLE goods(goods_id CHAR(10), name CHAR(20), price INT);
INSERT INTO goods VALUES('G1', '�V���cM',3150);
INSERT INTO goods VALUES('G2', '�V���[�YLR1',7600);
INSERT INTO goods VALUES('G3', '�A�����J���r�[�t',4200);
INSERT INTO goods VALUES('G4', '�X�j�[�J�[',7600);
INSERT INTO goods VALUES('G5', '�P�[�L',980);
INSERT INTO goods VALUES('G6', '�J�[�f�B�K��',12000);
INSERT INTO goods VALUES('G7', '�t���C�p��',1024);
INSERT INTO goods VALUES('G8', '�C��TT',650);
INSERT INTO goods VALUES('G9', '�}�t���[',1500);
SELECT * FROM goods;
# �e�[�u��request�쐬�C�f�[�^�}��
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
