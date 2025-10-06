-- =========================================
-- Lesson 1: Introduction to SQL and the Dataset
-- =========================================
/*
This intro will use the plants dataset to demonstrate basic SQL queries. But first, let's cover some foundational concepts.

What is SQL?

SQL stands for Structured Query Language. It is a standard programming language used to
manage and manipulate relational databases. SQL lets you create, read, update, and 
delete data stored in a database.

What is a relational database?

A relational database is a type of database that stores data in tables (like spreadsheets), 
where each table consists of rows and columns. Each row represents a record, and each column 
represents a field of the record. Tables can be related to each other through keys (primary and foreign keys).

SQLite is an example of a relational database. Other common relational databases include Google BigQuery, MySQL, PostgreSQL,
Microsoft SQL Server, and Oracle Database.
*/

-- View the first 5 rows of the dataset
SELECT * 
FROM plants 
LIMIT 5;

-- =========================================
-- Lesson 2: Selecting and Filtering Data
-- =========================================

-- Show plant names and their sunlight requirements
SELECT plant_name, sunlight
FROM plants;

-- Find all plants that are fast growing
SELECT * FROM plants 
WHERE growth = 'fast';
-- Find all plants that are fast growing and require full sunlight
SELECT * FROM plants 
WHERE growth = 'fast' 
    AND sunlight = 'full sunlight';

-- =========================================
-- Lesson 3: Sorting and Limiting Results
-- =========================================

-- List plants by fastest growth rate
SELECT plant_name, growth 
FROM plants 
ORDER BY growth DESC, plant_name ASC;

-- Show the first 10 plants alphabetically
SELECT * FROM plants 
ORDER BY plant_name ASC
LIMIT 10;

-- =========================================
-- Lesson 4: Aggregation and Grouping
-- =========================================

-- How many plants require each type of sunlight?
SELECT sunlight, COUNT(*) AS num_plants 
FROM plants 
GROUP BY sunlight;

-- What is the average name length for fast-growing plants?
SELECT AVG(LENGTH(plant_name)) 
FROM plants 
WHERE growth = 'fast';

-- =========================================
-- Lesson 5: Pattern Matching and Advanced Filtering
-- =========================================

-- Find all plants with "Palm" in their name
SELECT plant_name 
FROM plants 
WHERE plant_name LIKE '%Palm%';

-- =========================================
-- Lesson 7: Review and Challenge Exercises
-- =========================================

-- 1. Find all plants that do not require fertilization and grow slowly
SELECT plant_name 
FROM plants 
WHERE fertilization_type = 'No' 
    AND growth = 'slow';

-- 2. List the top 5 distinct plants (alphabetically) that grow fast and require indirect sunlight
SELECT DISTINCT plant_name, growth FROM plants
WHERE growth = 'fast' 
    AND sunlight = 'indirect sunlight'
ORDER BY plant_name ASC
LIMIT 5;

-- 3. How many unique soil categories are there?
SELECT COUNT(DISTINCT soil) 
FROM plants;

-- 4. Find all plants whose names start with the letter 'A'
SELECT plant_name 
FROM plants 
WHERE lower(plant_name) LIKE 'a%';
