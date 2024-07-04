\c pharmacyDb;

TRUNCATE users, products, request_products, medication_list, cart, orders, messages CASCADE;

INSERT INTO users (first_name, last_name, email, password, patient)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'password123', false),
('Jane', 'Doe', 'jane.doe@example.com', 'password456', true);

INSERT INTO products (name, description, category, brand, price, image_url, quantity, available, user_id)
VALUES 
('Aspirin', 'Pain reliever', 'Medication', 'PharmaCo', 10, 'http://example.com/aspirin.jpg', 100, true, 1),
('Paracetamol', 'Fever reducer', 'Medication', 'HealthCare', 15, 'http://example.com/paracetamol.jpg', 200, true, 1);

INSERT INTO request_products (user_id, product_id)
VALUES 
(1, 1),
(2, 2);

INSERT INTO medication_list (user_id)
VALUES 
(1),
(2);

INSERT INTO cart (user_id, product_id, total_amount)
VALUES 
(1, 1, 10.0),
(2, 2, 15.0);

INSERT INTO orders (user_id, product_id, total_amount)
VALUES 
(1, 1, 10.0),
(2, 2, 15.0);

INSERT INTO messages (user_id, receiver_id, message)
VALUES 
(1, 2, 'Hello Jane, how are you?'),
(2, 1, 'Hi John, I''m good, thanks! How about you?');