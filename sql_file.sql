use bus_booking_system;
select * from registration;
select * from login;

create table buses (
		 id int primary key auto_increment,
		 Bus_name varchar(100) not null,
		bus_type varchar(50) not null,
         source varchar(100) not null,
         destination varchar(50) not null,
         departs_time varchar(100) not null,
         price decimal (10,2) not null,
         created_at timestamp default current_timestamp
);

alter table buses add column total_seats int default 32, status varchar(50) default;
select * from buses;