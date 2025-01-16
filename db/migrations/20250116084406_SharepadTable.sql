-- migrate:up

CREATE TABLE IF NOT EXISTS sharepads(
	id INT GENERATED ALWAYS AS IDENTITY,
	external_id uuid UNIQUE NOT NULL DEFAULT gen_random_uuid(),
	slug TEXT UNIQUE NOT NULL,
	name TEXT,
	content TEXT,
	created timestamp default current_timestamp,
	updated timestamp default current_timestamp
);

CREATE TRIGGER update_sharepads_modtime
BEFORE UPDATE ON sharepads
FOR EACH ROW EXECUTE PROCEDURE update_modified_column();

-- migrate:down

DROP TABLE
IF EXISTS sharepads;

DROP TRIGGER
IF EXISTS update_sharepads_modtime
ON sharepads;