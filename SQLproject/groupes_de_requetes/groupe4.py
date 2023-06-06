from sqlalchemy import create_engine,text
engine =create_engine("mysql+mysqlconnector://root:@localhost:3306/sql", echo=True)
conn = engine.connect()
req1 = conn.execute(text(f"SELECT name, COUNT(artist_id) AS nombre FROM artist_group JOIN `group` ON (artist_group.artist_id = group.id) GROUP BY name"))
# 42 résultats
req2 = conn.execute(text(f"SELECT concert_id, COUNT(place) AS nombre FROM ticket GROUP BY concert_id"))
# 10 résultats
req3 = conn.execute(text(f"SELECT DATE(start_time) AS date, SUM(price.price) AS total FROM ticket JOIN event ON (ticket.concert_id = event.id) JOIN price WHERE price.id= ticket.price_id GROUP BY start_time;"))
# 10 résultats
conn.execute (text(f'CREATE TABLE IF NOT EXISTS `vente_par_jour` ( SELECT SUM(price.price) AS somme_p_day FROM ticket JOIN event ON (ticket.concert_id = event.id) JOIN price WHERE price.id= ticket.price_id GROUP BY start_time);'))
req4 = conn.execute(text(f"SELECT AVG(vente_par_jour.somme_p_day) AS moyenne FROM vente_par_jour;"))
# 1 résultat
req5 = conn.execute(text(f"SELECT ticket.concert_id AS concert, COUNT(ticket.spectator_id) AS nombre FROM ticket GROUP BY concert HAVING (nombre >100);"))
# 5 résultats
def rendeur_de_requetes () :
    return [req1,req2,req3,req4,req5]