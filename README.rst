PG-Inserts : Get INSERT commands from PostgreSQL dump with COPY statements
==========================================================================

PostgreSQL's pg_dump with COPY statements is the most effective way to dump your
database, but is it difficult to grep in to recover specific data.


Installation
------------

This tool is written in `Rust <https://www.rust-lang.org/>`_ language. Install
it, then type::

  cargo install


Usage
-----

Just pipe dump output to pg-inserts::

  cat dump.sql | pg-inserts

If the dump file is a binary archive, use pg_restore::

  pg_restore dump.db | pg-inserts


Notice
------

A Python version is also provided (7.5 times slower than Rust version).
