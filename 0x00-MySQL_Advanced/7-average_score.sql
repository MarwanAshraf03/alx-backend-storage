-- creating a procedure to add a new correction
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER &&  
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)  
BEGIN
    DECLARE average DECIMAL(10,2);
    DECLARE total_score INT;
    DECLARE total_count INT;

    SELECT SUM(score), COUNT(*) 
    INTO total_score, total_count
    FROM corrections
    WHERE corrections.user_id = user_id;

    IF total_count > 0 THEN
        SET average = total_score / total_count;
    ELSE
        SET average = 0;
    END IF;

    UPDATE users SET average_score = average WHERE users.id = user_id;

END &&  
DELIMITER ;  