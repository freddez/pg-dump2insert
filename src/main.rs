use std::io;
use std::io::prelude::*;
extern crate regex;
use regex::Regex;

fn main() {
    let stdin = io::stdin();
    let mut stdin = stdin.lock();
    let mut line = String::new();
    let mut table_name = String::new();
    let mut fields = String::new();
    let re = Regex::new(r"^COPY (\w+) \(([\w, ]+)\) FROM stdin;").unwrap();
    let mut insert_mode = false;
    while stdin.read_line(&mut line).unwrap() > 0 {
        if insert_mode {
            if line == "\\.\n" {
                insert_mode = false;
            }
            else {
                let mut values = String::new();
                line.pop();
                for s in line.split("\t") {
                    if s == "\\N" {
                        values += "NULL, ";
                    } else {
                        values += "'";
                        values += s;
                        values += "', ";
                    }
                }
                values.pop();
                values.pop();
                println!("INSERT INTO {} ({}) VALUES ({});",
                         table_name, fields, values);
            }
        }
        else {
            match re.captures(&line) {
                None => print!("{}", line),
                Some(caps) => {
                    table_name = String::from(caps.at(1).unwrap());
                    fields = String::from(caps.at(2).unwrap());
                    insert_mode = true;
                },
            };
        }
        line.clear();
    }
}
