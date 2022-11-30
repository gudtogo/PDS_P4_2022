from .botObjects import Module, SubModule, Question
import random
DEBUGFN = "[tutorialData]"
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


# * <------------------------------- Trivia first mode	 ------------------------------->
m1 = Module(name="Trivia", umbral=13)
# * <----------------------- Submodule Variables ----------------------->
m2 = SubModule(name="Trivia", alt_questions=[])
# ? <-------------------- Questions -------------------->
qalternatives = ["Oliver Stone","Francis Ford Coppola","Stanley Kubrick","Michael Cimino"]
m2.alt_questions.append(Question(question="Who wrote and directed the 1986 film Platoon?",
                                      answer=0,
                                      alternatives=qalternatives))
                                    
qalternatives = ["Homo Sapiens","Homo Ergaster","Homo Erectus","Homo Neanderthalensis"]
m2.alt_questions.append(Question(question="What is the scientific name for modern day humans?",
                                               answer=0,
                                               alternatives=qalternatives))

qalternatives = ["Castor","Daedalus","Jason","Odysseus"]
m2.alt_questions.append(Question(question="Who in Greek mythology, who led the Argonauts in search of the Golden Fleece?",
                                      answer=2,
                                      alternatives=qalternatives))
                                    
qalternatives = ["Wangan Midnight","Kino no Tabi","Cowboy Bebop", "Initial D"]
m2.alt_questions.append(Question(question="Which anime heavily features music from the genre 'Eurobeat'?",
                                               answer=3,
                                               alternatives=qalternatives))

qalternatives = ["Wheat","Bread","Milk","Egg"]
m2.alt_questions.append(Question(question="What ingredient is NOT used to craft a cake in Minecraft?",
                                      answer=1,
                                      alternatives=qalternatives))
                                    
qalternatives = ["Activision","Konami","Electronic Arts","Harmonix"]
m2.alt_questions.append(Question(question="What company develops the Rock Band series of rhythm games?",
                                               answer=3,
                                               alternatives=qalternatives))

qalternatives = ["Tardar Sauce","Sauce","Minnie","Broccoli"]
m2.alt_questions.append(Question(question="What is Grumpy Cat's real name?",
                                      answer=0,
                                      alternatives=qalternatives))
                                    
qalternatives = ["Gabriel Garcia Marquez","Jesus Quintero","Juan Joya Borga","Ernesto Guevara"]
m2.alt_questions.append(Question(question="What is the real name of the famous spanish humorist, El Risitas?",
                                               answer=2,
                                               alternatives=qalternatives))

qalternatives = ["Black","Brown","White","Yellow"]
m2.alt_questions.append(Question(question="What colour is the female blackbird?",
                                      answer=1,
                                      alternatives=qalternatives))
                                    
qalternatives = ["Region","River","Country","City"]
m2.alt_questions.append(Question(question="What is Laos?",
                                               answer=2,
                                               alternatives=qalternatives))

qalternatives = ["Ubisoft","Pixeltail Games","Valve","Electronic Arts"]
m2.alt_questions.append(Question(question="Who created the digital distribution platform Steam?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["107","108","93","96"]
m2.alt_questions.append(Question(question="How many people can you recruit in the game Suikoden in a single playthrough?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Vermont","Rhode Island ","Maine","Massachusetts"]
m2.alt_questions.append(Question(question="Which state of the United States is the smallest?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Oliver Stone","Francis Ford Coppola","Stanley Kubrick","Michael Cimino"]
m2.alt_questions.append(Question(question="Who wrote and directed the 1986 film 'Platoon'?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["GoldSrc","Quake","Source","Unreal"]
m2.alt_questions.append(Question(question="What engine did the original 'Half-Life' run on?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["2007","2009","2008","2006"]
m2.alt_questions.append(Question(question="In what year did 'The Big Bang Theory' debut on CBS?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Magical Mystery Tour","Revolver","Abbey Road","The Wall"]
m2.alt_questions.append(Question(question="Which of these is NOT an album released by The Beatles?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Oxygen","Hydrogen","Nitrogen","Carbon"]
m2.alt_questions.append(Question(question="This element, when overcome with extreme heat and pressure, creates diamonds.",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Jupiter","Mercury","Mars","Venus"]
m2.alt_questions.append(Question(question="What is the hottest planet in the Solar System?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Botswana","Togo","Gabon","Mozambique"]
m2.alt_questions.append(Question(question="What African country has Portuguese as its official language?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Using Alchemy For Crime ","Transmuting Lead Into Gold","Preforming Without A Permit","Human Transmutation "]
m2.alt_questions.append(Question(question="In the anime series 'Full Metal Alchemist', what do Alchemists consider the greatest taboo?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Femur","Patella","Foramen Magnum","Scapula"]
m2.alt_questions.append(Question(question="What is the scientific name of the knee cap?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["2003","2011","2007","2004"]
m2.alt_questions.append(Question(question="When was Steam first released?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Felix Miller","Sean Parker","Michael Breidenbruecker","Daniel Ek"]
m2.alt_questions.append(Question(question="Who is a co-founder of music streaming service Spotify?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["November 12, 2004","December 24, 2004","November 13, 2004","December 13, 2004"]
m2.alt_questions.append(Question(question="When was 'Garry's Mod' released?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["200","203","206","209"]
m2.alt_questions.append(Question(question="How many bones are in the human body?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Schwann cell","Node of Ranvier","Myelin sheath","Islets of Langerhans"]
m2.alt_questions.append(Question(question="Which of these is NOT a part of the structure of a typical neuron?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["16 - 0","7 - 1","0 - 1","3 - 4"]
m2.alt_questions.append(Question(question="What was the final score of the Germany vs. Brazil 2014 FIFA World Cup match?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Lake Michigan","Caspian Sea","Lake Superior ","Lake Huron"]
m2.alt_questions.append(Question(question="Which is the largest freshwater lake in the world?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["The Bourne Legacy","L&eacute;on: The Professional","Ip Man 2","Victoria"]
m2.alt_questions.append(Question(question="Which one of these action movies are shot entirely in one take?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Singing into a Microphone","Playing a Piano","Using a Composer Software","Listened to birds at the park"]
m2.alt_questions.append(Question(question="According to Toby Fox, what was the method to creating the initial tune for Megalovania?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["William Golding","Stephen King","Hunter Fox","F. Scott Fitzgerald"]
m2.alt_questions.append(Question(question="Who was the author of the 1954 novel, 'Lord of the Flies'?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Iran","Sudan","Indonesia","Saudi Arabia"]
m2.alt_questions.append(Question(question="What is the most populous Muslim-majority nation in 2010?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["4.5 Billion Years","2.5 Billion Years","5.5 Billion Years","3.5 Billion Years"]
m2.alt_questions.append(Question(question="About how old is Earth?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["JoJo's Bizarre Adventure","Golgo 13","Detective Conan","One Piece"]
m2.alt_questions.append(Question(question="Which of the following manga have the most tankouban volumes?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Max Verstappen","Lewis Hamilton","Kimi Raikkonen","Nico Rosberg"]
m2.alt_questions.append(Question(question="Who won the 2016 Formula 1 World Driver's Championship?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["RAID 1","RAID 10","RAID 0","RAID 5"]
m2.alt_questions.append(Question(question="Which RAID array type is associated with data mirroring?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["1975","1983","1969","1971"]
m2.alt_questions.append(Question(question="In what year did Clint Eastwood star as Inspector Harry Callahan in the film 'Dirty Harry'?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["At Church","At 742 Evergreen Terrace","At Summer Camp","At High School"]
m2.alt_questions.append(Question(question="In 'The Simpsons', where did Homer and Marge first meet?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["North America","Asia","South America","Africa"]
m2.alt_questions.append(Question(question="Where is the 'Sonoran Desert' located?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Paul McCartney","John Lennon","George Harrison","Ringo Starr"]
m2.alt_questions.append(Question(question="Which member of 'The Beatles' narrated episodes of 'Thomas the Tank Engine'?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Lucio","Reinhardt","Mercy","Sombra"]
m2.alt_questions.append(Question(question="In 'Overwatch', which hero is able to wallride?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Nuketown","Shangri-La","Revelations","Origins"]
m2.alt_questions.append(Question(question="Which 'Call Of Duty: Zombies' map introduced the 'Staffs Of The Ancients'?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Jimmy Page","David Gilmour","Eric Clapton","Mark Knopfler"]
m2.alt_questions.append(Question(question="Pete Townshend collaborated with which famous guitarist for an event at Brixton Academy in 1985?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["2005","2015","2007","2020"]
m2.alt_questions.append(Question(question="In what year does Jurassic World open in the 'Jurassic Park' universe?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Hallowed Relic","Sacred Gear","Blessed Artifact","Imperial Arm"]
m2.alt_questions.append(Question(question="In 'Highschool DxD', what is the name of the item some humans are born with?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Horsefly","Golden Eagle","Cheetah","Peregrine Falcon"]
m2.alt_questions.append(Question(question="What is the fastest animal?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Chitin","Keratin","Bone","Calcium"]
m2.alt_questions.append(Question(question="What are human nails made of?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["xebec","Trigger","Pierrot","Bones"]
m2.alt_questions.append(Question(question="What studio animated Fullmetal Alchemist?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Italy","Austria","Germany","France"]
m2.alt_questions.append(Question(question="From which country does the piano originate?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Bandit","Lucky","Rocky","Max"]
m2.alt_questions.append(Question(question="What was the name of Jonny's pet dog in The Adventures of Jonny Quest?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["North Manchester Express","New Metro Entertainment","Next Musical Enterprise","New Musical Express"]
m2.alt_questions.append(Question(question="Which music publication is often abbreviated to NME?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Family Guy","South Park","Rick &amp; Morty","American Dad"]
m2.alt_questions.append(Question(question="What TV show is about a grandfather dragging his grandson around on adventures?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Stoke City","Watford","Leicester City","Tottenham Hotspur"]
m2.alt_questions.append(Question(question="Who won the premier league title in the 2015-2016 season following a fairy tale run?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Oops!... I Did It Again","(You Drive Me) Crazy","...Baby One More Time","Toxic"]
m2.alt_questions.append(Question(question="What was Britney Spears' debut single?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Hirohiko Araki","Hiro Mashima","Keiichi Hikami","Shin Yamamoto"]
m2.alt_questions.append(Question(question="Who was the Author of the manga Monster Hunter Orage?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Israel and Jordan","Egypt and Sudan","Chad and Libya","Iraq and Saudi Arabia"]
m2.alt_questions.append(Question(question="Bir Tawil, an uninhabited track of land claimed by no country, is located along the border of which two countries?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Bromine","Rubidium","Tin","Antimony"]
m2.alt_questions.append(Question(question="Which of these Elements is a metalloid?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["288 GTO","F40","Testarossa","Enzo Ferrari"]
m2.alt_questions.append(Question(question="Which of these cars is NOT considered one of the 5 Modern Supercars by Ferrari?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Matthew Lopez","Anthony Neilson","Tony Kusher","Tom Stoppard"]
m2.alt_questions.append(Question(question="Who wrote the play 'Angels in America'?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Data","Address","Control","Instruction"]
m2.alt_questions.append(Question(question="The Harvard architecture for micro-controllers added which additional bus?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Coldplay - Midnight","Marvin Gaye - Sexual Healing","a-ha - Take On Me","Ed Sheeran - I See Fire"]
m2.alt_questions.append(Question(question="Electronic music producer Kygo's popularity skyrocketed after a certain remix. Which song did he remix?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Bird","Insect","Fish","Toad"]
m2.alt_questions.append(Question(question="What type of animal is a natterjack?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["York","Stuart","Tudor","Lancaster"]
m2.alt_questions.append(Question(question="King Henry VIII was the second monarch of which European royal house?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Helium","Nitrogen","Carbon","Hydrogen"]
m2.alt_questions.append(Question(question="Along with Oxygen, which element is primarily responsible for the sky appearing blue?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Mark Knopfler","Jeff Beck","Jimmy Page","Eric Clapton"]
m2.alt_questions.append(Question(question="Which English guitarist has the nickname 'Slowhand'?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Mark Zuckerberg","Christopher Poole","Catie Wayne","Allison Harvard"]
m2.alt_questions.append(Question(question="What is the real name of 'moot', founder of the imageboard 4chan?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Hard Disk Drive","Motherboard","Central Processing Unit","Random Access Memory"]
m2.alt_questions.append(Question(question="Which computer hardware device provides an interface for all other connected devices to communicate?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["2","3","5","13"]
m2.alt_questions.append(Question(question="In 'Undertale', how many main endings are there?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["South Korea","China","Japan","Vietnam"]
m2.alt_questions.append(Question(question="Which country is singer Kyary Pamyu Pamyu from?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["1","3","6","4"]
m2.alt_questions.append(Question(question="How many countries border Kyrgyzstan?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Pidgey","Caterpie","Pikachu","Charmander"]
m2.alt_questions.append(Question(question="What was Ash Ketchum's second Pokemon?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["December 13, 1931","July 18, 1940","April 17, 1938","January 8, 1935"]
m2.alt_questions.append(Question(question="When was Elvis Presley born?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["23","443","80","53"]
m2.alt_questions.append(Question(question="What port does HTTP run on?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["5","2","3","4"]
m2.alt_questions.append(Question(question="How many times do you fight the Imprisoned in The Legend of Zelda: Skyward Sword?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Blast Fencer","Bastion Warrior","Partisan Eagle","Winged Viper"]
m2.alt_questions.append(Question(question="In Xenoblade Chronicles X, which class has a sniper rifle as it's primary weapon?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = [" Anno 1701","Anno 1404","Anno 2070","Anno 2205"]
m2.alt_questions.append(Question(question="Which of the following games in the Anno series introduced the 'Eco Balance' gameplay mechanic?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Miley Cyrus","Kanye West","Donald Trump","Leonardo DiCaprio"]
m2.alt_questions.append(Question(question="Which celebrity announced his presidency in 2015?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Toronto","Seattle","Los Angles","Vancouver"]
m2.alt_questions.append(Question(question="The Space Needle is located in which city?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["AMD","Ageia","NovodeX","Nvidia"]
m2.alt_questions.append(Question(question="Who is the original author of the realtime physics engine called PhysX?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["'So sing your song until you're home'","'So start a fire in their cold stone'","'So melt your headaches call it home'","'So let them know they're on their own'"]
m2.alt_questions.append(Question(question="In the Panic! At the Disco's song 'Nothern Downpour', which lyric follows 'I know the world's a broken bone'.",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Cicero","Lucien Lachance","Archimedes","Astrid"]
m2.alt_questions.append(Question(question="In The Elder Scrolls V: Skyrim, who is the jester in the dark brotherhood?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Football","Baseball","American Football","Basketball"]
m2.alt_questions.append(Question(question="What sport is being played in the Anime Eyeshield 21?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Gaming Processor Unit","Graphical Proprietary Unit","Graphite Producing Unit","Graphics Processing Unit"]
m2.alt_questions.append(Question(question="What does the term GPU stand for?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["RTS (Real Time Strategy)","TBS (Turn Based Strategy)","MMO (Massively Multiplayer Online)","RPG (Role Playing Game)"]
m2.alt_questions.append(Question(question="What video game genre were the original Warcraft games?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Robbie Williams","Mike Posner","Harry Styles","Avicii"]
m2.alt_questions.append(Question(question="Who performed 'I Took A Pill In Ibiza'?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["70","60","65","55"]
m2.alt_questions.append(Question(question="What minimum level in the Defence skill is needed to equip Dragon Armour in the MMO RuneScape?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Josip Broz Tito","Karadjordje Petrovic","Milos Obilic","Aleskandar Petrovic"]
m2.alt_questions.append(Question(question="Who was the leader of the Communist Party of Yugoslavia ?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Nolan North","John Patrick Lowrie","J.K. Simmons","Christopher Lloyd"]
m2.alt_questions.append(Question(question="Aperture Science CEO Cave Johnson is voiced by which American actor?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = [" Tracker","Scribe","Assassin","Apprentice"]
m2.alt_questions.append(Question(question="Akatsuki's subclass in 'Log Horizon' is what?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Excalisore","Excalipoor","Excalibore","Excalisnore"]
m2.alt_questions.append(Question(question="In 'Final Fantasy VI', what is the name of (summoned) Gilgamesh's weakest attack?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Gohan","Bardock","Vegeta","Raditz"]
m2.alt_questions.append(Question(question="In the 'Dragon Ball' franchise, what is the name of Goku's brother?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Petricub","Spookit","Trictus","Pyromantle"]
m2.alt_questions.append(Question(question="In 'Starbound', according to the asset files, the description of the 'Erchius Ghost' is the same as which other assets?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Ray Gun","R115 Resonator","Scavenger","GKZ-45 Mk3"]
m2.alt_questions.append(Question(question="Which of these is not a wonder weapon in 'Call Of Duty: Zombies'?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Vistula-Oder Offensive","Operation Bagration","Leningrad-Novgorod Offensive","Crimean Offensive"]
m2.alt_questions.append(Question(question="Which of the following was not one of Joseph Stalin's ten blows during World War II?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Asus","Dell","Hewlett-Packard","Toshiba"]
m2.alt_questions.append(Question(question="Computer manufacturer Compaq was acquired for $25 billion dollars in 2002 by which company?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Radiohead","Bon Jovi","Coldplay","U2"]
m2.alt_questions.append(Question(question="Which of these bands was a featuring artist in Compton rapper Kendrick Lamar's 2017 album, 'DAMN.'?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Ljubljana","Maribor","Trbovlje","Velenje"]
m2.alt_questions.append(Question(question="What is the capital city of Slovenia?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Salvador Dali","Pablo Picasso","Andy Warhol","Vincent van Gogh"]
m2.alt_questions.append(Question(question="Who designed the Chupa Chups logo?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["A Dance with Dragons","A Storm of Swords","A Clash of Kings","A Feast for Crows"]
m2.alt_questions.append(Question(question="What's the second book in George R. R. Martin's 'A Song of Ice and Fire' series?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Light Access Node","Land Address Navigation","Long Antenna Node","Local Area Network"]
m2.alt_questions.append(Question(question="In computing, what does LAN stand for?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Screwball","Slowball","Fastball","Palmball"]
m2.alt_questions.append(Question(question="What is the most common type of pitch thrown by pitchers in baseball?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Family Guy","American Dad","South Park","Rick &amp; Morty"]
m2.alt_questions.append(Question(question="What TV show is about a grandfather dragging his grandson around on adventures?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Grand Theft Auto III","Grand Theft Auto II","Grand Theft Auto Vice City","Grand Theft Auto"]
m2.alt_questions.append(Question(question="Which one of the first four titles of the 'Grand Theft Auto' franchise started the series of iconic image grid cover arts?",
                                      answer=0,
                                      alternatives=qalternatives))

qalternatives = ["Manager of the Crown Estate","First Lord of the Treasury","Her Majesty's Loyal Opposition","Duke of Cambridge"]
m2.alt_questions.append(Question(question="What is the full title of the Prime Minister of the UK?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["New York Rangers","Boston Bruins","Montreal Canadiens","Toronto Maple Leafs"]
m2.alt_questions.append(Question(question="Who won the 2011 Stanley Cup?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Keiichi Hikami","Shin Yamamoto","Hiro Mashima","Hirohiko Araki"]
m2.alt_questions.append(Question(question="Who was the Author of the manga Monster Hunter Orage?",
                                      answer=2,
                                      alternatives=qalternatives))

qalternatives = ["Who Can It Be Now?","Basket Case","Dr. Heckyll and Mr. Jive","Be Good Johnny"]
m2.alt_questions.append(Question(question="Which of these are NOT a Men at Work song?",
                                      answer=1,
                                      alternatives=qalternatives))

qalternatives = ["Wilhelm Keitel","Gerd von Rundstadt","Heinz Guderian ","Erwin Rommel"]
m2.alt_questions.append(Question(question="Which Nazi General was known as the 'Desert Fox'?",
                                      answer=3,
                                      alternatives=qalternatives))

qalternatives = ["Yoko Ono","LiSA","Kyoko Ito","Kyary Pamyu Pamyu"]
m2.alt_questions.append(Question(question="What is the name of Rivers Cuomo's wife?",
                                      answer=2,
                                      alternatives=qalternatives))

trivia = [m2]

def retrieveQuestions():
    """
    Retrieves a set of questions based on their type `[Alternative|Code]` and difficulty
    the last is considered only when `questionDifficulty` is given.
    Parameters
    ----------
    module : `int`
            module index from the 'tutorial' list that contains all the data.
    subModule : `int`
            subumodule index from the submodules list of the given module.
    Returns
    -------
    `Bool,List`
            `True,Question` if successfull, `False,None` otherwise.
    """
    DEBUGMN = "[retrieveQuestions]"
    module = 0
    subModule = 0
    prCyan(DEBUGFN+DEBUGMN +
               F" looking in module:{module} in submodule:{subModule} for an alternative question")
    wantedQuestions = trivia[module].alt_questions
    if len(wantedQuestions) == 0:
        prRed(DEBUGFN+DEBUGMN + " No questions found...")
        return False, None
    else:
        prGreen(DEBUGFN+DEBUGMN + " Success questions found " + str(wantedQuestions[0].question))
        
    random.shuffle(wantedQuestions)
    return True, wantedQuestions