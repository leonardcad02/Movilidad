-- CREATE DATABASE FOR SYSTEM OF MONITORING WITH TABLES AND PARAMETERS
CREATE DATABASE movilidad_db;
use movilidad_db;
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
	('administrador', md5('12345'), 'Telematics', 'Research', 'telematics@gmail.com', now(), 'abhikuchnhihai');

create table node (
deviceID varchar(255),
username varchar(255),
field_name varchar(255),
temperature float(6,3),
humidity float(6,3),
polution float(7,3),
uv  float(8,3),
noise float(7,3),
pmone int,
pmtwo int,
pmten int);
SET GLOBAL innodb_file_format=Barracuda;
SET GLOBAL innodb_file_per_table=1;
SET GLOBAL innodb_large_prefix=1;
ALTER TABLE node ROW_FORMAT=DYNAMIC;
ALTER TABLE node Add primary key(deviceID);
ALTER TABLE node Add foreign  key(username) references users(username);


insert into node values
	('MET12012', 'administrador', 'MetereologiaIot', 18.40, 69.00, 534.56, 2613.75, 534.94 ,15 ,12 ,15);

select * from node;

create table movilidad (
deviceID varchar(255),
temperature float(6,3),
humidity float(6,3),
polution float(7,3),
uv  float(8,3),
noise float(7,3),
pmone int,
pmtwo int,
pmten int,
date_time datetime);
ALTER TABLE movilidad ROW_FORMAT=DYNAMIC;
ALTER TABLE movilidad Add foreign  key(deviceID) references Node(deviceID);

describe movilidad;

insert into movilidad values
('MET12012', 18.40, 69.00 , 534.56, 2613.75, 534.94, 15, 12, 15, now());

select * from movilidad;

select * from users where username = "administrador";
update users set last_login = now() where username = "administrador";

select * from movilidad;
select * from (select * from movilidad order by date_time desc limit 10) dummy order by date_time asc;
select * from (select * from movilidad order by date_time desc limit 10) dummy order by date_time asc;
