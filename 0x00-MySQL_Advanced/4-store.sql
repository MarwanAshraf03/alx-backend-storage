-- trigger
create trigger before insert on order
for each row set items.quantity = items.quantity - new.number;