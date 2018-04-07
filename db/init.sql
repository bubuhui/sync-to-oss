create table oss_file (
  id integer(20) PRIMARY KEY autoincrement,
  md5 varchar(64),
  oss_path varchar(2000),
  local_path varchar(2000),
  upload_time datetime default (datetime('now', 'localtime'))
);


CREATE UNIQUE INDEX unq_md5 ON  oss_file(md5);