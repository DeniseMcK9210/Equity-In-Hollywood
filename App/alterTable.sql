PRAGMA foreign_keys=off;

BEGIN TRANSACTION;

ALTER TABLE bechdel RENAME TO bechdel_final;

CREATE TABLE bechdel
("imdbid" integer NOT NULL,
 "bechdel_rating" integer NOT NULL,
 "title" text NOT NULL,
 "year" integer NOT NULL,
 "binary" integer NOT NULL,
 "budget_2013" integer NOT NULL,
 "domgross_2013" integer NOT NULL,
 "intgross_2013" integer NOT NULL,
 "genres" text NOT NULL,
 "A" text NOT NULL,
 "B" text NOT NULL,
 "C" text NOT NULL,
 "averageRating" real NOT NULL,
 "numVotes" integer NOT NULL);

INSERT INTO bechdel ("imdbid", "bechdel_rating", "title", "year", "binary", "budget_2013", "domgross_2013", "intgross_2013", "genres", "A", "B", "C", "averageRating", "numVotes")
	SELECT "imdbid", "bechdel_rating", "title", "year", "binary", "budget_2013", "domgross_2013", "intgross_2013", "genres", "A", "B", "C", "averageRating", "numVotes"
	FROM bechdel_final;
COMMIT;