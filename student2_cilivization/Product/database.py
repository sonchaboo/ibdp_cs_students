import sqlite3

with sqlite3.connect('Mark.db') as connection:
        cursor = connection.cursor()
        # cursor.execute('delete from civ where id=0')
        cursor.execute("create table bans (name varchar(200))")
        # cursor.execute('delete from civ')
        # cursor.execute('drop table civ')
        #cursor.execute('drop table bans')
        # cursor.execute("create table civ (id integer, name varchar(200), description varchar(1000), vers integer)")
        # cursor.execute("insert into civ values (24, 'American - Teddy Roosevelt', 'Teddy Roosevelts unique agenda is Big Stick Policy. He likes civilizations that have a city on his home continent and remain peaceful, while disliking those that start wars in his home continent. His leader ability is Roosevelt Corollary. His units receive a +5 Combat Strength bonus on the American home continent, and all tiles in a city with a National Park receive +1 Appeal. America under Roosevelt can also build the Rough Rider when Rifling is researched', 1)")
        # cursor.execute("insert into civ values (25, 'Arabian - Saladin', 'Saladins unique agenda is Ayyubid Dynasty. He likes leaders with his worship building, and dislikes leaders who follow other Religions or wage war on followers of his Religion. His leader bonus is Righteousness of the Faith, which lowers the Faith cost of his worship building and allows it to provide bonus Science, Faith, and Culture.', 1)")
        # cursor.execute("insert into civ values (26, 'Australian - John Curtin', 'Curtins unique agenda is Perpetually on Guard. He likes civilizations that liberate captured cities and dislikes civilizations that are occupying enemy cities. His leader ability is Citadel of Civilization. It provides the Australians with a 100% Production bonus if they have either been the target of a declaration of war in the past 10 turns or liberated a city in the past 20 turns (10 in Gathering Storm).', 1)")
        # cursor.execute("insert into civ values (27, 'Aztec - Montezuma', 'Montezumas unique agenda, Tlatoani, involves liking civilizations who have the same luxury resources as him. He dislikes civilizations who have luxuries which he does not possess. Montezumas leader ability, Gifts for the Tlatoani, causes luxury resources in Aztec territory to give an Amenity Amenity to two extra cities. Military units receive +1 Combat Strength for each different luxury resource improved in Aztec lands.', 1)")
        # cursor.execute("insert into civ values (28, 'Brazilian - Pedro II', 'Pedro IIs unique agenda is called Patron of the Arts. He desires Great People and dislikes civilizations who get the Great People he was trying to acquire. Pedros leader ability, Magnanimous, allows him to recoup 20% of the Great Person points used after recruiting or patronizing a Great Person.', 1)")
        # cursor.execute("insert into civ values (29, 'Egyptian - Cleopatra', 'Cleopatras unique agenda, Queen of the Nile, causes her to favor civilizations with a strong military and dislike civilizations with a weaker military. Her unique ability, Mediterraneans Bride, gives +4 Gold Gold to Trade Routes Egypt starts. Other civilizations Trade Routes to Egypt provide +2 Food to them and +2 Gold for Egypt.', 1)")
        # cursor.execute("insert into civ values (30, 'English - Victoria', 'Victorias unique agenda is called Sun Never Sets. She desires expansion to all the continents on the map, likes civilizations on her home continent, and dislikes civilizations on continents where she doesnt have cities. Her leader ability is called Pax Britannica. Founded cities outside of her home continent receive a free melee unit, and another one if a Royal Navy Dockyard is built there. It also grants access to the Redcoat unique unit when the Military Science technology is researched.', 1)")
        # cursor.execute("insert into civ values (31, 'French - Catherine de Medici', 'Catherine de Medicis unique agenda is Black Queen. She wishes to gain as many Spies and as much Diplomatic Visibility as she can, and dislikes leaders who ignore espionage. Her leader ability, Catherines Flying Squadron, grants her 1 level of Diplomatic Visibility greater than normal with every met civilization. She also gains an extra Spy capacity and a free Spy after researching Castles, and all her Spies start with a free promotion.', 1)")
        # cursor.execute("insert into civ values (32, 'German - Frederick Barbarossa', 'Frederick Barbarossas unique agenda is called Iron Crown. He does not like civilizations that associate with city-states, since he would like to conquer them. His leader ability is called Holy Roman Emperor. It provides him with an additional Military policy slot and +7 Strength Combat Strength for units fighting city-states.', 1)")
        # cursor.execute("insert into civ values (33, 'Greek - Pericles', 'Pericles unique agenda is Delian League. He likes leaders that are not competing for the same city-state allegiance, and dislikes leaders that are directly competing for city-state allegiance. His leader ability is Surrounded by Glory, which grants increased Culture Culture for each city-state that Pericles is the Suzerain of.', 1)")
        # cursor.execute("insert into civ values (34, 'Greek - Gorgo', 'Gorgos unique agenda is With Your Shield Or On It. She never gives up items in a peace deal, prefers leaders who havent yielded in a peace deal, and dislikes any leader who has surrendered in a peace deal or any leader who has never engaged in war. The Culture Culture is equal to 50% of the base Strength Combat Strength of the defeated unit.', 1)")
        # cursor.execute("insert into civ values (35, 'Indian - Gandhi', 'Gandhis unique agenda is Peacekeeper. He will resist starting or getting involved in wars if he might be branded a warmonger for doing so; he likes other leaders that keep the peace and dislikes warmongers. His leader ability is Satyagraha. For each civilization India has met who has founded a religion and is not at war, India gets a significant boost in Faith. Civilizations fighting wars against India suffer additional happiness penalties.', 1)")
        # cursor.execute("insert into civ values (36, 'Indonesian - Gitarja', 'Gitarjas unique agenda is called Archipelagic State. She likes civilizations that avoid settling or conquering cities on small landmasses and dislikes civs that have many such cities. Her leader ability is called Exalted Goddess of the Three Worlds. She can purchase naval units with Faith and her religious units can embark and disembark for free. She also receives +2 Faith from City Centers that are adjacent to Coast or Lake tiles.', 1)")
        # cursor.execute("insert into civ values (37, 'Japanese - Hojo Tokimune', 'Hojo Tokimunes unique agenda is Bushido. He prefers civilizations with both a strong military and Faith or Culture. He dislikes civilizations with a strong military with weak Faith and Culture. His leader ability is Divine Wind. His land units receive +5 Combat Strength on land tiles adjacent to Coast tiles, his naval units receive +5 Combat Strength on Coast tiles, and he builds Encampment, Holy Site, and Theater Square districts in half the usual time.', 1)")
        # cursor.execute("insert into civ values (38, 'Khmer - Jayavarman VII', 'Jayavarman VIIs unique agenda is called An End to Suffering. He likes civilizations that have Holy Sites and a high average city Citizen Population, and dislikes civs that are lacking in either of these areas. His leader ability is called Monasteries of the King. His Holy Sites trigger Culture Bombs, and provide extra Food and Housing if placed along rivers.', 1)")
        # cursor.execute("insert into civ values (39, 'Kongolese - Mvemba a Nzinga', 'Mvemba a Nzingas unique agenda is Enthusiastic Disciple. He likes leaders who spread their religion to his cities and dislikes leaders who have founded a religion and have not brought it to his cities. His leader ability is Religious Convert. He may not build Holy Site districts, gain Great Prophets, or found a religion. However, he gains all beliefs of any religion that has established itself in a majority of his cities and receives an Apostle.', 1)")
        # cursor.execute("insert into civ values (40, 'Macedonian - Macedonian', 'Alexanders unique agenda is called Short Life of Glory. He likes civilizations that are at war with nations other than Macedon and dislikes civilizations that are at peace. His leader ability is called To the Worlds End. It eliminates war weariness in his cities and allows his units to heal when he captures a city with a wonder. It also allows him to produce the Hetairoi, a unique unit that replaces the Horseman.', 1)")
        # cursor.execute("insert into civ values (41, 'Norwegian - Harald Hardrada', 'Harald Hardradas unique agenda, Last Viking King, involves wanting to build a strong navy, respecting civilizations with a strong navy, and disliking civilizations with weak navies. His leader ability is called Thunderbolt of the North. It gives him 50% bonus Production toward and enables coastal raiding for naval melee units, and allows him to produce the Viking Longship, a unique unit that replaces the Galley.', 1)")
        # cursor.execute("insert into civ values (42, 'Nubian - Amanitore', 'Amanitores unique agenda is called City Planner. She always tries to have the greatest possible number of districts in her cities and likes civilizations that do the same. Amanitores leader ability is called Kandake of Meroë. It provides her cities with 20% bonus Production toward districts, or 40% if they have Nubian Pyramids adjacent to their City Centers.', 1)")
        # cursor.execute("insert into civ values (43, 'Persian - Cyrus', 'Cyruss unique agenda is Opportunist. He likes leaders who have declared Surprise Wars and dislikes leaders who have not. His leader ability is Fall of Babylon. It gives all of his units a +2 Movement bonus for 10 turns when he declares a Surprise War, reduces the warmongering and war weariness penalties he suffers for doing so, and removes yield penalties in cities he occupies.', 1)")
        # cursor.execute("insert into civ values (44, 'Polish - Jadwiga', 'Jadwigas unique agenda is called Saint. She focuses on building up Faith and likes civilizations that do the same. Her unique ability is called Lithuanian Union. Using a Polish Culture Bomb on another civilizations city will convert it to her religion. She also gains +4 Gold and +2 Culture and Faith from Relics, and her Holy Site districts have increased adjacency bonuses.', 1)")
        # cursor.execute("insert into civ values (45, 'Roman - Trajan', 'Trajans unique agenda is called Optimus Princeps. He tries to incorporate as much territory as possible into his empire, and he dislikes civilizations that control little territory. His leader ability is called Trajans Column. All of his cities get an additional City Center building (which will be a Monument if the game is started in the Ancient Era).', 1)")
        # cursor.execute("insert into civ values (46, 'Russian - Peter', 'Peters unique agenda is called Westernizer. He is friendly to civilizations that are ahead of him in Science and Culture Culture, and dislikes backwards civilizations that are lacking in Science Science and Culture Culture. His leader ability is The Grand Embassy. Russia can receive Science Science or Culture Culture from Trade Routes Trade Routes to more advanced civilizations.', 1)")
        # cursor.execute("insert into civ values (47, 'Scythian - Tomyris', 'Tomyris unique agenda is called Backstab Averse. She likes those willing to become her Declared Friends, but hates those who declare Surprise Wars on other civilizations, especially if declared against former friends or allies. Her leader ability is called Killer of Cyrus. All her units receive +5 Strength Combat Strength when attacking wounded units, and heal up to 30 hit points (as of the Summer 2017 Update) when they eliminate a unit.', 1)")
        # cursor.execute("insert into civ values (48, 'Spanish - Philip II', 'Philip IIs unique agenda is called Counter Reformer. He likes civilizations which follow the same religion as him and wants all his cities to follow the same religion. He hates anyone trying to spread their religion into his empire. Philips leader ability is called El Escorial. His Inquisitors can Remove Heresy one extra time, and his combat units have a bonus of +4 Strength Combat Strength against players following other religions.', 1)")
        # cursor.execute("insert into civ values (49, 'Sumerian - Gilgamesh', 'Gilgameshs unique agenda is called Ally of Enkidu. He likes civilizations who are willing to form a long term alliance, and dislikes anyone denouncing or attacking his friends or allies. His leader ability is called Adventures of Enkidu. When he declares war on someone who is at war with one of his allies, it eliminates his warmonger penalties and allows his units to share pillage rewards and combat experience with the closest allied unit within five tiles.', 1)")
        # cursor.execute("insert into civ values (1, 'Cree - Poundmaker', 'Poundmakers unique agenda is called Iron Confederacy. He tries to establish as many alliances as possible, and dislikes civilizations that dont establish alliances. His leader ability is called Favorable Terms. It allows all types of alliances to provide Shared Visibility, and rewards him with extra Food Food and Gold Gold for receiving and sending Trade Routes Trade Routes depending on the number of Camps and Pastures at the destination.', 2)")
        # cursor.execute("insert into civ values (2, 'Dutch - Wilhelmina', 'Wilhelminas unique agenda is called Billionaire. She likes civilizations that send Trade Routes Trade Routes to her cities frequently and dislikes civilizations that do not send Trade Routes Trade Routes to her cities. Her leader ability is called Radio Oranje. It provides +1 Loyalty per turn to cities that create domestic Trade Routes Trade Routes and +1 Culture Culture from international Trade Routes Trade Routes.', 2)")
        # cursor.execute("insert into civ values (3, 'Georgian - Tamar', 'Tamars unique agenda is called Narikala Fortress. She tries to fortify her cities with the most advanced Walls available and dislikes civilizations that do not keep their cities fortified. Her leader ability is called Glory of the World, Kingdom and Faith. It provides the Georgians with a 100% Faith Faith bonus for 10 turns after declaring a Protectorate War and a bonus Envoy Envoy for each one they send to a city-state that follows their majority religion.', 2)")
        # cursor.execute("insert into civ values (4, 'Indian - Chandragupta', 'Chandraguptas unique agenda is Maurya Empire. He wants to expand his empire and dislikes civilizations that have cities near his borders. His leader ability is Arthashastra. He can declare a War of Territorial Expansion after discovering Military Training, and receives +2 Moves Movement and +5 Strength Combat Strength for the first 10 turns after doing so.', 2)")
        # cursor.execute("insert into civ values (5, 'Korean - Seondeok', 'Seondeoks unique agenda is called Cheomseongdae. She focuses on increasing her empires Science output and dislikes civilizations with low Science Science output. Her leader ability is called Hwarang. It provides her cities with an established Governor +3% Culture Culture and +3% Science Science for each promotion that Governor has.', 2)")
        # cursor.execute("insert into civ values (6, 'Mapuche - Lautaro', 'Lautaros unique agenda is called Spirit of Tucapel. He tries to keep his cities Loyalty high, dislikes civilizations that lose cities due to low Loyalty and likes civilizations that earn cities through Loyalty pressure. His leader ability is called Swift Hawk. It causes enemy cities to lose 20 Loyalty for each enemy unit one of his units defeats within their borders, and 5 Loyalty for each tile one of his units pillages within their borders.', 2)")
        # cursor.execute("insert into civ values (7, 'Mongolian - Genghis Khan', 'Genghis Khans unique agenda is called Horse Lord. He tries to build the worlds strongest cavalry force, and dislikes other civilizations with strong cavalry forces. His leader ability is called Mongol Horde. It provides all cavalry units with +3 Strength Combat Strength and a chance to capture defeated cavalry units from enemies.', 2)")
        # cursor.execute("insert into civ values (8, 'Scottish - Robert the Bruce', 'Roberts unique agenda is called Flower of Scotland. He will never attack his neighbors unless they break a promise to him, and dislikes civilizations who attack their neighbors. His leader ability is called Bannockburn. He can declare a War of Liberation after discovering Defensive Tactics, and receives +100% Production Production and +2 Moves Movement for the first 10 turns after doing so.', 2)")
        # cursor.execute("insert into civ values (9, 'Zulu - Shaka', 'Shakas unique agenda is called Horn, Chest, Loins. He tries to form as many Corps and Armies as possible, and dislikes civilizations who do not form their units into Corps and Armies. His leader ability is called Amabutho. He may form Corps with Mercenaries and Armies with Nationalism, and his Corps and Armies receive a +5 bonus to their base Strength Combat Strength.', 2)")
        # cursor.execute("insert into civ values (10, 'Hungarian - Matthias Corvinus', 'Matthias Corvinuss unique agenda is Raven Banner. He often levies units from city-states and likes leaders who do the same. He dislikes leaders who shun mercenaries. His leader ability is Raven King. He gains 2 Envoy Envoys with a city-state when he levies units from it, and levied units receive +2 Moves Movement and +5 Strength Combat Strength and can be upgraded at 25% of the normal resource and Gold Gold costs.', 3)")
        # cursor.execute("insert into civ values (11, 'Māori - Kupe', 'Kupes unique agenda is Kaitiakitanga. He respects the environment and likes leaders who do the same. His leader ability is Kupes Voyage. He begins the game in an Ocean tile and receives +2 Science Science and Culture Culture per turn prior to founding his first city. He receives a free Builder and +1 Citizen Population when he founds his first city, and his Palace provides +3 Housing Housing and +1 Amenity Amenity.', 3)")
        # cursor.execute("insert into civ values (12, 'Canadian - Wilfrid Laurier', 'Wilfrid Lauriers unique agenda is Canadian Expeditionary Force. He responds to Emergencies whenever possible and dislikes leaders who refuse to participate in Emergencies. His leader ability is The Last Best West. He can build Farms on Tundra tiles (and Tundra Hills tiles after discovering Civil Engineering) and receives a 50% discount on purchase costs of Snow, Snow Hills, Tundra, and Tundra Hills tiles, which also provide a 100% bonus to the extraction rate of resources.', 3)")
        # cursor.execute("insert into civ values (13, 'Incan - Pachacuti', 'Pachacutis unique agenda is Sapa Inca. He will try to settle near Mountains whenever possible and dislikes other leaders who settle near Mountains. His leader ability is Qhapaq Ñan. His domestic Trade Routes Trade Routes provide +1 Food Food for every Mountain tile in the origin citys territory, and his Builders can build the Qhapaq Ñan improvement when he discovers Foreign Trade.', 3)")
        # cursor.execute("insert into civ values (14, 'Malian - Mansa Musa', 'Mansa Musas unique agenda is Lord of the Mines. He tries to collect as much Gold Gold as possible and dislikes leaders whose Gold Gold output is low. His leader ability is Sahel Merchants. His international Trade Routes Trade Routes receive 1 extra Gold Gold for every flat Desert tile in the origin city, and his Trade Routes Trade Route capacity permanently increases by 1 each time he enters a Golden Age.', 3)")
        # cursor.execute("insert into civ values (15, 'Swedish - Kristina', 'Kristinas unique agenda is Bibliophile. She tries to collect as many Great Works as possible and dislikes other leaders with a large number of Great Works. Her leader ability is Minerva of the North. All her buildings with three or more Great Work slots and all her wonders with two or more Great Work slots are automatically themed once their slots are filled, and she is able to build the Queens Bibliotheque in her Government Plaza.', 3)")
        # cursor.execute("insert into civ values (16, 'Ottoman - Suleiman', 'Suleimans unique agenda is Lawgiver. He tries to maintain the happiness and loyalty of his cities and dislikes leaders who have unhappy or disloyal cities or a small number of captured cities. His leader ability is Grand Vizier. It gives him access to the Janissary once he researches Gunpowder, and a unique Governor named Ibrahim with military and diplomatic abilities.', 3)")
        # cursor.execute("insert into civ values (17, 'Phoenician - Dido', 'Didos unique agenda is Sicilian Wars. She wants to settle coastal cities and dislikes leaders who have many coastal cities. Her leader ability is Founder of Carthage. It grants cities with a Cothon the unique Move Capital project, which moves the Phoenician Capital Capital to that city. She also gains +1 Trade Routes Trade Route capacity after building the Government Plaza or any Government Plaza building and a 50%  Production bonus towards Districts in the city with the Government Plaza.', 3)")
        # cursor.execute("insert into civ values (18, 'Mayan - Lady Six Sky', 'Lady Six Skys unique agenda is Solitary. She will try to keep her cities clustered around her Capital Capital, likes leaders who settle far away from her and dislikes leaders who encroach upon her borders. Her leader ability is Ix Mutal Ajaw. Within 6 tiles of her Capital Capital, all her units receive +5 Strength Combat Strength and all her cities receive a 10% yield bonus. However, all her cities that are more than 6 tiles away from her Capital Capital receive a 15% yield penalty.', 4)")
        # cursor.execute("insert into civ values (19, 'Gran Colombian - Simón Bolívar', 'Simón Bolívars unique agenda is Carabobo. He respects other leaders with many promoted units and focuses on that himself by building Encampments. He dislikes those who do not take care to build an elite army like he does. His leader ability is Campaña Admirable. He earns a Comandante General, a unique type of Great Person Great Person, when the game enters a new era.', 4)")
        # cursor.execute("insert into civ values (20, 'Ethiopian - Menelik II', 'Menelik IIs unique agenda is Ethiopian Highlands. He prefers settling cities on Hills, likes those who leave Hill-heavy areas to him, and dislikes those who also settle around Hills. His leader ability is Council of Ministers, which provides cities founded on Hills with Science Science and Culture Culture equal to 15% of their Faith Faith output, and grants all units additional Strength Combat Strength when fighting on Hills.', 4)")
        # cursor.execute("insert into civ values (21, 'Byzantine  - Basil II', 'Basil IIs unique agenda is Divine Guardian. He will focus on spreading his religion, likes those who follow his religion, and dislikes those who follow a different religion. His leader ability is Porphyrogénnētos. His heavy and light cavalry units deal full damage when attacking cities following the same religion as Byzantium. It also gives him access to the Tagma once he researches Divine Right.', 4)")
        # cursor.execute("insert into civ values (22, 'Gallic  - Ambiorix', 'Ambiorixs unique agenda is Scourge of Rome. He likes leaders with many military units and dislikes those with few military units. His leader ability is King of the Eburones. He gains Culture Culture equal to the 20% of the Production Production cost of each non-civilian unit he trains, and his melee, ranged, and anti-cavalry units (as well as recon units) receive +2 Strength Combat Strength for each adjacent military unit.', 4)")
        # cursor.execute("insert into civ values (23, 'Babylonian - Hammurabi', 'Hammurabis unique agenda is Cradle of Civilization. He tries to build every possible type of district in his cities, and respects other civilizations that do the same. He dislikes civilizations that focus heavily on one district type or do not build every type of district. His leader ability is Ninu Ilu Sirum. When each specialty district, except the Government Plaza, is constructed for the first time, he receives the lowest Production Production cost building of that district for free.', 4)")
        # cursor.execute("select * from civ")
        data = []
        for row in cursor.fetchall():
            data.append(row)
        print(data)