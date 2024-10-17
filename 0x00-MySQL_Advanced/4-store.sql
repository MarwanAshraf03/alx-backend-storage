-- trigger
create trigger before insert on order
for each row begin 
update items set items.quantity = items.quantity - new.number where items.name = new.item_name;