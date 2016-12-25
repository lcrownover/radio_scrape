CREATE TABLE artists(
    artist_id      INTEGER PRIMARY KEY,
    artist_name    TEXT                NOT NULL
);

CREATE TABLE songs(
    song_id      INTEGER PRIMARY KEY,
    song_name    TEXT                NOT NULL,
    artist_id    INTEGER             NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

CREATE TABLE playdates(
    datetime     TEXT                NOT NULL,
    song_id      INTEGER             NOT NULL,
    FOREIGN KEY(song_id) REFERENCES songs(song_id)
);
