from sqlalchemy import create_engine,text
engine =create_engine("mysql+mysqlconnector://root:@localhost:3306/sql", echo=True)
conn = engine.connect()
req1 = conn.execute(text(f"SELECT artist.first_name AS nom,artist.last_name AS prenom,artist.instrument AS travail FROM artist UNION SELECT staff.first_name  AS nom, staff.last_name AS prenom,role.role_name AS travail FROM role JOIN staff WHERE role.person_id= staff.id;"))
# 219 résulats (les doublons sont considérés vu que les activités diffèrent trop à ce niveau)



#Plusieurs personnes ont divers tâches en bénévolat; ils seront cités qu'une fois (pas de doublons cette fois)
req2 = conn.execute(text(f"SELECT artist.first_name AS nom,artist.last_name AS prenom,artist.instrument AS travail, CASE WHEN artist.id > 0 THEN 'Artiste' END AS roles FROM artist UNION SELECT staff.first_name  AS nom, staff.last_name AS prenom,role.role_name AS travail, CASE WHEN staff.id > 0 THEN 'Bénévole' END AS roles FROM role JOIN staff WHERE role.person_id= staff.id GROUP BY nom,prenom ORDER BY nom;"))
# 210 résultats
def rendeur_de_requetes () :
    return [req1,req2]