SELECT
	username,
	passhash,
	salt,
	email-confirmed,
	creation-timestamp
FROM
	users
WHERE
	username = ?username
