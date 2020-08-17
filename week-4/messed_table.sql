UPDATE Planet SET kepler_name = NULL WHERE status != 'CONFIRMED';
DELETE FROM Planet WHERE radius < 0;
