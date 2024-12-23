-- Create trigger that decreases quantity after inserting new order

CREATE TRIGGER update_items 
AFTER INSERT ON orders
FOR EACH ROW
  UPDATE items
  SET quantity = quantity - NEW.number
  WHERE name = NEW.item_name;
