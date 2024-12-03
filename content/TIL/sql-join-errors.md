Title: SQL join errors
Date: 2023-01-12
Tags: sql
Slug: sql-join-errors

# Join duplications

SQL joins give you **at least** as many rows as the join specifies:
- A left join will give you **at least** as many rows in the left table
- An inner join will give you **at least**  the amount of rows common to both tables

Count the number of rows `COUNT()` before and after a join


https://alexpetralia.com/2017/07/19/more-dangerous-subtleties-of-joins-in-sql/