create database footprints;

grant all privileges on database footprints to fpuser;

\c footprints

create table device_master
(
	device_id bigint,
	instagram_id varchar(50),
	preparation_flg numeric(1),
	max_follow_count numeric(2),
	create_datetime timestamp,
	update_datetime timestamp,
	primary key (
		device_id
	)
);

--
-- process_type|state|mean
----------------------------------------------
-- 1           |1    |not found searchbox...
-- 2           |1    |not found searchbox...
-- 2           |2    |more look is appeared
create table device_state
(
	device_id bigint,
	process_type numeric(1), -- 1:follow 2:collect
	state numeric(1),        -- 0:clear 1-9:can't continue
	create_datetime timestamp,
	update_datetime timestamp,
	primary key (
		device_id,
		process_type
	)
);

create table parent_account
(
	parent_id varchar(50),
	url varchar(100),
	collection_date date,
	create_datetime timestamp,
	update_datetime timestamp,
	primary key (
		parent_id
	)
);

create table account_pool
(
	follow_id varchar(50),
	parent_id varchar(50),
	url varchar(100),
	status numeric(1),
	create_datetime timestamp,
	update_datetime timestamp,
	primary key(
		follow_id
	)
);

create table file_request
(
	request_id varchar(12),
	device_id bigint,
	file_name varchar(20),
	status numeric(1),
	create_datetime timestamp,
	update_datetime timestamp,
	primary key(
		request_id,
		device_id
	)
);

create table account_follow_history
(
	instagram_id varchar(50),
	follow_id varchar(50),
	parent_id varchar(50),
	status numeric(1),
	create_datetime timestamp,
	update_datetime timestamp,
	primary key(
		instagram_id,
		follow_id
	)
);
