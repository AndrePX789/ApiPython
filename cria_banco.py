import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY, nome text, avaliacao real, diaria real, cidade text)"

cria_hotel = "INSERT INTO hoteis VALUES ('casabranca', 'Hotel Casa Branca', 4.5, 250.0, 'Curitiba')"

cursor.execute(cria_tabela)
cursor.execute(cria_hotel)

connection.commit()
connection.close()