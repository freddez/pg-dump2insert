pg-dump2insert : Fast PostgreSQL COPY dump to INSERT commands converter
=======================================================================

PostgreSQL's pg_dump with *COPY* statements format is the most effective way to
backup and restore your database. However for retrieving specific data or to
inject dump into non-PostgreSQL database, *INSERT* commands are far more
convenient. This tool simply converts *COPY* dumps to *INSERT* dumps.

Installation
------------

This tool is written in `Rust <https://www.rust-lang.org/>`_ language. Install
it, then type::

  cargo install


Usage
-----

Just pipe dump output to pg-dump2insert::

  cat dump.sql | pg-dump2insert

If the dump file is a binary archive, use pg_restore::

  pg_restore dump.db | pg-dump2insert
  pg_restore -t tablenamedump.db | pg-dump2insert


Notice
------

The only difference with "--inserts" dumps is that all numeric values are quoted
in INSERTs (which is permitted in PostgreSQL), i.e.::

  INSERT INTO tablename (id, ...) VALUES ('2', ...);

A (5 times slower) Python version is also provided.
