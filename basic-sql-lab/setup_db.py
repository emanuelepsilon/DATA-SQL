import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).with_name("ai_internship.db")


SCHEMA = """
DROP TABLE IF EXISTS applications;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS skills;
DROP TABLE IF EXISTS learning_logs;

CREATE TABLE applications (
    id INTEGER PRIMARY KEY,
    company TEXT NOT NULL,
    role TEXT NOT NULL,
    field TEXT NOT NULL,
    location TEXT NOT NULL,
    status TEXT NOT NULL,
    applied_date TEXT,
    salary_sek INTEGER
);

CREATE TABLE projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    main_language TEXT NOT NULL,
    difficulty INTEGER NOT NULL,
    completed INTEGER NOT NULL
);

CREATE TABLE skills (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    level TEXT NOT NULL,
    project_id INTEGER,
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

CREATE TABLE learning_logs (
    id INTEGER PRIMARY KEY,
    topic TEXT NOT NULL,
    minutes INTEGER NOT NULL,
    log_date TEXT NOT NULL,
    notes TEXT
);
"""


APPLICATIONS = [
    (1, "Northvolt", "ML Intern", "Machine Learning", "Stockholm", "applied", "2026-07-01", 28000),
    (2, "Spotify", "Data Science Intern", "Data", "Stockholm", "saved", None, 30000),
    (3, "Ericsson", "AI Engineer Intern", "LLM Systems", "Stockholm", "interview", "2026-07-03", 29000),
    (4, "Saab", "Computer Vision Intern", "Computer Vision", "Linkoping", "rejected", "2026-06-22", 27000),
    (5, "Klarna", "Analytics Intern", "Data", "Stockholm", "applied", "2026-07-05", 31000),
    (6, "Hugging Face", "Agents Intern", "LLM Systems", "Remote", "dream", None, 0),
    (7, "Volvo Cars", "Edge AI Intern", "Edge AI", "Gothenburg", "applied", "2026-07-10", 28500),
    (8, "Sectra", "Medical AI Intern", "Computer Vision", "Linkoping", "saved", None, 27500),
]


PROJECTS = [
    (1, "Bank RAG Assistant", "RAG", "Python", 4, 1),
    (2, "MCP Practice Server", "Agents", "Python", 3, 1),
    (3, "Gemini Terminal Agent", "LLM API", "Python", 3, 1),
    (4, "Edge Neural Network Thesis", "Edge AI", "Python", 5, 1),
    (5, "Toy Language Model", "NLP", "Python", 4, 1),
    (6, "C Performance Experiment", "Systems", "C", 3, 0),
]


SKILLS = [
    (1, "Python", "Programming", "strong", 1),
    (2, "MATLAB", "Programming", "strong", None),
    (3, "C", "Programming", "developing", 6),
    (4, "SQL", "Data", "basic", None),
    (5, "RAG", "AI", "comfortable", 1),
    (6, "MCP", "AI Infrastructure", "comfortable", 2),
    (7, "LLM APIs", "AI", "comfortable", 3),
    (8, "TensorFlow", "Deep Learning", "comfortable", 4),
    (9, "PyTorch", "Deep Learning", "practiced", 5),
    (10, "Git", "Development", "comfortable", None),
]


LEARNING_LOGS = [
    (1, "SQL SELECT basics", 35, "2026-07-14", "Started with SELECT and WHERE."),
    (2, "SQL filtering", 25, "2026-07-14", "Practiced status filters."),
    (3, "RAG", 90, "2026-07-12", "Built bank assistant examples."),
    (4, "MCP", 120, "2026-07-14", "Built server and terminal client."),
    (5, "Gemini API", 60, "2026-07-12", "Built terminal chat agent."),
    (6, "SQL joins", 45, "2026-07-15", "Next target."),
]


def main() -> None:
    connection = sqlite3.connect(DB_PATH)
    try:
        connection.executescript(SCHEMA)
        connection.executemany(
            "INSERT INTO applications VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            APPLICATIONS,
        )
        connection.executemany(
            "INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?)",
            PROJECTS,
        )
        connection.executemany(
            "INSERT INTO skills VALUES (?, ?, ?, ?, ?)",
            SKILLS,
        )
        connection.executemany(
            "INSERT INTO learning_logs VALUES (?, ?, ?, ?, ?)",
            LEARNING_LOGS,
        )
        connection.commit()
    finally:
        connection.close()

    print(f"Created {DB_PATH}")


if __name__ == "__main__":
    main()
