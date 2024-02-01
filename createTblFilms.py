from connectFilms import *

dbCursor.execute(
    """
CREATE TABLE IF NOT EXISTS "tblFilms" (
	"filmID"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT,
	"yearReleased"	INTEGRER,
    "rating"	TEXT,
    "duration"	INTEGRER,
	"Genre"	TEXT,
	PRIMARY KEY("filmID" AUTOINCREMENT)
)"""
)
