#����1
CREATE DATABASE jikanwaribase;
SHOW databases;
USE jikanwaribase;
#����2
CREATE TABLE gakusei (gakuseino CHAR(10), namae CHAR(20), kana CHAR(30), PRIMARY KEY (gakuseino));
SHOW fields from gakusei;
INSERT INTO gakusei VALUES ('80AB0001', '�c���Ԏq', '���Ȃ��͂Ȃ�');
INSERT INTO gakusei VALUES ('80AB0002', '�R�c��', '��܂����Ƃ�');
INSERT INTO gakusei VALUES ('80AB0003', '�������ߎq', '���Ƃ��݂Ȃ�');
INSERT INTO gakusei VALUES ('80AB0004', '��ؔ�', '�������Ђ낵');
#����3
CREATE TABLE kamoku (kamokuno  CHAR(10), kamokumei CHAR(20), kyouin CHAR(30), kyoushitsu CHAR(20), tani INT, youbi CHAR(10), jigen CHAR(10), PRIMARY KEY (kamokuno));
SHOW fields from kamoku;
INSERT INTO kamoku VALUES ('C110', '�l�b�g���[�N��b', '����', '2111', 2, '��', '1');
INSERT INTO kamoku VALUES ('C111', '�v���O���~���O����', '��c', '2111', 2, '��', '2');
INSERT INTO kamoku VALUES ('C211', '�I�y���[�e�B���O�V�X�e��', '�R��', '1203', 2, '��', '3');
INSERT INTO kamoku VALUES ('C212', '�f�[�^�x�[�X', '��R', '1203', 4, '��', '2');
INSERT INTO kamoku VALUES ('C321', '�v���W�F�N�g�P', '�O�c', '1211', 2, '��', '3');
INSERT INTO kamoku VALUES ('C322', '�v���W�F�N�g�Q', '�哇', '1212', 2, '��', '4');
INSERT INTO kamoku VALUES ('T1022', '�p��P', '���c', '3221', 2, '��', '2');
INSERT INTO kamoku VALUES ('T1023', '�p��Q', '���c', '3221', 2, '��', '2');
INSERT INTO kamoku VALUES ('T1211', '�̈�P', '�O��', '�̈��', 1, '��', '3');
INSERT INTO kamoku VALUES ('T1212', '�̈�Q', '�O��', '�O�����h', 1, '��', '2');
#����4
CREATE TABLE rishu (gakuseino CHAR(10), kamokuno  CHAR(10));
SHOW fields from rishu;
INSERT INTO rishu VALUES ('80AB0001', 'C110'), ('80AB0001', 'C212'), ('80AB0001', 'T1022'), ('80AB0001', 'C321'), ('80AB0001', 'T1211');
INSERT INTO rishu VALUES ('80AB0002', 'C211'), ('80AB0002', 'C110'), ('80AB0002', 'C321'), ('80AB0002', 'T1211'), ('80AB0002', 'T1023');
INSERT INTO rishu VALUES ('80AB0003', 'C211'), ('80AB0003', 'C110'), ('80AB0003', 'T1212'), ('80AB0003', 'C321'), ('80AB0003', 'T1023');
INSERT INTO rishu VALUES ('80AB0004', 'C211'), ('80AB0004', 'C111'), ('80AB0004', 'C322'), ('80AB0004', 'T1212'), ('80AB0004', 'T1023');
#����5
SELECT * FROM gakusei;
SELECT * FROM kamoku;
SELECT * FROM rishu;
