--Credits to (https://genshin.honeyhunterworld.com/) for the Data
INSERT INTO 
Characters (Name, Star, Element_ID, WeaponType_ID, Region_ID, Domain_ID, DomainMaterial_ID, Availabilties, ImgURL)
VALUES
-- St:Star , El:Element , WT:WeaponType , R:Region , D:Domain , DM:DomainMaterial , A:Availability , U:IngURL
--Name                  St El WT  R  D DM  A  U
('Amber',               4, 1, 5, 1, 1, 1, 1, '../../assets/data/images/characters/amber.png'),
('Kaeya',               4, 6, 1, 1, 1, 3, 3, '../../assets/data/images/characters/kaeya.png'),
('Lisa',                4, 4, 4, 1, 1, 3, 3, '../../assets/data/images/characters/lisa.png'),
('Barbara',             4, 2, 4, 1, 1, 1, 1, '../../assets/data/images/characters/barbara.png'),
('Razor',               4, 4, 2, 1, 1, 2, 2, '../../assets/data/images/characters/razor.png'),
('Xiangling',           4, 1, 3, 2, 3, 5, 2, '../../assets/data/images/characters/xiangling.png'),
('Beidou',              4, 4, 2, 2, 3, 6, 3, '../../assets/data/images/characters/beidou.png'),
('Xingqiu',             4, 2, 1, 2, 3, 6, 3, '../../assets/data/images/characters/xingqiu.png'),
('Nigguang',            4, 7, 4, 2, 3, 4, 1, '../../assets/data/images/characters/ningguang.png'),
('Fischl',              4, 4, 5, 1, 1, 3, 3, '../../assets/data/images/characters/fischl.png'),
('Bennett',             4, 1, 1, 1, 1, 2, 2, '../../assets/data/images/characters/bennett.png'),
('Noelle',              4, 7, 3, 1, 1, 2, 2, '../../assets/data/images/characters/noelle.png'),
('Chongyun',            4, 6, 2, 2, 3, 5, 2, '../../assets/data/images/characters/chongyun.png'),
('Sucrose',             4, 3, 4, 1, 1, 1, 1, '../../assets/data/images/characters/sucrose.png'),
('Jean',                5, 3, 1, 1, 1, 2, 2, '../../assets/data/images/characters/jean.png'),
('Diluc',               5, 1, 2, 1, 1, 2, 2, '../../assets/data/images/characters/diluc.png'),
('Qiqi',                5, 6, 1, 2, 3, 4, 1, '../../assets/data/images/characters/qiqi.png'),
('Mona',                5, 2, 4, 1, 1, 2, 2, '../../assets/data/images/characters/mona.png'),
('Keqing',              5, 4, 1, 2, 3, 4, 1, '../../assets/data/images/characters/keqing.png'),
('Venti',               5, 3, 5, 1, 1, 3, 3, '../../assets/data/images/characters/venti.png'),
('Klee',                5, 1, 4, 1, 1, 1, 1, '../../assets/data/images/characters/klee.png'),
('Diona',               4, 6, 5, 1, 1, 1, 1, '../../assets/data/images/characters/diona.png'),
('Tartaglia',           5, 2, 5, 2, 1, 1, 1, '../../assets/data/images/characters/tartaglia.png'),
('Xinyan',              4, 1, 3, 2, 3, 6, 3, '../../assets/data/images/characters/xinyan.png'),
('Zhongli',             5, 7, 3, 2, 3, 6, 3, '../../assets/data/images/characters/zhongli.png'),
('Albedo',              5, 7, 1, 1, 1, 3, 3, '../../assets/data/images/characters/albedo.png'),
('Ganyu',               5, 6, 5, 2, 3, 5, 2, '../../assets/data/images/characters/ganyu.png'),
('Xiao',                5, 3, 3, 2, 3, 4, 1, '../../assets/data/images/characters/xiao.png'),
('Hu Tao',              5, 1, 3, 2, 3, 5, 2, '../../assets/data/images/characters/hutao.png'),
('Rosaria',             4, 6, 3, 1, 1, 3, 3, '../../assets/data/images/characters/rosaria.png'),
('Yanfei',              4, 1, 4, 2, 3, 6, 3, '../../assets/data/images/characters/yanfei.png'),
('Eula',                5, 6, 2, 1, 1, 2, 2, '../../assets/data/images/characters/eula.png'),
('Kaedehara Kazuha',    5, 3, 1, 3, 3, 5, 2, '../../assets/data/images/characters/kazuha.png'),
('Kamisato Ayaka',      5, 6, 1, 3, 5, 8, 2, '../../assets/data/images/characters/ayaka.png'),
('Sayu',                4, 3, 2, 3, 5, 9, 3, '../../assets/data/images/characters/sayu.png'),
('Yoimiya',             5, 1, 5, 3, 5, 7, 1, '../../assets/data/images/characters/yoimiya.png'),
('Aloy',                5, 6, 5, 1, 1, 1, 1, '../../assets/data/images/characters/aloy.png'),
('Kujou Sara',          4, 4, 5, 3, 5, 8, 2, '../../assets/data/images/characters/sara.png'),
('Raiden Shogun',       5, 4, 3, 3, 5, 9, 3, '../../assets/data/images/characters/shogun.png'),
('Sangonimoya Kokomi',  5, 2, 4, 3, 5, 7, 1, '../../assets/data/images/characters/kokomi.png'),
('Thoma',               4, 1, 3, 3, 5, 7, 1, '../../assets/data/images/characters/thoma.png'),
('Gorou',               4, 7, 5, 3, 5, 9, 3, '../../assets/data/images/characters/gorou.png'),
('Arataki Itto',        5, 7, 2, 3, 5, 8, 2, '../../assets/data/images/characters/itto.png'),
('Yun Jin',             4, 7, 3, 2, 3, 5, 2, '../../assets/data/images/characters/yunjin.png'),
('Shenhe',              5, 6, 3, 2, 3, 4, 1, '../../assets/data/images/characters/shenhe.png'),
('Yae Miko',            5, 4, 4, 3, 5, 9, 3, '../../assets/data/images/characters/yaemiko.png'),
('Kamisato Ayato',      5, 2, 1, 3, 5, 8, 2, '../../assets/data/images/characters/ayato.png'),
('Kuki Shinobu',        4, 4, 1, 3, 5, 8, 2, '../../assets/data/images/characters/shinobu.png'),
('Yelan',               5, 2, 5, 2, 3, 4, 1, '../../assets/data/images/characters/yelan.png'),
('Shikanoin Heizou',    4, 3, 4, 3, 5, 7, 1, '../../assets/data/images/characters/heizo.png')

