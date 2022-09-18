#小問1
CREATE DATABASE jikanwaribase;
SHOW databases;
USE jikanwaribase;
#小問2
CREATE TABLE gakusei (gakuseino CHAR(10), namae CHAR(20), kana CHAR(30), PRIMARY KEY (gakuseino));
SHOW fields from gakusei;
INSERT INTO gakusei VALUES ('80AB0001', '田中花子', 'たなかはなこ');
INSERT INTO gakusei VALUES ('80AB0002', '山田聡', 'やまださとし');
INSERT INTO gakusei VALUES ('80AB0003', '佐藤美那子', 'さとうみなこ');
INSERT INTO gakusei VALUES ('80AB0004', '鈴木博', 'すずきひろし');
#小問3
CREATE TABLE kamoku (kamokuno  CHAR(10), kamokumei CHAR(20), kyouin CHAR(30), kyoushitsu CHAR(20), tani INT, youbi CHAR(10), jigen CHAR(10), PRIMARY KEY (kamokuno));
SHOW fields from kamoku;
INSERT INTO kamoku VALUES ('C110', 'ネットワーク基礎', '小川', '2111', 2, '火', '1');
INSERT INTO kamoku VALUES ('C111', 'プログラミング入門', '川田', '2111', 2, '火', '2');
INSERT INTO kamoku VALUES ('C211', 'オペレーティングシステム', '山川', '1203', 2, '月', '3');
INSERT INTO kamoku VALUES ('C212', 'データベース', '大山', '1203', 4, '月', '2');
INSERT INTO kamoku VALUES ('C321', 'プロジェクト１', '前田', '1211', 2, '水', '3');
INSERT INTO kamoku VALUES ('C322', 'プロジェクト２', '大島', '1212', 2, '水', '4');
INSERT INTO kamoku VALUES ('T1022', '英語１', '島田', '3221', 2, '火', '2');
INSERT INTO kamoku VALUES ('T1023', '英語２', '島田', '3221', 2, '金', '2');
INSERT INTO kamoku VALUES ('T1211', '体育１', '前川', '体育館', 1, '木', '3');
INSERT INTO kamoku VALUES ('T1212', '体育２', '前川', 'グランド', 1, '火', '2');
#小問4
CREATE TABLE rishu (gakuseino CHAR(10), kamokuno  CHAR(10));
SHOW fields from rishu;
INSERT INTO rishu VALUES ('80AB0001', 'C110'), ('80AB0001', 'C212'), ('80AB0001', 'T1022'), ('80AB0001', 'C321'), ('80AB0001', 'T1211');
INSERT INTO rishu VALUES ('80AB0002', 'C211'), ('80AB0002', 'C110'), ('80AB0002', 'C321'), ('80AB0002', 'T1211'), ('80AB0002', 'T1023');
INSERT INTO rishu VALUES ('80AB0003', 'C211'), ('80AB0003', 'C110'), ('80AB0003', 'T1212'), ('80AB0003', 'C321'), ('80AB0003', 'T1023');
INSERT INTO rishu VALUES ('80AB0004', 'C211'), ('80AB0004', 'C111'), ('80AB0004', 'C322'), ('80AB0004', 'T1212'), ('80AB0004', 'T1023');
#小問5
SELECT * FROM gakusei;
SELECT * FROM kamoku;
SELECT * FROM rishu;
