insert = """
INSERT INTO sharepads (
	slug,
	name
) VALUES (
	%(slug)s,
	%(name)s
)
RETURNING (id, external_id)
"""

all = """
SELECT *
FROM sharepads
"""
