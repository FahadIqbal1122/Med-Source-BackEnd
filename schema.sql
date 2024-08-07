DROP DATABASE IF EXISTS pharmacyDb;

CREATE DATABASE pharmacyDb;

\c pharmacyDb;

DROP TABLE IF EXISTS messages, orders, cart, request_products, products, medication_list, users CASCADE;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  phone_number INTEGER,
  address VARCHAR(255),
  patient BOOLEAN
);

CREATE TABLE medication_list (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE request_products (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  product_id INTEGER
);

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description VARCHAR(255),
  category VARCHAR(255),
  brand VARCHAR(255),
  price INTEGER NOT NULL,
  image_url VARCHAR(255),
  quantity INTEGER,
  available BOOLEAN,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  medication_list_id INTEGER REFERENCES medication_list(id) ON DELETE CASCADE,
  request_products_id INTEGER 
);

CREATE TABLE cart (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  product_id INTEGER REFERENCES products(id) ON DELETE CASCADE,
  total_amount FLOAT NOT NULL
);

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  product_id INTEGER REFERENCES products(id) ON DELETE CASCADE,
  total_amount FLOAT NOT NULL
);

CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  receiver_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  message TEXT
);

ALTER TABLE request_products ADD CONSTRAINT fk_request_products_product_id FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE;

ALTER TABLE products ADD CONSTRAINT fk_products_request_products_id FOREIGN KEY (request_products_id) REFERENCES request_products(id) ON DELETE CASCADE;