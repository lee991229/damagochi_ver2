import json

# json.dumps()
"""
CREATE TABLE "character" (
	"character_id"	INTEGER,
	"user_id"	INTEGER NOT NULL,
	"character_nickname"	TEXT NOT NULL,
	"character_exp"	INTEGER NOT NULL,
	PRIMARY KEY("character_id" AUTOINCREMENT)
);
CREATE TABLE "character_stat" (
	"character_id"	INTEGER NOT NULL,
	"character_hunger"	INTEGER NOT NULL,
	"character_affection"	INTEGER NOT NULL,
	"character_health"	INTEGER NOT NULL
);
CREATE TABLE "inventory" (
	"user_id"	INTEGER NOT NULL,
	"item_id"	INTEGER NOT NULL,
	"item_name"	TEXT NOT NULL,
	"item_num"	INTEGER NOT NULL
);
CREATE TABLE "item_list" (
	"item_id"	INTEGER NOT NULL,
	"item_name"	INTEGER NOT NULL UNIQUE,
	"hunger"	INTEGER NOT NULL,
	"affection"	INTEGER NOT NULL,
	"health"	INTEGER NOT NULL,
	"exp"	INTEGER NOT NULL,
	PRIMARY KEY("item_id" AUTOINCREMENT)
);
CREATE TABLE "user" (
	"user_id"	INTEGER,
	"user_name"	TEXT NOT NULL UNIQUE,
	"user_pw"	TEXT NOT NULL,
	"user_nickname"	TEXT NOT NULL,
	PRIMARY KEY("user_id" AUTOINCREMENT)
);
"""
