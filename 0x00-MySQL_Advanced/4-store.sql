-- trigger
delimiter |

CREATE TRIGGER sub BEFORE INSERT ON orders
  FOR EACH ROW
  BEGIN
    UPDATE items SET items.quantity = items.quantity - NEW.number WHERE items.name = new.item_name;
  END;
|

delimiter ;