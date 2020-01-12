import random
import main as maf
import numpy as np

data = ['Licorice', 'Blaber', 'Jensen', 'Sneaky', 'Zeyzal', 'Zantins', 'Mong', 'Ranger', 'dyNquedo', 'TitaN', 'Riyev', 'PVPStejos', 'Diamondprox', 'Kira', 'Lodik', 'Edward', 'PK', 'Empt2y', 'Candy', 'Stitch', 'Koala', 'Evi', 'Steal', 'Ceros', 'Yutapon', 'viviD', 'Nate', 'Tierwulf', 'Plugo', 'Fix', 'Slow', 'ray', 'ClearLove', 'Scout', 'iBOY', 'meiko', 'Relic', 'SolidSnake', 'Cotopaco', 'Renyu', 'Arce', 'Wunder', 'Jankos', 'Perkz', 'Hjarnan', 'Wadid', 'fabFabulous', 'Stomaged', 'GBM', 'Zeitnot', 'SnowFlower', 'BioPanther', 'UDYSOF', 'Triple', 'k1ng', 'Cupcake', 'Rockky', 'Lloyd', 'G4', 'Niksar', 'Rich', 'Haro', 'Shernfire', 'Svenskeren', 'Smeb', 'Score', 'Ucal', 'Deft', 'Mata', 'Impact', 'Xmithie', 'Pobelter', 'Doublelift', 'Olleh', 'Liang', 'Kongyue', 'Uniboy', 'Breeze', 'K', 'Zeros', 'Meliodas', 'Naul', 'BigKoro', 'Palette', 'Hanabi', 'Moojin', 'Maple', 'Betty', 'SwordArt', 'Kiin', 'Spirit', 'Kuro', 'Kramer', 'TusiN', 'LetMe', 'Karsa', 'xiaohu', 'Uzi', 'Ming', 'CuVee', 'Haru', 'Crown', 'Ruler', 'CoreJJ', 'Cabochard', 'Kikis', 'Jiizuke', 'Attila', 'Jactroll','Ssumday', 'AnDa', 'Ryu', 'Rikara', 'aphromoo', 'sOAZ', 'Broxah', 'Caps', 'Rekkles', 'Hylissang', 'Duke', 'Ning', 'RooKie', 'JackeyLove', 'Baolan', 'baybay', 'Mowgli', 'TheShy', 'Bwipo', 'Ambition', 'Mlxg', 'XuHao', 'Benny', 'Dardoch', 'Damonte', 'Lost','Smoothie', 'Hauntzer', 'Grig', 'Bjergsen', 'Zven', 'Mithy', 'Smittyj', 'Shook', 'Selfie', 'Sheriff', 'promisq', 'Tay', 'Shini', 'Envy', 'Absolut', 'RedBert', 'Wos', 'Yang', 'Revolta', 'tockers', 'micaO', 'Jockster', 'SkyBart', 'Minerva', 'Lynkez', 'LUSKKA', 'Professor', 'Vert', 'Robo', 'Turtle', 'Brucer', 'pbO', 'Baiano', 'LEP', 'Chaser', 'Sky', 'Sacy', 'Loop', 'Rakin', 'Jisu', 'Shrimp', 'Goku', 'brTT', 'esA', 'Fitz', 'Carioca', 'Anyyy', 'Sarkis', 'Cabu', 'Cariok', 'Crazy', 'Bono', 'Tempt', 'Aries', 'IgNar', 'ADD', 'Yondu','Ian', 'Pilot', 'Max', 'Sword', 'Tarzan', 'Rather', 'Viper', 'Lehends', 'Lindarang', 'SeongHwan', 'Lava', 'Sangyoon', 'Key', 'Chovy', 'Khan', 'Cuzz', 'Bdd', 'PraY', 'GorillA', 'Fly', 'Aiming', 'Thal', 'Blank', 'Faker', 'Bang', 'Wolf', 'Rush', 'SoHwan', 'UmTi', 'Grace', 'Teddy', 'Nova', 'MaHa', 'Broken Blade', 'Closer', 'Abbedagge', 'Freeze', 'Dumbledoge', 'Hioss', 'Wisdom', 'Naru', 'Rain', 'Rogu', 'Motive', 'Odoamne', 'Xerxe', 'Nisqy', 'Kobbe', 'kaSing', 'Gilius', 'Ruin', 'Djoko', 'Betsy', 'Steeelback', 'SirNukesAlot', 'Vizicsacsi', 'Amazing', 'Nukeduck', 'Upset', 'Vander', 'WhiteKnight', 'Kold', 'Exileh', 'Samux', 'Totoro', 'Profit', 'Memento', 'Blanc', 'HeaQ', 'Norskeren', 'Alphari', 'Maxlore', 'Sencux', 'Hans Sama', 'Mikyx', 'Peanut', 'KaKAO', 'Blossom', 'PieCakeLord', 'MikeYeung', 'Ablazeolive', 'MrRallez', 'Shady', 'FallnBandit', 'Wiggily', 'Tuesday', 'Auto', 'Fill', 'V1per', 'Hard', 'Insanity', 'Shoryu', 'Joey', 'NintendudeX', 'OddOrange', 'Yusui', 'Adrian', 'Shiro', 'Ngo', 'Pekin Woof', 'Erry', 'JayJ', 'Brandini', 'Levi', 'Linsanity', 'Stunt', 'Dhokla', 'Fanatiik', 'Palafox', 'Eclipse', 'Gate', 'Maxtrobo', 'Moon', 'Sun', 'Piglet', 'Vulcan', 'zig', 'Potluck', 'bobqin', 'Benji', 'Sheep', 'Meteos', 'Cody Sun', 'Darshan', 'Reignover', 'huhi', 'Stixxay', 'Biofrost', 'Solo', 'LirA', 'Febiven', 'Apollo', 'Hakuho', 'Goldenglue', 'Keith', 'Lourlo', 'Contractz', 'Mickey', 'Deftly', 'Matt', 'Akaadian', 'PowerOfEvil', 'Arrow', 'BIG', 'Trick', 'Ghost', 'Flame', 'Santorin', 'Keane', 'WILDTURTLE', 'Kwon', 'Huni', 'Altec', 'Fenix', 'Yampi', 'Clid', 'Yagao', 'LvMao', 'Zoom', 'jinjiao', 'Chieftain', 'Mole', 'road', 'AmazingJ', 'LokeN', 'Athena', 'Lwx', 'Xinyi', 'Cool', 'Crisp', 'GimGoon', 'Fdy', 'Eimy', 'Yuuki', 'Newt', 'Jinoo', 'kRYST4L', 'SofM', 'Guoguo', 'Maestr0', 'Flandre', 'Chelly', 'jiekou', 'icon', 'Five', 'Xiyang', 'Mountain', 'Zz1tai', 'Fury', 'H4cker', 'fenfen', 'Yoon', 'XiaoAL', 'Snow', 'Swift', 'FireRain', 'Caveman', 'Aodi', 'GENTLE', 'Condi', 'xiye', 'Missing', '957', 'Hudie', 'Qiuqiu', 'Xx', 'Ggoong', 'CAT', 'MaRin', 'Ben', 'imp', 'Lies', 'SmLz', 'Flawless', 'Doinb', 'killua', 'Mouse', 'M1anhua', 'Move', 'Frozen', 'Padden', 'Zergsting', 'Panky', 'Crush', 'LongB', 'Route', 'Kairos', 'Ragner', 'Stefan', 'Milica', 'Hades', 'Tolerant', 'Armut', 'Trix', 'telracS', 'Innaxe', 'Revanche', 'Elwind', 'Mojito', 'MagiFelix', 'Madness', 'Zzus', 'Thaldrin', 'Leo', 'Effort', 'Pirean', 'Allorim', 'Feng', '3z', 'Crash', 'Apex', 'Deul', 'Dreamer', 'Ziv', 'Westdoor', 'Wako', 'An', 'Albis', 'Ninuo', 'Epic', 'Moonblack', 'Art', 'Zest', 'Rest', 'Breaker', 'FoFo', 'Lilv', 'Ysera', 'erssu', 'Gemini', 'cyeol', 'Unified', 'Kaiwing', 'Wuji', 'Damage', 'Mystic', 'Pepper', 'Easyhoon', 'Y4', 'Pyl', 'XuanXuanPi', 'Able', 'M1ssion', 'Tuna', 'Butter', 'PingPong', 'Rainbow', 'Taizan', 'Berentt', 'Corn', 'Alex', 'Kirei', 'Humanoid', 'Neon', 'BoBo', 'Bugi', 'Morning', 'MMD', 'Rock', 'Kingen','Brook', 'Mightybear', 'Kuzan', 'Clever', 'Asper', 'Mabrey', 'Nestea', 'Raise', 'PaSa', 'Japone', 'WaenA', 'Snitch', 'Only35', 'Mills', '694', 'Light', 'Maestro', 'Angel', 'CoCo', 'Moyu', 'ReGank', 'Rascal', 'Caedrel', 'Spica', 'Cake', 'Luger', 'World6', 'Justice', 'PawN', 'Larssen', 'Laba', 'ShiauC', 'Hana', 'Hope', 'Yueguan', 'Martin', 'Xintai', 'Hy0g4', 'Bydeki', 'Maynah', 'Pbd', 'Savage', 'Jesiz', 'Kino', 'Xico', 'Inori', 'Pilter', 'Secaf Reis', 'West', 'Kiwi', 'Holder', 'Youdang', 'Meow', 'WXZ', 'Lex', 'Gyu', 'Magic', 'Untara', 'Pray', 'Roach', 'Edge', 'SSol', 'Secret', 'Beyond', 'Ninja', 'achuu', 'Seonghwan', 'Marshall', 'Lucete', 'Ruvelius', 'Wraith', 'Andy', 'LemonNation', 'V1PER', 'OmarGod', 'kaizen', 'Kitzuo', 'Whyin', 'Jenkins', 'Jurassiq', 'Xpecial', 'Papa Chau', 'Promisq', 'Minitroupax', 'Targamas', 'Pride', 'Boris', 'Hai', 'Riris', 'Chawy', 'Ayel', 'Ziriguidun', 'Titan', 'takeshi', 'tinowns', 'Matsukaze', 'VVvert', '4LaN', 'Lactea', 'Winged', 'Malrang', 'Cepted', 'HolyPhoenix', 'Rare', 'Viking', 'Backlund', 'J1mmy', 'Veux', 'Melon', 'Sks', 'iBoy', 'Meiko', 'bing', 'Xiaohu', 'Letme', 'y4', 'Karin', 'Tian', 'Knight', 'U Jun', 'Fage', 'Nanzhu', 'Kadir', 'Winter', 'Fireloli', 'Marf', 'Destiny', 'Gear', 'SwordArT', 'CooN', 'Dalka', 'LBB', 'Farfetch', 'Nappon', 'Loong', 'Ace', 'styllEE', 'Neo', 'CaiPi', 'Swing', 'BocaJR', 'TRY', 'Casual', 'Celestial', 'xiaohan', 'Prb', 'Hopezz', 'RD', 'Kid', 'PapaChau', 'Chosenn', 'MGX', 'Ozgur', 'intruder', 'Fiseyin', 'PvPStejos', 'EDward', 'Jirall', 'Oddie', 'Seiya', 'WhiteLotus', 'Genthix', 'Intreso', 'Chippys', 'shernfire', 'Paz', 'Once', 'Ramune', 'YutoriMoyasi', 'Gaeng', 'Stark', 'YiJin', 'Warzone', 'Slay', 'RonOP', 'ikssu', 'Pawn', 'Helper', 'Ella', 'Dyrus', 'Scarra', 'Voyboy', 'Imaqtpie', 'Shiphtur', 'rjsdndgod', 'Madlife', 'Nuclear', 'Chei', 'Trashy', 'Bless', 'Naehyun', 'Mocha', 'padden', 'Shy', 'Phaxi', 'Pridestalker', 'Send0o', 'Loulex', 'mithy', 'Ray', 'Huhi', 'Nexus', 'BeBe', 'Jay', 'Dee', 'Pk', 'wuji', 'LilV', 'MooJin', 'Sedrion', 'KaSing', 'DANDAN', 'xani', 'Scarlet', 'Iluzjonist', 'Lamabear', 'CozQ', 'Yuuki60', 'Dreams', 'Nagne', 'sprattel', 'Looper', 'Froggen', 'Balls', 'WildTurtle', 'LOD', 'Big', 'Seraph', 'Comeback', 'MapleSnow', 'GodKwai', 'Expect', 'brTT RX', 'Dioud', 'Mylon', 'Kami', 'Cris', 'SirT', 'fabbbyyy', 'b4dd', 'Ferchu', 'Krastyel', 'DudsTheBoy', 'Ceos', 'Zuao', 'Danagorn', 'Theusma', 'Lep', 'Slooshi', 'Quas', 'Reven', 'FallenBandit', 'Zag', 'DanDy', 'deftly', 'Wulala', 'Wind', 'SkuLL', 'once1', 'Moonblackk', 'Madnesss', 'Juzinho', 'Vash', 'Rhuckz', 'Zet', 'Iceloli', 'Audi', 'ClearLove7', 'Ohq', 'Zzitai', 'Starlight', 'Megan', 'Barrett', 'Cloud', 'Kabe', 'Wuxx', 'Y1han', 'Avoidless', 'Dian', 'Pinus', 'V', 'Rawbin IV', 'Shoshin', 'Amades', 'Cognac', 'Smoke', 'KonDziSan', 'umuut', 'Endz', 'Kairos Plz', 'PANKY', 'Cheong', 'Ruve sama', 'k0u', 'Soz Purefect', 'mean', 'Rogu sama', 'Cinkrof', 'Immortoru', 'Hustlin', 'Godbro Sama', 'Jwaow', 'Dan', 'Woolite', 'AoD', 'SevenArmy', 'IluzjonistJ', 'Satorius', 'Nardeus', 'Klaj', 'KuKu', 'REFRA1N', 'Noxiak', 'Jiizuké', 'jactroll', 'Kakan', 'DarkSide', 'Quixeth', 'Ben4', 'Koro1', 'Crossman', 'reje', 'konkwon', 'Visdom', 'Coma', 'un1tback', 'Vasilii', 'MorZB', 'Skye', 'Joo', 'Crystal', 'Zero', 'Im Jonny', 'Mash', 'Enzz', 'Ran', 'Mayhem', 'Natz', 'FishBall', 'qi', 'Quan', 'RF Legendary', 'Taikki', 'Banana', 'Arin', 'Crow', 'HappyY', 'Flaxxish', 'Aligan', 'Phurion', 'BANANAFISH','BRAIN', 'LZ', 'HanXuan', 'Omen', 'Eli', 'Eason', 'Pony', 'Soul', 'Veritas', 'Pure', 'Punch', 'bono', 'Zig', 'HuHi', 'Aphromoo', 'Achie', 'LOFS', 'SiuSiu', 'Chunx', 'WIND', 'Brolia', 'meanTnT', 'Godbro', 'Wendelbo', 'MarS', 'Rins', 'Veki', 'AN', 'Expession', 'GuGer', 'Tabzz', 'Hiiva', 'PerkZ', 'Soaz', 'Amazingx', 'KAKAO', 'Hans sama', 'Night', 'nukeduck', 'Hachani', 'Kanani', 'KillerS', 'Madagger', 'AlexIch', 'firel0li', 'Bengi', 'Hetong', 'OniOn', 'Candyseven', 'Xubin', 'WuShuang', 'Republic', 'Savoki', 'Alone', 'Ali', 'GODV', 'Funny', 'Marge', 'Rookie', 'S1mlz', 'juejue', 'five', 'xiyang', 'Baybay', 'Mint', 'TANK', 'Mo', 'cool', 'Endless', 'TinOwns', 'Woswos', 'Aoshi', 'Luskka', 'BocaJunior', 'TheFoxz', 'Thulz', 'Evrot', 'Cabuloso', 'Zentinel', 'Hatrixx', 'Fox', 'Grigne', 'Shynon', 'Baby', 'Strompest', 'Vex', 'Vincent', 'Fabbbyyy', 'FeniX', 'lira', 'MadLife', 'IceBeasto', 'Tabasko', 'Sebekx', 'delord', 'loulex', 'Steve', 'MrRalleZ', 'Mimic', 'steal', 'Pretty', 'P1noy', 'Coco', 'xiaoyu', 'dan', 'Chingz', 'SuKi', 'Rlun', 'Jcain', 'Soulmate', 'Zzr', 'React', 'Reach', 'Elysion', 'Un1tback', 'Emtest', 'Kirito', 'LEYL U NEHAR', 'Atom', 'avenuee', 'PADDEN', 'Wickd', 'Obvious', 'Nerroh', 'Adaniel', 'Whiteknight', 'Zhergoth', 'Youngbin', 'xPeke', 'Peng', 'Decagon Moon', 'Clearlove', 'Ocean', 'caveMan', 'YoDa SL', 'Again', 'Part', 'PentaQ', 'Chen', 'Deceit', 'DreamSha', 'westdoor', 'Minn', 'Rio', 'Crimson', 'Lethilion', 'Phantiks', 'Tussle', 'Yutorimoyasi', 'Dara', 'Doxy', 'Kreox', 'Paranoia', 'Blasting', 'SaNTaS', 'Optimus', 'Archie', 'QQmore', 'Emp', 'Kindless', 'Newbie', 'YoDa', 'Ren', 'Venus', 'MANTARRAYA', 'Godkwai', 'NhocTy', 'Noway', 'Nevan', 'Clearlove7', 'Sya', 'Gamsu', 'Eika', 'Emperor', 'Hybrid', 'FORG1VENGRE', 'xPePii', 'Adryh', 'G0DFRED', 'Wunderwear', 'Nisbeth', 'fredy122', 'Airwaks', 'Safir', 'BetongJocke', 'extinkt', 'Rudy', 'Sonstar', 'Bubbling', 'Cpt Jack', 'TrAce', 'Hipo', 'SoaR', 'SaSin', 'Dinter', 'Chillyz', 'AJ', 'SpeaR', 'Rabi2', 'Never', 'Julian', 'Payne', 'exciting', 'YO', 'SuwaKo', 'Rokenia', 'NL', 'CorGi', 'XUE', 'CandyBB', 'Syuan', 'Yue', 'Yellowstar', 'Bunny FuFuu', 'KiWiKiD', 'KonKwon', 'Crumbz', 'Remi', 'IWDominate', 'kfo', 'beibei', 'Ken', 'BillyBoss', 'Procxin', 'Flaresz', 'Eryon', 'SacyR', 'Skyer', 'Verfix', 'Tierwulf VPP', 'Rakin VPP', 'RedBert VPP', 'TaeYeon', 'Verto', 'Impaler', 'Krislund', 'wewillfailer', 'GAP', 'H1iva', 'Kaze', 'masterwork', 'FORG1VEN', 'Parang', 'Police', 'S0NSTAR', 'Reje', 'Toaster', 'Werlyb', 'Cry', 'Firetrap', 'Sweet', 'Vayn3z', 'Yo', 'Raison', 'Zor', 'Mist', 'XiaoLiang', 'k3soju', 'ShorterACE', 'Poppers OP', 'Impactful', 'Nisker', 'Chorong', 'Massacre', 'Trance', 'Roar', 'Bodydrop', 'Bee Sin', 'Pomi', 'Prototype', 'ohq', 'ShrimP', 'Kez', 'Jynthe', 'Arcsecond', 'Smurf', 'aMiracle', 'Likkrit', 'BaeMe']
team = ['Cloud9', 'KaBuM e-Sports', 'Gambit Esports', 'G-Rex', 'DetonatioN FocusMe', 'Kaos Latin Gamers', 'Edward Gaming', 'Infinity Esports', 'G2 Esports', 'SuperMassive', 'Dire Wolves', 'Ascension Gaming', 'KT Rolster', 'Team Liquid', 'MAD Team', 'Phong Vu Buffalo', 'Flash Wolves', 'Afreeca Freecs', 'Royal Never Give Up', 'Gen.G', 'Vitality', '100 Thieves', 'Fnatic', 'Invictus Gaming', 'Echo Fox', 'Team SoloMid', 'H2K', 'INTZ e-Sports', 'Vivo Keyd', 'ProGaming Esports', 'CNB e-Sports Club', 'Red Canids', 'Flamengo eSports', 'IDM Gaming', 'BBQ Olivers', 'MVP', 'Griffin', 'Hanwha Life Esports', 'Kingzone DragonX', 'SK Telecom T1', 'Jin Air Green Wings', 'Royal Bandits e-sports', 'Team AURORA', 'Splyce', 'Giants Gaming', 'Schalke 04', 'Unicorns of Love', 'Roccat', 'Misfits', 'TSM Academy', 'CLG Academy', 'Team Liquid Academy', 'Echo Fox Academy', 'Cloud9 Academy', 'FlyQuest Academy', '100 Thieves Academy', 'OpTic Academy', 'Clutch Gaming Academy', 'Golden Guardians Academy', 'Counter Logic Gaming', 'Clutch Gaming', 'Golden Guardians', 'OpTic Gaming', 'FlyQuest', 'JD Gaming', 'Bilibili Gaming', 'Funplus Phoenix', 'LGD Gaming', 'Snake Esports', 'OMG', 'Suning Gaming', 'Vici Gaming', 'Team WE', 'Topsports Gaming', 'Rogue Warriors', 'Fenerbahce Esports', 'Dark Passage', 'Bursaspor Esports', 'HWA Gaming', 'YouthCREW', 'Machi 17', 'AHQ e-Sports Club', 'Team Afro', 'J Team', 'Hong Kong Attitude', 'Rampage', 'KSV Esports', 'Kongdoo Monster', 'ROX Tigers', 'INTZ e-Sports Club', 'paiN Gaming', 'Team One e-Sports', 'Galakticos', 'EDward Gaming', 'Rainbow7', 'Pentagram', 'EVOS Esports', 'Dignitas', 'Longzhu Gaming', 'Ever8 Winners', 'Delta Fox', 'Gold Coin United', 'Samsung Galaxy', 'Crew e-Sports Club', 'Immortals', 'Phoenix1', 'Wayi Spider', 'Raise Gaming', 'Red Bulls', 'Origen', 'Mysterious Monkeys', 'Ninjas in Pyjamas', 'EnVyUs', 'RED Canids', 'Big Gods Jackals', 'T Show E-Sports', 'Team oNe e-Sports', 'Keyd Stars', 'Tempo Storm', 'eUnited', 'Fire Ball', 'DAN Gaming', 'I May', 'Newbee', 'P3P eSports', 'Cilekler', 'Wind and Rain', 'Paris Saint-Germain', 'Giants', 'Besiktas', 'Oyunhizmetleri','17 Academy', 'AHQ Fighter', 'CJ Entus', 'Kongdoo Mongster', 'Flyquest', 'Hong Kong Esports', 'Galatasaray Esports', 'QG Reapers', 'Game Talents', 'I MAY', 'Snake eSports', 'NewBee', 'Operation Kino', 'KaBuM eSports', 'Remo Brave eSports', 'Team Gates', 'Kinguin','Fnatic Academy', 'Misfits Academy', 'Millenium', 'eXtreme Gamers', 'Virtus.pro', 'Lyon Gaming', 'GIGABYTE Marines', 'Isurus Gaming', 'Team oNe Esports', 'Young Generation', 'Gigabyte Marines', 'Elements', 'SBENU Sonicboom', 'Cougar eSports', 'Midnight Sun e-Sports', 'Machi17', 'eXtreme Gamers eSports Club', 'Taipei Assassins', 'NRG Esports', 'Renegades', 'Team Impulse', 'INTZ', 'Big Gods eSports', 'Huma', 'Nerv', 'Team Forge', 'Epsilon Esports', 'ESC Ever', 'Team Mist', 'Cloud9 Challenger', 'Eanix', 'Dream Team', 'Nova', 'Apex Pride', 'Apex', 'Albus NoX Luna' ]

def createSingleData(input):
    convert_input = []
    for _ in range(0, 20, 2):
        convert_input.append(team.index(input[_]))
        convert_input.append(data.index(input[_ + 1]))
    return convert_input

def createMultiData(input):
    array = []
    for i in input:
        array.append(createSingleData(i))
    return array


def fakeDataMaker(size):
    array = []
    output = []
    for _ in range(size):
        ac = []
        at_team = team[random.randint(0, 10)]
        from_team = team[random.randint(10, 20)]
        for __ in range(5):
            ac.append(team.index(at_team))
            ac.append(random.randint(0, 20))
        for __ in range(5):
            ac.append(team.index(from_team))
            ac.append(random.randint(20, 40))
        array.append(ac)
        output.append([random.randint(0, 1)])
    return array, output

#multi, output = fakeDataMaker(100)

#print(multi)
#print(output)



dataset = maf.extract_all()
finput, fouput = maf.first_try(dataset)
multi = createMultiData(finput[1:])

output = []

fouput = fouput[1:]

for i in range(0, len(fouput) - 1, 1):
    output.append([int(fouput[i])])

test_multi = multi[3000:3100]
test_output = output[3000:3100]

multi = np.array(multi[:3000], dtype= np.float64)
output = np.array(output[:3000], dtype= np.float64)
multi = multi/1000
print("Data Loaded !")
print(multi)
print(output)




"""
multi = createMultiData([
    ["Cloud9", "Kira", "Cloud9", "Edward", "G-Rex", "Zeyzal", "G-Rex", "Ranger"],
    ["Cloud9", "Jensen", "Cloud9", "dyNquedo", "G-Rex", "Riyev", "G-Rex", "Licorice"],
    ["Cloud9", "TitaN", "Cloud9", "Diamondprox", "G-Rex", "Stitch", "G-Rex", "Koala"],
    ["Cloud9", "Empt2y", "Cloud9", "Stitch", "G-Rex", "Steal", "G-Rex", "Lodik"],
])

output = [
    [1],
    [0],
    [1],
    [0]
]

print(multi)
#createData(["Cloud9", "Kira", "Cloud9", "Edward", "G-Rex", "Zeyzal", "G-Rex", "Ranger" ])
"""