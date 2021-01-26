
Problem 1
----------

The 'select' is the basic query. We use it to extract information from a
table. There are a number of clauses to a select statement. Right now, we'll
concern ourself with just two: the column list and the table you are querying.
The format of the basic select statement is

    SELECT <column list> FROM <table name>;

For now, we can use the wildcard '*' (without quotes) to select all columns
from a given table.

Examples: http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial -- 1

Task: Write a query that shows all the information about all the salespeople in
the database. Use a basic SELECT query.

SQL [1]> SELECT *
... [1]> SELECT *;
There was a problem with your SQL syntax:

        syntax error at or near "SELECT"
LINE 3: SELECT *;
        ^



SQL [1]> SELECT * FROM salespeople;

  id   |          email          | first_name | last_name  |  region   
-------+-------------------------+------------+------------+-----------
     1 | vriley24@gmail.com      | Victor     | Riley      | Central   
     2 | dmarshall64@gmail.com   | Doris      | Marshall   | Southeast 
     3 | rmartinez98@gmail.com   | Ruth       | Martinez   | Northwest 
     4 | aking95@gmail.com       | Anne       | King       | Southeast 
     5 | crichardson95@gmail.com | Chris      | Richardson | Central   
     6 | shunt49@gmail.com       | Steven     | Hunt       | Northeast 
     7 | acarr32@gmail.com       | Anna       | Carr       | Northeast 
     8 | lhayes62@gmail.com      | Linda      | Hayes      | Southeast 
     9 | jtaylor23@gmail.com     | Jeffrey    | Taylor     | Southwest 
    10 | nfields5@gmail.com      | Norma      | Fields     | Northwest 
    11 | mfernandez48@gmail.com  | Michelle   | Fernandez  | Northeast 
    12 | mhart95@gmail.com       | Michelle   | Hart       | Northwest 
    13 | cbailey73@gmail.com     | Cynthia    | Bailey     | Southeast 
    14 | smorales2@gmail.com     | Shirley    | Morales    | Northeast 
    15 | lgeorge92@gmail.com     | Louise     | George     | Central   
    16 | jgrant89@gmail.com      | Judy       | Grant      | Northeast 
    17 | ctorres2@gmail.com      | Carol      | Torres     | Central   
    18 | mwatkins36@gmail.com    | Maria      | Watkins    | Central   
    19 | raustin87@gmail.com     | Ruth       | Austin     | Southwest 
    20 | mcrawford24@gmail.com   | Marilyn    | Crawford   | Central   
(250 rows, truncated for display at 20)

        Correct!

SELECT * FROM salespeople;

        Moving on...


Problem 2
----------

Select statements can have an additional clause called the 'where' clause.
This lets us extract specific rows out of our table. Our where clause can be
specific enough to match a single row, or general enough to match a set of
rows. The format of a select statement with a 'where' clause is:

    SELECT <column list> FROM <table name> WHERE <equality expression>;

Examples: http://sqlzoo.net/wiki/SELECT_basics -- 1

Task: Write a query that shows all the information about all salespeople from
the 'Northwest' region.

SQL [2]> SELECT region FROM salespeople WHERE region='Northwest';

  region   
-----------
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
 Northwest 
(52 rows, truncated for display at 20)

(results do not match answer)


SQL [2]> SELECT * FROM salespeople WHERE region='Northwest';

  id   |         email          | first_name | last_name |  region   
-------+------------------------+------------+-----------+-----------
     3 | rmartinez98@gmail.com  | Ruth       | Martinez  | Northwest 
    10 | nfields5@gmail.com     | Norma      | Fields    | Northwest 
    12 | mhart95@gmail.com      | Michelle   | Hart      | Northwest 
    27 | abutler68@gmail.com    | Anne       | Butler    | Northwest 
    30 | lnichols80@gmail.com   | Lori       | Nichols   | Northwest 
    37 | shansen50@gmail.com    | Susan      | Hansen    | Northwest 
    39 | jcole2@gmail.com       | Jennifer   | Cole      | Northwest 
    40 | cberry73@gmail.com     | Carol      | Berry     | Northwest 
    42 | lgutierrez50@gmail.com | Louise     | Gutierrez | Northwest 
    45 | hdixon51@gmail.com     | Heather    | Dixon     | Northwest 
    56 | afrazier90@gmail.com   | Amanda     | Frazier   | Northwest 
    58 | jmiller60@gmail.com    | Julia      | Miller    | Northwest 
    63 | ahill75@gmail.com      | Annie      | Hill      | Northwest 
    70 | pwells28@gmail.com     | Phyllis    | Wells     | Northwest 
    72 | lwelch43@gmail.com     | Lillian    | Welch     | Northwest 
    77 | bking33@gmail.com      | Beverly    | King      | Northwest 
    87 | sjackson98@gmail.com   | Stephanie  | Jackson   | Northwest 
    88 | jphillips90@gmail.com  | Judy       | Phillips  | Northwest 
    96 | dross42@gmail.com      | Deborah    | Ross      | Northwest 
    97 | pbaker10@gmail.com     | Phyllis    | Baker     | Northwest 
(52 rows, truncated for display at 20)

        Correct!

SELECT * FROM salespeople WHERE region='Northwest';

        Moving on...


Problem 3
----------

We've been selecting all the columns out of our table up until now, but the
amount of data can be overwhelming. We can use the column list to specify
individual columns. We do this by specifying the column list as a single column
name instead of a '*'.

Examples: http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial -- 1

Task: Write a query that shows just the emails of the salespeople from the
'Southwest' region.

SQL [3]> SELECT email FROM salespeople WHERE region='Southwest'
... [3]> ;

         email         
-----------------------
 jtaylor23@gmail.com   
 raustin87@gmail.com   
 aharper19@gmail.com   
 mhughes19@gmail.com   
 dtorres70@gmail.com   
 mscott19@gmail.com    
 lcastillo71@gmail.com 
 bclark93@gmail.com    
 rfuller24@gmail.com   
 rbennett86@gmail.com  
 bboyd86@gmail.com     
 eevans28@gmail.com    
 hmyers61@gmail.com    
 hgeorge10@gmail.com   
 mgonzales11@gmail.com 
 kcampbell83@gmail.com 
 cwilliams60@gmail.com 
 cfuller59@gmail.com   
 pbell12@gmail.com     
 lmorris25@gmail.com   
(44 rows, truncated for display at 20)

        Correct!

SELECT email FROM salespeople WHERE region='Southwest'
;

        Moving on...


Problem 4
----------

We can ask for more than one column from the data set by specifying all the
columns separated by commas.

Examples: http://sqlzoo.net/wiki/SELECT_from_Nobel_Tutorial -- 1, 2
          http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial -- 1

Task: Write a query that shows the first name, last name, and email of all
salespeople in the 'Northwest' region.

SQL [4]> SELECT first_name, last_name, email FROM salespeople WHERE region='Northwest';

 first_name | last_name |         email          
------------+-----------+------------------------
 Ruth       | Martinez  | rmartinez98@gmail.com  
 Norma      | Fields    | nfields5@gmail.com     
 Michelle   | Hart      | mhart95@gmail.com      
 Anne       | Butler    | abutler68@gmail.com    
 Lori       | Nichols   | lnichols80@gmail.com   
 Susan      | Hansen    | shansen50@gmail.com    
 Jennifer   | Cole      | jcole2@gmail.com       
 Carol      | Berry     | cberry73@gmail.com     
 Louise     | Gutierrez | lgutierrez50@gmail.com 
 Heather    | Dixon     | hdixon51@gmail.com     
 Amanda     | Frazier   | afrazier90@gmail.com   
 Julia      | Miller    | jmiller60@gmail.com    
 Annie      | Hill      | ahill75@gmail.com      
 Phyllis    | Wells     | pwells28@gmail.com     
 Lillian    | Welch     | lwelch43@gmail.com     
 Beverly    | King      | bking33@gmail.com      
 Stephanie  | Jackson   | sjackson98@gmail.com   
 Judy       | Phillips  | jphillips90@gmail.com  
 Deborah    | Ross      | dross42@gmail.com      
 Phyllis    | Baker     | pbaker10@gmail.com     
(52 rows, truncated for display at 20)

        Correct!

SELECT first_name, last_name, email FROM salespeople WHERE region='Northwest';

        Moving on...


Problem 5
----------

In addition to finding exact matches, we can specify the where clause of our
query to match a range of columns using inequalities.

Examples: http://sqlzoo.net/wiki/SELECT_basics -- 2, 3
          http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial -- 2

Task: Write a query that shows the common name of melons that cost more than
$5.00.

SQL [5]> SELECT common_name FROM melons WHERE price>5.0
... [5]> ;

   common_name   
-----------------
 Christmas Melon 
 Densuke         
(2 rows)

        Correct!

SELECT common_name FROM melons WHERE price>5.0
;

        Moving on...


Problem 6
----------

Sometimes, we want to filter down our matched rows even further. We can add
additional restrictions to our query using an 'and' clause. It looks like this:
    
    SELECT <column list> FROM <table> WHERE <expression 1> AND <expression 2>;

Examples: http://sqlzoo.net/wiki/SELECT_basics -- 3, 6

Task: Write a query that shows the common name and price for all
watermelons that cost more than $5.00.


SQL [6]> SELECT common_name, price FROM watermelons WHERE price > 5;
There was a problem with your SQL syntax:

        relation "watermelons" does not exist
LINE 2: SELECT common_name, price FROM watermelons WHERE price > 5;
                                       ^



SQL [6]> SELECT common_name, price FROM watermelons WHERE price > 5.0;
There was a problem with your SQL syntax:

        relation "watermelons" does not exist
LINE 2: SELECT common_name, price FROM watermelons WHERE price > 5.0...
                                       ^



SQL [6]> SELECT common_name, price FROM melons WHERE price > 5.0 AND melon_type='Watermelon';

 common_name |  price   
-------------+----------
 Densuke     |   250.00 
(1 rows)

        Correct!

SELECT common_name, price FROM melons WHERE price > 5.0 AND melon_type='Watermelon';

        Moving on...


Problem 7
----------

Using inequalities on numeric columns lets us match a range of rows.
Similarly, we can use a string wildcard to do matches on ranges of strings.
Confusingly, the string wildcard is '%', which is different from the column
wildcard, which is '*'. Additionally, you can't use an equality to match a
string wildcard, you have to use a 'like' clause instead. The format is as
follows:

    <column_name> LIKE '<match string with wildcards>'
    
Examples: http://sqlzoo.net/wiki/SELECT_basics -- 5

Task: Write a query that displays all common names of melons that start with
the letter 'C'.


SQL [7]> SELECT common_name FROM melons WHERE common_name LIKE 'C%'
... [7]> ;

           common_name            
----------------------------------
 Crane                            
 Casaba                           
 Cantaloupe                       
 Christmas Melon                  
 Canary                           
 Carolina Cross 180 Watermelon    
 Charleston Gray Watermelon       
 Chris Cross Watermelon           
 Congo Watermelon                 
 Cream of Saskatchewan Watermelon 
 Crimson Sweet Watermelon         
 Crenshaw                         
(12 rows)

        Correct!

SELECT common_name FROM melons WHERE common_name LIKE 'C%'
;

        Moving on...


Problem 8
----------

String wildcards can be places anywhere in a string, allowing you to match
complex patterns. For example, the string pattern 'W%termelon%' matches the
strings 'Watermelon', 'Wintermelon', 'Watermelons', and 'Wintermelons'.
    
Examples: http://sqlzoo.net/wiki/SELECT_basics -- 5

Task: Write a query that shows the common name of any melon with 'Golden'
anywhere in the common name.


SQL [8]> SELECT common_name FROM melons WHERE common_name LIKE '%Golden%';

       common_name        
--------------------------
 Golden Honey Watermelon  
 Golden Midget Watermelon 
 Royal Golden Watermelon  
 Texas Golden Watermelon  
(4 rows)

        Correct!

SELECT common_name FROM melons WHERE common_name LIKE '%Golden%';

        Moving on...


Problem 9
----------

Frequently, you will encounter duplicate data across multiple rows. In our
salespeople table schema, we can see that each one is attached to a specific
'region'. If we query that table for all the different regions that are used,
sql will return duplicates, one for each salesperson in our table.
To counter this, we can use the 'distinct' keyword. In our column list, we can
prepend the keyword to the column name.

Examples: http://sqlzoo.net/wiki/Using_SUM,_Count,_MAX,_DISTINCT_and_ORDER_BY -- 2
          http://sqlzoo.net/wiki/SUM_and_COUNT -- 2

Task: Write a query that shows all the distinct regions that a salesperson can belong to.


SQL [9]> SELECT region FROM salespeople;

  region   
-----------
 Central   
 Southeast 
 Northwest 
 Southeast 
 Central   
 Northeast 
 Northeast 
 Southeast 
 Southwest 
 Northwest 
 Northeast 
 Northwest 
 Southeast 
 Northeast 
 Central   
 Northeast 
 Central   
 Central   
 Southwest 
 Central   
(250 rows, truncated for display at 20)

(results do not match answer)


SQL [9]> SELECT DISTINCT region FROM salespeople;

  region   
-----------
 Northwest 
 Southeast 
 Northeast 
 Central   
 Southwest 
(5 rows)

        Correct!

SELECT DISTINCT region FROM salespeople;

        Moving on...


Problem 10
----------

Earlier, we used the 'and' keyword to narrow down our query: we made our
search more specific. We can use the 'or' keyword in exactly the opposite way,
to make our search match more rows.
Example: http://sqlzoo.net/wiki/SELECT_basics -- 6

Task: Write a query that shows the emails of all salespeople from both the
Northwest and Southwest regions.


SQL [10]> SELECT email FROM salespeople WHERE region='Northwest' OR 'Southwest';
There was a problem with your SQL syntax:

        invalid input syntax for type boolean: "Southwest"
LINE 2: ...mail FROM salespeople WHERE region='Northwest' OR 'Southwest...
                                                             ^



SQL [10]> SELECT email FROM salespeople WHERE region='Northwest' OR region='Southwest';

         email          
------------------------
 rmartinez98@gmail.com  
 jtaylor23@gmail.com    
 nfields5@gmail.com     
 mhart95@gmail.com      
 raustin87@gmail.com    
 aharper19@gmail.com    
 mhughes19@gmail.com    
 abutler68@gmail.com    
 lnichols80@gmail.com   
 shansen50@gmail.com    
 jcole2@gmail.com       
 cberry73@gmail.com     
 dtorres70@gmail.com    
 lgutierrez50@gmail.com 
 hdixon51@gmail.com     
 mscott19@gmail.com     
 lcastillo71@gmail.com  
 bclark93@gmail.com     
 afrazier90@gmail.com   
 rfuller24@gmail.com    
(96 rows, truncated for display at 20)

        Correct!

SELECT email FROM salespeople WHERE region='Northwest' OR region='Southwest';

        Moving on...


Problem 11
----------

It can be tedious to match a single column against multiple options. In our
previous exercise, we searched for the region to match both 'Northwest' and
'Southwest'. If we had more options we were trying to match, this would make
our query very long. We can use an 'in' clause to write this kind of query more
succinctly. We can replaces a series of 'or' clauses with a single 'in' clause
that takes the following format:

    <column name> IN (<option1>, <option2>, <...>)

Example: http://sqlzoo.net/wiki/SELECT_basics -- 4

Task: Write a query that shows the emails of all salespeople from both the
Northwest and Southwest regions, this time using an 'IN' clause.  


SQL [11]> SELECT email FROM salespeople WHERE region IN ('Northwest', 'Southwest');

         email          
------------------------
 rmartinez98@gmail.com  
 jtaylor23@gmail.com    
 nfields5@gmail.com     
 mhart95@gmail.com      
 raustin87@gmail.com    
 aharper19@gmail.com    
 mhughes19@gmail.com    
 abutler68@gmail.com    
 lnichols80@gmail.com   
 shansen50@gmail.com    
 jcole2@gmail.com       
 cberry73@gmail.com     
 dtorres70@gmail.com    
 lgutierrez50@gmail.com 
 hdixon51@gmail.com     
 mscott19@gmail.com     
 lcastillo71@gmail.com  
 bclark93@gmail.com     
 afrazier90@gmail.com   
 rfuller24@gmail.com    
(96 rows, truncated for display at 20)

        Correct!

SELECT email FROM salespeople WHERE region IN ('Northwest', 'Southwest');

        Moving on...


Problem 12
----------

Using all these tools, we can bring them together to do fairly complex
queries that match many different rows. Using what you've learned, write a
query that combines column selection, an 'in' clause, and string wildcards.

Task: Write a query that shows the email, first name, and last name of all
salespeople in either the Northwest or Southwest regions whose last names start
with the letter 'M'.

SQL [12]> SELECT email, first_name, last_name FROM salespeople WHERE region IN ('North  ... [12]> ;
There was a problem with your SQL syntax:

        unterminated quoted string at or near "'North
;"
LINE 2: ...rst_name, last_name FROM salespeople WHERE region IN ('North
                                                                 ^



SQL [12]> SELECT email, first_name, last_name FROM salespeople WHERE region IN
... [12]> ('Northwest', 'Southwest') AND last_name LIKE 'M%';

         email         | first_name | last_name 
-----------------------+------------+-----------
 rmartinez98@gmail.com | Ruth       | Martinez  
 jmiller60@gmail.com   | Julia      | Miller    
 hmyers61@gmail.com    | Helen      | Myers     
 lmorris25@gmail.com   | Laura      | Morris    
 tmendoza27@gmail.com  | Teresa     | Mendoza   
 tmendoza1@gmail.com   | Tammy      | Mendoza   
 jmartin88@gmail.com   | Janice     | Martin    
 cmoreno1@gmail.com    | Catherine  | Moreno    
 jmccoy35@gmail.com    | Judith     | Mccoy     
 mmitchell73@gmail.com | Melissa    | Mitchell  
(10 rows)

        Correct!

SELECT email, first_name, last_name FROM salespeople WHERE region IN
('Northwest', 'Southwest') AND last_name LIKE 'M%';

        Moving on...


Problem 13
----------

An odd feature of sql is the ability to select data out of a
table that doesn't actually exist. Certain kinds of data can be computed on the
fly and be made to look as if they were part of the table. We'll use this to
query for melon price in USD and EUR, where one column will be computed from
the other.

Examples: http://sqlzoo.net/wiki/SELECT_basics -- 2

Task: Write a query that shows the melon type, common name, price, and the
price of the melon given in euros. The 'melons' table has prices in dollars,
and the dollar to euro conversion rate is 0.73.


SQL [13]> SELECT melon_type, common_name, price, price*.73 AS euro_price FROM melons;

 melon_type |           common_name            |  price   | euro_price 
------------+----------------------------------+----------+------------
 Musk       | Honeydew                         |     1.00 |     0.7300 
 Hybrid     | Crane                            |     2.50 |     1.8250 
 Musk       | Casaba                           |     2.50 |     1.8250 
 Musk       | Cantaloupe                       |     0.99 |     0.7227 
 Musk       | Persian Melon                    |     3.00 |     2.1900 
 Musk       | Christmas Melon                  |     5.50 |     4.0150 
 Musk       | Armenian Cucumber                |     4.50 |     3.2850 
 Hybrid     | Galia                            |     3.75 |     2.7375 
 Winter     | Winter Melon                     |     0.99 |     0.7227 
 Musk       | Canary                           |     1.50 |     1.0950 
 Musk       | Hami                             |     2.75 |     2.0075 
 Watermelon | Ali Baba Watermelon              |     2.50 |     1.8250 
 Watermelon | Arkansas Black Watermelon        |     4.00 |     2.9200 
 Watermelon | Blacktail Mountain Watermelon    |     2.75 |     2.0075 
 Watermelon | Carolina Cross 180 Watermelon    |     4.25 |     3.1025 
 Watermelon | Charleston Gray Watermelon       |     2.00 |     1.4600 
 Watermelon | Chris Cross Watermelon           |     2.50 |     1.8250 
 Watermelon | Congo Watermelon                 |     2.00 |     1.4600 
 Watermelon | Cream of Saskatchewan Watermelon |     2.50 |     1.8250 
 Watermelon | Crimson Sweet Watermelon         |     1.75 |     1.2775 
(67 rows, truncated for display at 20)

        Correct!

SELECT melon_type, common_name, price, price*.73 AS euro_price FROM melons;

        Moving on...


Problem 14
----------

Similar to the 'computed' columns, SQL has a set of predefined 'aggregate'
functions that operate on an entire set of matched rows. Aggregate functions
condense a set of rows into a single row. An example of this kind of aggregate
operation is a 'count'. It simply counts up all the matched rows and returns a
single record in their place.

Example: http://sqlzoo.net/wiki/The_nobel_table_can_be_used_to_practice_more_SUM_and_COUNT_functions. -- 1

Task: Write a query that shows the total number of customers in our customer
table.

SQL [14]> SELECT COUNT(*) FROM melons;

   count    
------------
         67 
(1 rows)

(results do not match answer)


SQL [14]> SELECT COUNT(*) FROM salespeople;

   count    
------------
        250 
(1 rows)

(results do not match answer)


SQL [14]> SELECT COUNT(*) FROM customers;

   count    
------------
       1000 
(1 rows)

        Correct!

SELECT COUNT(*) FROM customers;

        Moving on...


Problem 15
----------

We can combine aggregate functions with the standard SQL clauses we've seen
so far. In this exercise, you will combine a count clause with a where clause
to limit what is counted.

Task: Write a query that counts the number of orders (in the orders table) shipped to California.

SQL [15]> SELECT COUNT(*) FROM orders WHERE shipto_state = 'California';

   count    
------------
          0 
(1 rows)

(results do not match answer)


SQL [15]> SELECT COUNT(*) FROM orders WHERE shipto_state = 'CA';

   count    
------------
        187 
(1 rows)

        Correct!

SELECT COUNT(*) FROM orders WHERE shipto_state = 'CA';

        Moving on...


Problem 16
----------

Aggregate functions work on column lists. When we're counting things, it
doesn't matter which column we count, there should be the same number of each
column across all the records. For this reason, it is customary to execute the
count on all the columns in the query. With other aggregate functions, the
column we use can be meaningful, for example, if we are totaling up the values
in a single column.

Examples: http://sqlzoo.net/wiki/SUM_and_COUNT -- 1
          http://sqlzoo.net/wiki/The_nobel_table_can_be_used_to_practice_more_SUM_and_COUNT_functions. -- 3

Task: Write a query that shows the total amount of money spent across all melon
orders.

SQL [16]> SELECT SUM(price) FROM melons;

   sum    
----------
   420.73 
(1 rows)

(results do not match answer)


SQL [16]> SELECT SUM(order_total) FROM orders;

   sum    
----------
 2979590.48 
(1 rows)

        Correct!

SELECT SUM(order_total) FROM orders;

        Moving on...


Problem 17
----------

Another useful aggregate function is the average.

Task: Write a query that shows the average order cost.

SQL [17]> SELECT AVG(order_total) FROM orders;

   avg    
----------
 297.9590480000000000 
(1 rows)

        Correct!

SELECT AVG(order_total) FROM orders;

        Moving on...


Problem 18
----------

Lastly, we have aggregate functions to select both the minimum or maximum values 
of a column.

Task: Write a query that shows the order total that was lowest in price.

SQL [18]> SELECT MIN(order_total) FROM orders;

   min    
----------
     2.57 
(1 rows)

        Correct!

SELECT MIN(order_total) FROM orders;

        Moving on...


Problem 19
----------

Now, for a change of pace, we're going to try to write queries that can
show us information that spans multiple tables. Before we can do that though, 
a quick review.

Task: Write a query that fetches the id of the customer whose email is
'pclark74@gmail.com'.

SQL [19]> SELECT id FROM customers WHERE email='pclark74@gmail.com';

  id   
-------
   100 
(1 rows)

        Correct!

SELECT id FROM customers WHERE email='pclark74@gmail.com';

        Moving on...


Problem 20
----------

We've identified Phyllis in our previous exercise to be customer number 100.

Task: Write a query that shows the id, status and order_total for all orders 
made by customer 100.

SQL [20]> SELECT id, status, order_total FROM customers WHERE id=100;
There was a problem with your SQL syntax:

        column "status" does not exist
LINE 2: SELECT id, status, order_total FROM customers WHERE id=100;
                   ^



SQL [20]> SELECT id, status, order_total FROM orders WHERE customer_id=100;

  id   |   status   | order_total 
-------+------------+-------------
   449 | Delivered  |      102.40 
  2579 | New        |      636.59 
  2855 | Delivered  |      450.33 
  3239 | Processing |      437.40 
  7482 | Processing |      362.38 
  9460 | New        |       28.01 
(6 rows)

        Correct!

SELECT id, status, order_total FROM orders WHERE customer_id=100;

        Moving on...


Problem 21
----------

Our first technique for writing queries that cross tables is the subselect.
It lets us use the results of a query in the where clause of another query. In
this case, we can query the 'orders' table for orders matching the 'id' that
comes out of a different query. In this way, we can combine the previous two
queries into a single query.

Examples: http://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial -- 1

Task: Write a single query that shows the id, status, and order total for all
orders made by 'pclark74@gmail.com'. Use a subselect to do this.


SQL [21]> SELECT id, status, order_total FROM orders WHERE customer_id IN
... [21]> (SELECT id FROM customers WHERE email='pclark74@gmail.com');

  id   |   status   | order_total 
-------+------------+-------------
   449 | Delivered  |      102.40 
  2579 | New        |      636.59 
  2855 | Delivered  |      450.33 
  3239 | Processing |      437.40 
  7482 | Processing |      362.38 
  9460 | New        |       28.01 
(6 rows)

        Correct!

SELECT id, status, order_total FROM orders WHERE customer_id IN
(SELECT id FROM customers WHERE email='pclark74@gmail.com');

        Moving on...


Problem 22
----------

Another way we can span tables is the 'join'. Joins can be complicated, but
one way to visualize them is as a venn diagram. Imagine you have a query that
selects all the customers in the customer table, and another query that selects
all the orders in the orders table. You can treat these two queries as the two
circles in a venn diagram. The intersection of these two sets, then, is all the
orders, attached to their respective customers.
Using a join, we can get the same results as the previous query by connecting
orders to the customers that made them, then filtering on the email of the
resulting join.

Examples: http://sqlzoo.net/wiki/The_JOIN_operation -- 1, 2, 3, 4

Task: Write a query that shows the id, status, and order total for all orders
made by 'pclark74@gmail.com'. Use a join to do this.
