# Practical SQL Walkthrough

This folder teaches SQL by doing small useful tasks against a fake AI internship database.

You will use SQLite. No server, account, or installation needed.

## Start

From PowerShell:

```powershell
cd C:\Users\emanu\Desktop\HuggingFace\sql_practice
python setup_db.py
```

Then run one query:

```powershell
python run_query.py "SELECT * FROM applications;"
```

Or interactive one-query mode:

```powershell
python run_query.py
```

Or use the interactive SQL shell so you can type SQL directly without wrapping it
in a Python command:

```powershell
python sql_shell.py
```

Then type:

```sql
SELECT * FROM applications;
```

Use `.tables`, `.schema applications`, `.help`, and `.exit` inside the shell.

## Tables

`applications`

- internship applications
- columns: company, role, field, location, status, applied_date, salary_sek

`projects`

- your AI/software projects
- columns: name, category, main_language, difficulty, completed

`skills`

- skills connected to project evidence
- columns: name, category, level, project_id

`learning_logs`

- study/practice time
- columns: topic, minutes, log_date, notes

## Mental Model

SQL is basically asking tables questions.

```sql
SELECT columns
FROM table
WHERE condition
ORDER BY column;
```

Example:

```sql
SELECT company, role, status
FROM applications
WHERE status = 'applied';
```

Means:

> Show me company, role, and status from the applications table, but only rows where status is applied.

## Level 1: Look At Data

Show all applications:

```sql
SELECT * FROM applications;
```

Show only company and role:

```sql
SELECT company, role FROM applications;
```

Show all projects:

```sql
SELECT * FROM projects;
```

## Level 2: Filter Data

Find applications in Stockholm:

```sql
SELECT company, role, location
FROM applications
WHERE location = 'Stockholm';
```

Find LLM-related roles:

```sql
SELECT company, role, field
FROM applications
WHERE field = 'LLM Systems';
```

Find salaries above 28,000:

```sql
SELECT company, role, salary_sek
FROM applications
WHERE salary_sek > 28000;
```

## Level 3: Sort And Limit

Highest salary first:

```sql
SELECT company, role, salary_sek
FROM applications
ORDER BY salary_sek DESC;
```

Top 3:

```sql
SELECT company, role, salary_sek
FROM applications
ORDER BY salary_sek DESC
LIMIT 3;
```

## Level 4: Count And Group

Count all applications:

```sql
SELECT COUNT(*) AS total_applications
FROM applications;
```

Count by status:

```sql
SELECT status, COUNT(*) AS count
FROM applications
GROUP BY status;
```

Average salary by field:

```sql
SELECT field, AVG(salary_sek) AS avg_salary
FROM applications
WHERE salary_sek > 0
GROUP BY field;
```

## Level 5: Join Tables

Skills can point to a project through `project_id`.

```sql
SELECT skills.name AS skill, projects.name AS project
FROM skills
JOIN projects ON skills.project_id = projects.id;
```

This means:

> Match skills to projects where `skills.project_id` equals `projects.id`.

## Level 6: Realistic Questions

Which completed Python projects support AI skills?

```sql
SELECT projects.name, projects.category, skills.name AS skill
FROM projects
JOIN skills ON skills.project_id = projects.id
WHERE projects.completed = 1
  AND projects.main_language = 'Python'
  AND skills.category LIKE '%AI%';
```

How much time was spent learning each topic?

```sql
SELECT topic, SUM(minutes) AS total_minutes
FROM learning_logs
GROUP BY topic
ORDER BY total_minutes DESC;
```

## Your First Mission

Run these, one by one:

```sql
SELECT * FROM applications;
SELECT company, role FROM applications;
SELECT company, role FROM applications WHERE status = 'applied';
SELECT status, COUNT(*) FROM applications GROUP BY status;
SELECT skills.name, projects.name FROM skills JOIN projects ON skills.project_id = projects.id;
```

Then move to `exercises.sql`.
