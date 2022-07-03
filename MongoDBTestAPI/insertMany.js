//USED for Adding Data/ Backup Data
//load("C:Users/user/Documents/MiniProjects/MongoDBTestAPI/insertMany.js");
db.Characters.insertMany([
    {name:"Amber",              star:4, element:"Pyro",     type:"Bow",         region:"Mondstadt", domain:"Forsaken Rift", material:"Freedom", availability:["Sunday","Monday","Thursday"],        imgurl:"../../assets/data/images/characters/amber.png" },
    {name:"Kaeya",              star:4, element:"Cryo",     type:"Sword",       region:"Mondstadt", domain:"Forsaken Rift", material:"Ballad",  availability:["Sunday","Wednesday","Saturday"],     imgurl:"../../assets/data/images/characters/amber.png" },
    {name:"Lisa",               star:4, element:"Electro",  type:"Catalyst",    region:"Mondstadt"},
    {name:"Barbara",            star:4, element:"Hydro",    type:"Catalyst",    region:"Mondstadt"},
    {name:"Razor",              star:4, element:"Electro",  type:"Claymore",    region:"Mondstadt"},
    {name:"Xiangling",          star:4, element:"Pyro",     type:"Polearm",     region:"Liyue"},
    {name:"Beidou",             star:4, element:"Electro",  type:"Claymore",    region:"Liyue"},
    {name:"Xingqiu",            star:4, element:"Hydro",    type:"Sword",       region:"Liyue"},
    {name:"Ningguang",          star:4, element:"Geo",      type:"Catalyst",    region:"Liyue"},
    {name:"Fischl",             star:4, element:"Electro",  type:"Bow",         region:"Mondstadt"},
    {name:"Bennett",            star:4, element:"Pyro",     type:"Sword",       region:"Mondstadt"},
    {name:"Noelle",             star:4, element:"Geo",      type:"Claymore",    region:"Mondstadt"},
    {name:"Chongyun",           star:4, element:"Cryo",     type:"Claymore",    region:"Liyue"},
    {name:"Sucrose",            star:4, element:"Anemo",    type:"Catalyst",    region:"Mondstadt"},
    {name:"Jean",               star:5, element:"Anemo",    type:"Sword",       region:"Mondstadt"},
    {name:"Diluc",              star:5, element:"Pyro",     type:"Claymore",    region:"Mondstadt"},
    {name:"Qiqi",               star:5, element:"Cryo",     type:"Sword",       region:"Liyue"},
    {name:"Mona",               star:5, element:"Hydro",    type:"Catalyst",    region:"Mondstadt"},
    {name:"Keqing",             star:5, element:"Electro",  type:"Sword",       region:"Liyue"},
    {name:"Venti",              star:5, element:"Anemo",    type:"Bow",         region:"Mondstadt"},
    {name:"Klee",               star:5, element:"Pyro",     type:"Catalyst",    region:"Mondstadt"},
    {name:"Diona",              star:4, element:"Cryo",     type:"Bow",         region:"Mondstadt"},
    {name:"Tartaglia",          star:5, element:"Hydro",    type:"Bow",         region:"Liyue"},
    {name:"Xinyan",             star:4, element:"Pyro",     type:"Claymore",    region:"Liyue"},
    {name:"Zhongli",            star:5, element:"Geo",      type:"Polearm",     region:"Liyue"},
    {name:"Albedo",             star:5, element:"Geo",      type:"Sword",       region:"Mondstadt"},
    {name:"Ganyu",              star:5, element:"Cryo",     type:"Bow",         region:"Liyue"},
    {name:"Xiao",               star:5, element:"Anemo",    type:"Polearm",     region:"Liyue"},
    {name:"Hu Tao",             star:5, element:"Pyro",     type:"Polearm",     region:"Liyue"},
    {name:"Rosaria",            star:4, element:"Cryo",     type:"Polearm",     region:"Mondstadt"},
    {name:"Yanfei",             star:4, element:"Pyro",     type:"Catalyst",    region:"Liyue"},
    {name:"Eula",               star:5, element:"Cryo",     type:"Claymore",    region:"Mondstadt"},
    {name:"Kaedahara Kazuha",   star:5, element:"Anemo",    type:"Sword",       region:"Inazuma"},
    {name:"Kamisato Ayaka",     star:5, element:"Cryo",     type:"Sword",       region:"Inazuma"},
    {name:"Sayu",               star:4, element:"Anemo",    type:"Claymore",    region:"Inazuma"},
    {name:"Yoimiya",            star:5, element:"Pyro",     type:"Bow",         region:"Inazuma"},
    {name:"Aloy",               star:5, element:"Cryo",     type:"Bow",         region:"Mondstadt"},
    {name:"Kujou Sara",         star:4, element:"Electro",  type:"Bow",         region:"Inazuma"},
    {name:"Raiden Shogun",      star:5, element:"Electro",  type:"Polearm",     region:"Inazuma"},
    {name:"Sangonomiya Kokomi", star:5, element:"Hydro",    type:"Catalyst",    region:"Inazuma"},
    {name:"Thoma",              star:4, element:"Pyro",     type:"Polearm",     region:"Inazuma"},
    {name:"Gorou",              star:4, element:"Geo",      type:"Bow",         region:"Inazuma"},
    {name:"Arataki Itto",       star:5, element:"Geo",      type:"Claymore",    region:"Inazuma"},
    {name:"Yun Jin",            star:4, element:"Geo",      type:"Polearm",     region:"Liyue"},
    {name:"Shenhe",             star:5, element:"Cryo",     type:"Polearm",     region:"Liyue"},
    {name:"Yae Miko",           star:5, element:"Electro",  type:"Catalyst",    region:"Inazuma"},
    {name:"Kamisato Ayato",     star:5, element:"Hydro",    type:"Sword",       region:"Inazuma"},
    {name:"Kuki Shinobu",       star:4, element:"Electro",  type:"Sword",       region:"Liyue"},
    {name:"Yelan",              star:5, element:"Hydro",    type:"Bow",         region:"Liyue"},
    {name:"Shikanoin Heizou",   star:4, element:"Anemo",    type:"Catalyst",    region:"Liyue"}

]);