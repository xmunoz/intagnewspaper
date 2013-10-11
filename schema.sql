drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    title text not null,
    date text not null
    issue_number text not null
)