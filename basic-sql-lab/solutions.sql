-- Solutions

-- 1
SELECT * FROM applications;

-- 2
SELECT company, role, status FROM applications;

-- 3
SELECT company, role, status
FROM applications
WHERE status = 'applied';

-- 4
SELECT company, role, location
FROM applications
WHERE location != 'Stockholm';

-- 5
SELECT company, role, salary_sek
FROM applications
WHERE salary_sek >= 29000;

-- 6
SELECT company, role, salary_sek
FROM applications
ORDER BY salary_sek DESC;

-- 7
SELECT COUNT(*) AS total_applications
FROM applications;

-- 8
SELECT status, COUNT(*) AS count
FROM applications
GROUP BY status;

-- 9
SELECT name, category, main_language
FROM projects
WHERE completed = 1;

-- 10
SELECT name, category, difficulty
FROM projects
WHERE difficulty >= 4;

-- 11
SELECT name, category, level
FROM skills
WHERE category = 'AI';

-- 12
SELECT skills.name AS skill, projects.name AS supporting_project
FROM skills
JOIN projects ON skills.project_id = projects.id;

-- 13
SELECT name, category, level
FROM skills
WHERE project_id IS NULL;

-- 14
SELECT topic, SUM(minutes) AS total_minutes
FROM learning_logs
GROUP BY topic;

-- 15
SELECT topic, SUM(minutes) AS total_minutes
FROM learning_logs
GROUP BY topic
ORDER BY total_minutes DESC
LIMIT 3;

-- 16
SELECT projects.name AS project, projects.category, skills.name AS skill
FROM projects
JOIN skills ON skills.project_id = projects.id
WHERE projects.category IN ('RAG', 'Agents', 'LLM API', 'Edge AI', 'NLP');

-- 17
SELECT field, AVG(salary_sek) AS avg_salary
FROM applications
WHERE salary_sek > 0
GROUP BY field
HAVING AVG(salary_sek) > 28000;

-- 18
SELECT company, role, status
FROM applications
WHERE status IN ('applied', 'interview');
