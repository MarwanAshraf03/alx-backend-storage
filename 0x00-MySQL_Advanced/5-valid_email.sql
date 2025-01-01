-- trigger
delimiter |

CREATE TRIGGER validity BEFORE UPDATE ON users
  FOR EACH ROW
  BEGIN
    IF OLD.email <> NEW.email
    then
        SET NEW.valid_email = 0;
    END IF;
  END;
|

delimiter ;