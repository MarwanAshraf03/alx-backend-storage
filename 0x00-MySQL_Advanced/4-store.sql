-- trigger
create trigger before insert on order
for each row set holberton.items.quantity = holberton.items.quantity - new.number;