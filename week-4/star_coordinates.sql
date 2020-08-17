ALTER TABLE Star
ADD COLUMN ra FLOAT,
ADD COLUMN decl FLOAT;
DELETE FROM Star;
COPY Star (kepler_id, t_eff, radius, ra, decl) FROM 'stars_full.csv' CSV;

