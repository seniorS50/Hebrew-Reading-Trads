CREATE TABLE filenames (
    file TEXT NOT NULL,
    country TEXT NOT NULL,
    city TEXT NOT NULL,
    HULTP TEXT NOT NULL,
    book TEXT NOT NULL,
    chapter TEXT NOT NULL,
    verses TEXT NOT NULL,
    reader_1st_Name TEXT NOT NULL,
    reader_2nd_Name TEXT NOT NULL,
    year INTEGER NOT NULL,
    FOREIGN KEY (city) REFERENCES cities (name)
);

CREATE TABLE cities (
    name TEXT NOT NULL,
    country TEXT NULL,
    latitude NUMERIC,
    longitude NUMERIC
);


{
    "File": "Afghanistan Herat 12504 Genesis 47 28-31 Aba Gol 1981",
    "Country": "Afghanistan",
    "City": "Herat",
    "HULTP": 12504,
    "Book": "Genesis",
    "Chapter": 47,
    "Verses": "28-31",
    "Reader_1st_Name": "Aba",
    "Reader_1st_Name": "Gol",
    "Year": 1981
  }