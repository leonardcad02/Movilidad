CREATE DATABASE bus_db;
use bus_db;
create table users (
		username varchar(255), 
		password varchar(255),
        first_name varchar(255),
        Last_name varchar(255),
        email varchar(255),
        last_login datetime, 
        api_key varchar(255));        
show tables;
select * from users;
alter table users add unique (username, api_key);
alter table users add primary key (username, api_key);
truncate users;

insert into users values 
	('administrador', md5('12345'), 'Telematics', 'Research', 'telematics@gmail.com', now(), 'dfsdfsdfsfsdfcsd');

create table Node (
deviceID varchar(255),
username varchar(255),
field_name varchar(255),
latitud float(7,3),
longitud float(7,3),
altitud float(7,3),
velocidad  float(6,2),
personaone int,
personatwo int,
personatree int,
personafour int);
SET GLOBAL innodb_file_format=Barracuda;
SET GLOBAL innodb_file_per_table=1;
SET GLOBAL innodb_large_prefix=1;
ALTER TABLE Node ROW_FORMAT=DYNAMIC;
ALTER TABLE Node Add primary key(deviceID);
ALTER TABLE Node Add foreign  key(username) references users(username);


insert into Node values
	('BUS12012', 'administrador', 'BusIot', 40.714, -74.006, 2700, 63, 1 ,0 ,1 ,0);

select * from Node;

create table bus(
deviceID varchar(255),
latitud float(7,3),
longitud float(7,3),
altitud float(7,3),
velocidad  float(6,2),
personaone int,
personatwo int,
personatree int,
personafour int,
date_time datetime);
ALTER TABLE bus ROW_FORMAT=DYNAMIC;
ALTER TABLE bus Add foreign  key(deviceID) references Node(deviceID);

describe bus;

insert into bus values
('BUS12012', 40.714, -74.006, 2700, 63, 1 ,0 ,1 ,0, now());

select * from bus;

select * from users where username = "administrador";
update users set last_login = now() where username = "administrador";

select * from bus;
select * from (select * from bus order by date_time desc limit 10) dummy order by date_time asc;
select * from (select * from bus order by date_time desc limit 10) dummy order by date_time asc;
