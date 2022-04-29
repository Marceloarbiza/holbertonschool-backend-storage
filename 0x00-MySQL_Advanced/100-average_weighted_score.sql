-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    SELECT SUM(score * weight) / SUM(weight) INTO @score_proj 
    FROM corrections INNER JOIN projects ON corrections.project_id = projects.id WHERE corrections.user_id = user_id;
    UPDATE users SET average_score = @score_proj WHERE id = user_id;
END$$
