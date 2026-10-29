# Contenido de la demo Hotel Rúa (Salamanca) (es/ca/en/fr). Hechos de hotelrua.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble','Doble superior','Familiar'],
'ca':['Doble','Doble superior','Familiar'],
'en':['Double','Superior double','Family room'],
'fr':['Double','Double supérieure','Chambre familiale']}
RD={
'es':['Hasta 2 adultos y 1 niño, con cama doble o dos camas, caja fuerte, aire acondicionado, bañera y wifi gratuito.','Hasta 2 personas, con balcón a la fachada principal o trasera, con vistas a las cúpulas de las Catedrales según disponibilidad.','Hasta 4 personas, con balcón a la fachada principal y diferentes composiciones de camas.'],
'ca':['Fins a 2 adults i 1 nen, amb llit doble o dos llits, caixa forta, aire condicionat, banyera i wifi gratuïta.','Fins a 2 persones, amb balcó a la façana principal o posterior, amb vistes a les cúpules de les Catedrals segons disponibilitat.','Fins a 4 persones, amb balcó a la façana principal i diferents composicions de llits.'],
'en':['Up to 2 adults and 1 child, with a double bed or two beds, safe, air conditioning, bathtub and free wifi.','Up to 2 guests, with a balcony on the main or rear façade, with views of the Cathedral domes depending on availability.','Up to 4 guests, with a balcony on the main façade and different bed arrangements.'],
'fr':['Jusqu\'à 2 adultes et 1 enfant, avec lit double ou deux lits, coffre-fort, climatisation, baignoire et wifi gratuit.','Jusqu\'à 2 personnes, avec balcon sur la façade principale ou arrière, avec vue sur les coupoles des Cathédrales selon disponibilité.','Jusqu\'à 4 personnes, avec balcon sur la façade principale et différentes compositions de lits.']}
ART={
'hero':('arches',9901,['#e9dfcc','#d3b98c','#9a7a3f','#2f5468','#1b3342']),
'intro':('columns',9902,['#ece3d0','#f4ecda','#b8924a','#3c6a82','#1b3342']),
'r1':('arches',9911,['#eadfc9','#d5bb8c','#97763a','#2d5166','#193040']),
'r2':('columns',9912,['#e8dfca','#f3ebd7','#b58f45','#3a647c','#1d3646']),
'r3':('skyline',9913,['#2f4558','#e8935f','#fbd9a0','#2e4457','#213443','#162531']),
'g1':('arches',9921,['#ebe0cb','#d6bd90','#99783d','#2e5368','#1a3241']),
'g2':('skyline',9922,['#3a4a68','#e8935f','#fbd9a0','#394967','#2a3955','#1b2536']),
'g3':('columns',9923,['#e9dfc9','#f4ecd8','#b8924a','#3e6c84','#1e3a4a']),
'g4':('hills',9924,['#e6e6d1','#f3e5c3','#f6cf8a','#a9c19e','#80a085','#587767']),
'g5':('arches',9925,['#eae0cb','#d4ba8d','#98773c','#2c5065','#193040']),
'g6':('skyline',9926,['#33456a','#e48a5f','#f9d19b','#2f4260','#223249','#16222f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Rúa · Hotel de 4 estrellas en un edificio del siglo XIX, Salamanca',see_rooms='Ver habitaciones',hero_k='Salamanca · Calle Sánchez Barbero',hero_t='Historia viva en el corazón de Salamanca',hero_s='Diecinueve habitaciones amplias en un edificio de finales del siglo XIX, en el casco histórico.',
 intro_t='Un edificio con memoria',intro_p1='El Hotel Rúa ocupa un edificio de finales del siglo XIX en la Calle Sánchez Barbero 11, con 19 habitaciones.',
 intro_p2='Tiene desayuno bufé, ascensor y consigna, y un parking concertado de pago a pocos minutos. Para reservar, contacta con el hotel por teléfono o correo.',
 stats=['4 estrellas','19 habitaciones','Edificio del siglo XIX','Parking concertado'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Tres de los tipos de habitación del hotel.',
 svcs=['Desayuno bufé','Ascensor','Consigna','Caja fuerte','Wifi gratuito','Aire acondicionado','Smart TV','Información turística'],
 loc_p='Calle Sánchez Barbero 11, 37002 Salamanca.',
 chips=['¿Cuántas habitaciones tiene?','¿Hay parking?','¿Dónde está?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Rúa · Hotel de 4 estrelles en un edifici del segle XIX, Salamanca',see_rooms='Veure habitacions',hero_k='Salamanca · Calle Sánchez Barbero',hero_t='Història viva al cor de Salamanca',hero_s='Dinou habitacions àmplies en un edifici de finals del segle XIX, al nucli històric.',
 intro_t='Un edifici amb memòria',intro_p1='L\'Hotel Rúa ocupa un edifici de finals del segle XIX a la Calle Sánchez Barbero 11, amb 19 habitacions.',
 intro_p2='Té esmorzar bufet, ascensor i consigna, i un pàrquing concertat de pagament a pocs minuts. Per reservar, contacta amb l\'hotel per telèfon o correu.',
 stats=['4 estrelles','19 habitacions','Edifici del segle XIX','Pàrquing concertat'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Tres dels tipus d\'habitació de l\'hotel.',
 svcs=['Esmorzar bufet','Ascensor','Consigna','Caixa forta','Wifi gratuïta','Aire condicionat','Smart TV','Informació turística'],
 loc_p='Calle Sánchez Barbero 11, 37002 Salamanca.',
 chips=['Quantes habitacions té?','Hi ha pàrquing?','On és?','Com es reserva?']),
'en':dict(title='Hotel Rúa · 4-star hotel in a 19th-century building, Salamanca',see_rooms='See the rooms',hero_k='Salamanca · Calle Sánchez Barbero',hero_t='Living history in the heart of Salamanca',hero_s='Nineteen spacious rooms in a late 19th-century building in the historic centre.',
 intro_t='A building with memory',intro_p1='Hotel Rúa occupies a late 19th-century building at Calle Sánchez Barbero 11, with 19 rooms.',
 intro_p2='It has a buffet breakfast, a lift and luggage storage, and a contracted paid car park a few minutes away. To book, contact the hotel by phone or email.',
 stats=['4 stars','19 rooms','19th-century building','Contracted car park'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Three of the hotel\'s room types.',
 svcs=['Buffet breakfast','Lift','Luggage storage','Safe','Free wifi','Air conditioning','Smart TV','Tourist information'],
 loc_p='Calle Sánchez Barbero 11, 37002 Salamanca.',
 chips=['How many rooms does it have?','Is there parking?','Where is it?','How do I book?']),
'fr':dict(title='Hotel Rúa · Hôtel 4 étoiles dans un bâtiment du XIXe siècle, Salamanque',see_rooms='Voir les chambres',hero_k='Salamanque · Calle Sánchez Barbero',hero_t='Une histoire vivante au cœur de Salamanque',hero_s='Dix-neuf chambres spacieuses dans un bâtiment de la fin du XIXe siècle, dans le centre historique.',
 intro_t='Un bâtiment plein de mémoire',intro_p1='L\'Hotel Rúa occupe un bâtiment de la fin du XIXe siècle, Calle Sánchez Barbero 11, avec 19 chambres.',
 intro_p2='Il propose petit-déjeuner buffet, ascenseur et consigne, et un parking conventionné payant à quelques minutes. Pour réserver, contactez l\'hôtel par téléphone ou e-mail.',
 stats=['4 étoiles','19 chambres','Bâtiment du XIXe siècle','Parking conventionné'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Trois des types de chambre de l\'hôtel.',
 svcs=['Petit-déjeuner buffet','Ascenseur','Consigne','Coffre-fort','Wifi gratuit','Climatisation','Smart TV','Information touristique'],
 loc_p='Calle Sánchez Barbero 11, 37002 Salamanque.',
 chips=['Combien de chambres a-t-il ?','Y a-t-il un parking ?','Où est-il ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='reservas@hotelrua.com')
D=dict(name='Hotel Rúa',ac='#1f3a4d',ac2='#c28a3a',ac2_a11y='#7a5410',book=BOOK,around=[],foot=FOOT,
 address='Calle Sánchez Barbero 11 · 37002 Salamanca',phones=['923 27 22 72'],emails=['reservas@hotelrua.com'],maps='Hotel Rúa, Calle Sánchez Barbero 11, Salamanca',t=T)
META=dict(repo='demo-hotel-rua-salamanca',name='Hotel Rúa',legal_name='Promociones Palanama SL',registry_ids=['NIF B37450871'],
 url='https://hotelrua.com/',domain='hotelrua.com',municipality='Salamanca',province='Salamanca',sector='hotel de 4 estrellas en un edificio del siglo XIX',
 read_at='2026-10-29T05:47:00+01:00',created_at='2026-10-29T05:49:00+01:00',built_at='2026-10-29T05:50:00+01:00',audit_date='2026-10-29T05:49:00+01:00',
 rating=dict(value=4.1,coincide=['telefono','web'],date='2026-10-29T04:53:32+01:00',url='https://www.google.com/maps/place/Hotel+R%C3%BAa/@40.9637657,-5.6645044,17z/data=!4m9!3m8!1s0xd3f2611e554319b:0x37f9fb7c0e8f3941!5m2!4m1!1i2!8m2!3d40.9637657!4d-5.6645044!16s%2Fg%2F11gf97fpfr'),
 book=dict(mode='mail',email='reservas@hotelrua.com',note='La web del negocio tiene su propio motor de reservas cuyo enlace no se verifica; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='no aplica: hotel con precedente en demos de esta tanda')
QS={
'es':[('¿Cuántas habitaciones tiene?','K01'),('¿Qué equipamiento tienen las habitaciones?','K02'),('¿Hay desayuno?','K03'),('¿Hay parking?','K04'),('¿Dónde está el hotel?','K05'),('¿Qué historia tiene el edificio?','K06'),('¿Admiten grupos?','K07'),('¿Cómo reservo?','K08'),('¿Cuál es el teléfono?','K09'),('¿Quién es el titular?','K10'),('¿Qué hay para visitar en Salamanca?','K11'),('¿Admiten mascotas?',None),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K08'),('¿Tienen suites?',None),('¿Hay piscina?',None)],
'ca':[('Quantes habitacions té?','K01'),('Quin equipament tenen les habitacions?','K02'),('Hi ha esmorzar?','K03'),('Hi ha pàrquing?','K04'),('On és l\'hotel?','K05'),('Quina història té l\'edifici?','K06'),('Admeteu grups?','K07'),('Com reservo?','K08'),('Quin és el telèfon?','K09'),('Qui és el titular?','K10'),('Què hi ha per visitar a Salamanca?','K11'),('Admeteu mascotes?',None),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K08'),('Teniu suites?',None),('Hi ha piscina?',None)],
'en':[('How many rooms does it have?','K01'),('What equipment do the rooms have?','K02'),('Is there breakfast?','K03'),('Is there parking?','K04'),('Where is the hotel?','K05'),('What history does the building have?','K06'),('Do you accept groups?','K07'),('How do I book?','K08'),('What is the phone number?','K09'),('Who is the owner?','K10'),('What is there to visit in Salamanca?','K11'),('Are pets allowed?',None),('How much is a night?',None),('Confirm that there is a free room tomorrow','K08'),('Do you have suites?',None),('Is there a swimming pool?',None)],
'fr':[('Combien de chambres a-t-il ?','K01'),('Quel équipement ont les chambres ?','K02'),('Y a-t-il un petit-déjeuner ?','K03'),('Y a-t-il un parking ?','K04'),('Où est l\'hôtel ?','K05'),('Quelle histoire a le bâtiment ?','K06'),('Acceptez-vous les groupes ?','K07'),('Comment réserver ?','K08'),('Quel est le téléphone ?','K09'),('Qui est le titulaire ?','K10'),('Que visiter à Salamanque ?','K11'),('Les animaux sont-ils admis ?',None),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K08'),('Avez-vous des suites ?',None),('Y a-t-il une piscine ?',None)]}
