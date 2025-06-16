-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT CHECK(role IN ('chief_admin', 'department_admin', 'user')),
    department_id INTEGER
);

-- Departments table
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

-- Files table
CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    content BLOB,
    uploaded_by INTEGER,
    department_id INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Audit log table
CREATE TABLE IF NOT EXISTS audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    action TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
