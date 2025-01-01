-- creating an index called idx_name_first
-- ALTER TABLE names DROP INDEX idx_name_first;
CREATE INDEX idx_name_first ON names (name(1));
-- Write a SQL script that creates an index idx_name_first on the table names and the first letter of name.