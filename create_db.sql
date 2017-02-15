BEGIN TRANSACTION;

DROP TABLE IF EXISTS assignments;
DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS sub_assignments;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS users;


CREATE TABLE "users" (
	`ID_user`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`name`	TEXT NOT NULL,
	`surname`	TEXT NOT NULL,
	`login`	TEXT NOT NULL,
	`password`	TEXT NOT NULL DEFAULT 123,
	`status`	INTEGER NOT NULL DEFAULT 1,
	`ID_role`	INTEGER NOT NULL DEFAULT 1,
	`ID_team`	INTEGER
);
INSERT INTO "users" VALUES(1,'Jan','Kowalski','jkowalski','123',1,1,1);
INSERT INTO "users" VALUES(2,'Andrzej','Student','astudent','123',1,1,1);
INSERT INTO "users" VALUES(3,'Adam','Abacki','aabacki','123',1,1,2);
INSERT INTO "users" VALUES(4,'Bolesław','Babacki','bbabacki','123',1,1,2);
INSERT INTO "users" VALUES(5,'Czesław','Cabacki','ccabacki','123',1,1,3);
INSERT INTO "users" VALUES(6,'Damian','Dabacki','ddabacki','123',1,1,3);
INSERT INTO "users" VALUES(7,'Edward','Ebacki','eebacki','123',1,1,NULL);
INSERT INTO "users" VALUES(8,'Adam','Mentor','amentor','123',1,2,NULL);
INSERT INTO "users" VALUES(9,'Marcin','Izworski','mizworski','123',1,2,NULL);
INSERT INTO "users" VALUES(10,'Fabian','Fabacki','ffabacki','123',1,2,NULL);
INSERT INTO "users" VALUES(11,'Grzegorz','Gabacki','ggabacki','123',1,2,NULL);
INSERT INTO "users" VALUES(12,'Amadeusz','Employee','aemployee','123',1,3,NULL);
INSERT INTO "users" VALUES(13,'Hiacynt','Habacki','hhabacki','123',1,3,NULL);
INSERT INTO "users" VALUES(14,'Jerzy','Margaus','jmargaus','123',1,4,NULL);
CREATE TABLE "teams" (
	`ID_team`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`team_name`	TEXT NOT NULL
);
INSERT INTO "teams" VALUES(1,'biedronki');
INSERT INTO "teams" VALUES(2,'motylki');
INSERT INTO "teams" VALUES(3,'muchomorki');
CREATE TABLE `roles` (
	`ID_role`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`role_name`	TEXT NOT NULL
);
INSERT INTO "roles" VALUES(1,'student');
INSERT INTO "roles" VALUES(2,'mentor');
INSERT INTO "roles" VALUES(3,'employee');
INSERT INTO "roles" VALUES(4,'manager');
CREATE TABLE `assignments` (
	`ID_assignment`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`assignment_name`	TEXT NOT NULL,
	`due_date`	INTEGER NOT NULL,
	`max_points`	INTEGER NOT NULL,
	`ID_user`	INTEGER NOT NULL
);
INSERT INTO "assignments" VALUES(1,'ccms','2017-02-14',72,8);
INSERT INTO "assignments" VALUES(2,'geometry','2017-02-10',36,9);
INSERT INTO "assignments" VALUES(3,'dojo','2017-01-04',12,11);
INSERT INTO "assignments" VALUES(4,'erp','2017-02-16',36,9);
CREATE TABLE `sub_assignments` (
	`ID_sub_assignment`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`sub_date`	INTEGER NOT NULL,
	`grade`	INTEGER,
	`ID_assignment`	INTEGER NOT NULL,
	`ID_user`	INTEGER NOT NULL
);
INSERT INTO "sub_assignments" VALUES(1,'2017-02-12',50,1,2);
INSERT INTO "sub_assignments" VALUES(2,'2017-02-13',30,2,2);
INSERT INTO "sub_assignments" VALUES(3,'2017-01-23','',3,2);
INSERT INTO "sub_assignments" VALUES(4,'2017-01-12',61,1,1);
INSERT INTO "sub_assignments" VALUES(5,'2017-01-16',24,2,1);
INSERT INTO "sub_assignments" VALUES(6,'2017-01-20','',1,3);
CREATE TABLE `attendance` (
	`ID_attendance`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`date`	INTEGER NOT NULL,
	`attendance_status`	INTEGER NOT NULL DEFAULT 0,
	`ID_user`	INTEGER NOT NULL
);
INSERT INTO "attendance" VALUES(1,'2017-02-01',0,2);
INSERT INTO "attendance" VALUES(2,'2017-02-02',1,2);
INSERT INTO "attendance" VALUES(3,'2017-02-03',1,2);
INSERT INTO "attendance" VALUES(4,'2017-02-04',1,2);
INSERT INTO "attendance" VALUES(5,'2017-02-01',1,1);
INSERT INTO "attendance" VALUES(6,'2017-02-01',1,3);
INSERT INTO "attendance" VALUES(7,'2017-02-01',1,4);
INSERT INTO "attendance" VALUES(8,'2017-02-01',1,5);
INSERT INTO "attendance" VALUES(9,'2017-02-01',1,6);
INSERT INTO "attendance" VALUES(10,'2017-02-03',0,7);
INSERT INTO "attendance" VALUES(11,'2017-02-03',1,1);
INSERT INTO "attendance" VALUES(12,'2017-02-04',1,3);
INSERT INTO "attendance" VALUES(13,'2017-02-03',1,4);
INSERT INTO "attendance" VALUES(14,'2017-02-05',1,5);
INSERT INTO "attendance" VALUES(15,'2017-02-07',1,6);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('teams',3);
INSERT INTO "sqlite_sequence" VALUES('roles',4);
INSERT INTO "sqlite_sequence" VALUES('assignments',4);
INSERT INTO "sqlite_sequence" VALUES('sub_assignments',6);
INSERT INTO "sqlite_sequence" VALUES('attendance',15);
COMMIT;
