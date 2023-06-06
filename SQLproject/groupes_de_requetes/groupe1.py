from sqlalchemy import create_engine,text
engine =create_engine("mysql+mysqlconnector://root:@localhost:3306/sql", echo=True)
conn = engine.connect()
req1 = conn.execute(text(f"SELECT * FROM artist ORDER BY birthdate")) # 200 résultats
req2 = conn.execute(text(f"SELECT name,max_spectators,id FROM place ORDER BY max_spectators")) # 5 résultats
req3 = conn.execute(text(f"SELECT * FROM event WHERE DATE(start_time) > DATE(NOW())  ORDER BY start_time LIMIT 5")) # 5 résultats

def rendeur_de_requetes () :
    return [req1,req2,req3]