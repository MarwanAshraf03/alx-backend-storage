-- trigger
delimiter //
create trigger sub before insert on orders
for each row begin 
update items set items.quantity -= NEW.number where items.name = new.item_name;
end//
delimiter ;