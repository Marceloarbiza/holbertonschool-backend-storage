-- Write a SQL script that creates a stored
-- procedure AddBonus that adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id, IN project_name VARCHAR(255), IN score INT)
BEGIN
    IF NOT EXISTS (SELECT name FROM projects WHERE name = project_name) THEN
        INSERT INTO projects (name) VALUES (project_name);
        SELECT id INTO @project_id FROM projects WHERE name=project_name;
        INSERT INTO corrections (user_id, project_id, score)VALUES (user_id, project_id, score); 
    ELSE
        SELECT id INTO @project_id FROM projects WHERE name=project_name;
        INSERT INTO corrections (user_id, project_id, score)VALUES (user_id, project_id, score);
    END IF;
END;$$