Title: Preventing join errors using `COUNT()`
Date: 2023-01-12
Tags: sql
Summary: Preventing join errors using `COUNT()`
Status: draft

Checking the number of rows before and after a join can prevent "join duplications"

A row can get duplicated if the join condition is true for multiple rows

SQL joins give you **at least** as many rows as the join specifies:
- A left join will give you **at least** as many rows in the left table
- An inner join will give you **at least**  the amount of rows common to both tables


https://alexpetralia.com/2017/07/19/more-dangerous-subtleties-of-joins-in-sql/