create table oss_file (
  id integer PRIMARY KEY autoincrement,
  md5 varchar(64),
  oss_path varchar(2000),
  local_path varchar(2000),
  upload_time datetime default (datetime('now', 'localtime'))
);

CREATE UNIQUE INDEX unq_md5 ON  oss_file(md5);


// 忽略MD5,可以重复上传
CREATE TABLE "oss_file" (
"id"  integer PRIMARY KEY AUTOINCREMENT,
"md5"  varchar(64),
"oss_path"  varchar(2000),
"local_path"  varchar(2000),
"upload_time"  datetime DEFAULT (datetime('now', 'localtime'))
);

CREATE INDEX "idx_md5"
ON "oss_file" ("md5" ASC);