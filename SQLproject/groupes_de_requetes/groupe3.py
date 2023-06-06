from sqlalchemy import create_engine,text
engine =create_engine("mysql+mysqlconnector://root:@localhost:3306/sql", echo=True)
conn = engine.connect()
req1 = conn.execute(text(f"SELECT c_p.concert_id,ev.id,ev.date,art.first_name,art.last_name FROM `concert_part` AS c_p JOIN `event` AS ev  JOIN artist AS art ON c_p.artist_id= art.id WHERE c_p.concert_id=ev.id AND c_p.status = 'approved'"))
# 6 résultats
req2 = conn.execute(text(f"SELECT c_p.concert_id,ev.id,ev.date,pl.name FROM `concert_part` AS c_p JOIN `event` AS ev  JOIN place AS pl ON ev.place_id = pl.id WHERE c_p.concert_id=ev.id AND c_p.status = 'approved'"))
# 6 résultats
req3 = conn.execute(text(f"SELECT DISTINCT GROUP_CONCAT(DISTINCT art.instrument) AS instruments,gr.name,gr.id FROM `group` AS gr JOIN artist_group AS art_g JOIN artist AS art WHERE art_g.artist_id = art.id AND art_g.group_id= gr.id GROUP BY gr.name;"))
# 60 résultats (les instruments par groupe)
req4 = conn.execute(text(f"SELECT concert_part.concert_id, GROUP_CONCAT( DISTINCT artist.first_name) AS artistes_groupe, event.start_time AS debut, place.name AS lieu FROM concert_part INNER JOIN artist INNER JOIN artist_group INNER JOIN place INNER JOIN `event` WHERE artist_group.group_id IN (SELECT artist_group.group_id FROM spectateur_artist INNER JOIN artist_group INNER JOIN `event` WHERE spectateur_artist.spectateur_id = 18694 AND spectateur_artist.artist_id = artist_group.artist_id ) AND event.place_id = place.id AND concert_part.concert_id = event.id AND artist.id IN ( SELECT artist_group.artist_id FROM artist_group WHERE artist_group.group_id IN (SELECT artist_group.group_id FROM spectateur_artist INNER JOIN artist_group INNER JOIN `event` WHERE spectateur_artist.spectateur_id = 18694 AND spectateur_artist.artist_id = artist_group.artist_id ));"))# Aucun musicien du nom de Retha Dookie, plutot Retha Dooley 
# 1 seul concert. Il s'agit du concert d'id 168 déroulé à la place Est et qui débute à 2023-04-22 04:21:24
#Les membres du groupe sont: Fred,Hubert,Kenton,Peggie,Rogelio
req5 = conn.execute(text(f"SELECT AVG(p.price) AS panier_moyen FROM ticket t JOIN price p ON t.price_id=p.id JOIN concert c ON t.concert_id = c.id;"))
# 1 résultat; Le panier moyen des ventes est : 64.994.
req6 = conn.execute(text(f"SELECT concert_part.artist_id, artist.id, concert_part.start_time, CASE 	WHEN concert_part.start_time IS null THEN 'Aucun' 	ELSE artist.id END AS personne FROM concert_part JOIN artist WHERE concert_part.status= 'approved' AND artist.id = concert_part.artist_id ORDER BY concert_part.start_time;"))
# 5 résultats (5 salles évidemment)
req7 = conn.execute(text(f"SELECT place.name AS salle, GROUP_CONCAT(DISTINCT description) AS descr FROM technical_constraints INNER JOIN technical_constraints_place ON technical_constraints.id = technical_constraints_place.technical_constraints_id INNER JOIN place ON place.id = technical_constraints_place.place_id GROUP BY name;"))
#Toutes les start_time ont pour valeur NULL; impossible de travailler avec, ceci est juste est essai de commande pour afficher l'ereur.
req8 = conn.execute(text(f"SELECT DISTINCT group.name AS groupe, place.name AS salle FROM `group` INNER JOIN artist_group ON group.id = artist_group.group_id INNER JOIN artist ON artist_group.artist_id = artist.id INNER JOIN concert_part ON artist.id = concert_part.artist_id INNER JOIN event ON concert_part.concert_id = event.id INNER JOIN place ON event.place_id = place.id;"))
# 13 résultats visibles sur l'interface.
def rendeur_de_requetes () :
    return [req1,req2,req3,req4,req5,req6,req7,req8]