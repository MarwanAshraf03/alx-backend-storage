-- trigger
delimiter |

CREATE TRIGGER sub BEFORE INSERT ON orders
  FOR EACH ROW
  BEGIN
    update items set items.quantity = items.quantity - NEW.number where items.name = new.item_name;
  END;
|

delimiter ;