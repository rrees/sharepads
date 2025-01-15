-- migrate:up

CREATE OR REPLACE FUNCTION update_modified_column() 
	RETURNS TRIGGER AS $$
	BEGIN
	    NEW.modified = now();
	    RETURN NEW; 
	END;
	$$ language 'plpgsql';

-- migrate:down

DROP FUNCTION update_modified_column;