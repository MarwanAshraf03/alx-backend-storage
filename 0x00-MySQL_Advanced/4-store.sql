-- trigger
DELIMITER //

CREATE TRIGGER before_insert_order
BEFORE INSERT ON `order`
FOR EACH ROW 
BEGIN
    UPDATE items 
    SET items.quantity = items.quantity - NEW.number 
    WHERE items.name = NEW.item_name;
END//

DELIMITER ;