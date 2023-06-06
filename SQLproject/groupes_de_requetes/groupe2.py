from sqlalchemy import create_engine,text
engine =create_engine("mysql+mysqlconnector://root:@localhost:3306/sql", echo=True)
conn = engine.connect()

req1 = conn.execute(text(f"SELECT first_name,last_name,country FROM spectateur WHERE country = 'Croatia' ")) #7 résultats
req2 = conn.execute(text(f"SELECT first_name,last_name,instrument FROM artist WHERE instrument <> 'song' AND ( YEAR (birthdate) BETWEEN {1970} AND {1990})"))#Bizarement c'est seulement la fausse écriture qui marche (concernant les variables dans flask)
#84 résultats
req3 = conn.execute(text(f"SELECT first_name,last_name,birthdate FROM spectateur WHERE last_name LIKE 'B%' AND YEAR(birthdate) < {1970}"))
#15 résultats
req4 = conn.execute(text(f"SELECT id,date FROM event WHERE discr = 'concert' ORDER BY date,start_time"))
#10 résultats
def rendeur_de_requetes () :
    return [req1,req2,req3,req4]