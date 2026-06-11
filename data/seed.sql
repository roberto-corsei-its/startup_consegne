DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS riders;

CREATE TABLE riders(
id serial PRIMARY KEY,
name varchar(50) not null,
vehicle varchar(50) not null,
total_deliveries integer not null
)

CREATE TABLE reviews(
id SERIAL,
rider_id integer not null ,
customer_name varchar(50) not null,
rating integer not null,
comment varchar(400) not null,
FOREIGN KEY (rider_id) references riders(id),
PRIMARY KEY(id)
)
