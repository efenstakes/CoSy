create database if not exists cosy;


create table accounts (
  id int auto_increment,
  name varchar(50),
  email varchar(120),
  joined_on datetime default NOW(),
  primary key(id)
);
create table accounts_backup (
  id int auto_increment,
  user_id int,
  contact_phone varchar(15),
  contact_email varchar(95),
  contact_name varchar(95),
  added_on datetime default NOW(),
  primary key(id),
  foreign key(user_id) references accounts(id) on delete cascade
);


' to use for testing cosy on heroku '
create table accounts_backup_teste (
  id int auto_increment,
  user varchar,
  contact_phone varchar(15),
  contact_email varchar(95),
  contact_name varchar(95),
  added_on datetime default NOW(),
  primary key(id)
);