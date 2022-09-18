#小問１
SELECT * FROM gakusei INNER JOIN rishu ON gakusei.gakuseino = rishu.gakuseino;
#小問２
SELECT * FROM gakusei natural INNER JOIN rishu;
#小問３
SELECT gakusei.namae, kamoku.kamokumei, kamoku.kyoushitsu, kamoku.youbi, kamoku.jigen FROM gakusei INNER JOIN rishu ON gakusei.gakuseino = rishu.gakuseino INNER JOIN kamoku ON rishu.kamokuno = kamoku.kamokuno;
#小問４
SELECT gakusei.namae, kamoku.kamokumei, kamoku.kyoushitsu, kamoku.youbi, kamoku.jigen FROM gakusei natural INNER JOIN rishu natural INNER JOIN kamoku;
