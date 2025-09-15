# CC Plants
This README file will contain useful information about how to set-up and use the CC Plants repo.

**Important Note:**
This documentation assumes you are using a Mac OS computer, which comes with some software used in this set-up already installed. Attempting to follow these instructions using a Windows or Linux computer may require additional steps.

## Set-up Dataset

If you want to set-up the dataset from scratch (or replicate this process for a different project), follow the steps below. Otherwise, skip these steps and simply use the `plants.db` database that is in the `/data` folder in this repo.

1. Download the dataset from [Plants Growth and Care Recommendations](https://www.kaggle.com/datasets/aribashafaqat/plants-growth-and-care-recommendations/data) from Kaggle. You will need to create a Kaggle account first.
2. Create a database from the csv (using SQLite)
    * In a terminal, run `sqlite3 plants.db`. This will open a SQLite prompt
    * In the SQLite prompt, copy and paste the CREATE TABLE SQL query found in `/scripts/setup.sql`
    * In the SQLite prompt, run `.mode csv` 
    * In the SQLite prompt, run `.import /path/to/cc-plants/data/plants.csv plants`
        * Make sure in the command above that you replace the file path with the fully specified file path to your `plants.csv` file (e.g., `/Users/justin.lien/Downloads/plants.csv`)
    * In the SQLite prompt, test your new database using an example query, e.g., `SELECT COUNT(*) FROM plants;`


1. Navigate to repo
2. 