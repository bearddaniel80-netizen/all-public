# Querying with AQL

AQL provides a SQL-inspired interface for querying Aegis data, files, and standard input.

## Core Commands

### Discover Available Sources

List all registered query sources.

```bash
aegis query "SHOW sources"
```

Example output:

```text
clusters
failures
json()
csv()
xml()
yaml()
stdin
```

---

### Inspect a Source

View available fields and metadata.

```bash
aegis query "DESCRIBE clusters"
```

```bash
aegis query "DESCRIBE failures"
```

For file-based sources:

```bash
aegis query "DESCRIBE json('data.json')"
```

```bash
aegis query "DESCRIBE csv('data.csv')"
```

---

## Querying Aegis Data

### List Available Clusters

```bash
aegis query "SHOW clusters"
```

### Query All Clusters

```bash
aegis query "SELECT * FROM clusters"
```

### Filter Results

```bash
aegis query "SELECT * FROM clusters WHERE cluster_id = 1"
```

### Select Specific Fields

```bash
aegis query "SELECT error_type FROM clusters WHERE cluster_id = 1"
```

```bash
aegis query "SELECT cluster_id FROM clusters WHERE cluster_id = 1"
```

### Use IN Filters

```bash
aegis query "SELECT cluster_id FROM clusters WHERE cluster_id IN [1, 5]"
```

---

## Querying Failures

List failure data sources:

```bash
aegis query "SHOW failures"
```

Inspect schema:

```bash
aegis query "DESCRIBE failures"
```

Query all failures:

```bash
aegis query "SELECT * FROM failures"
```

---

## Querying JSON Files

Inspect file structure:

```bash
aegis query "SHOW json('data.json')"
```

```bash
aegis query "DESCRIBE json('data.json')"
```

Query file contents:

```bash
aegis query "SELECT * FROM json('data.json')"
```

---

## Querying CSV Files

Inspect file structure:

```bash
aegis query "SHOW csv('data.csv')"
```

```bash
aegis query "DESCRIBE csv('data.csv')"
```

Query file contents:

```bash
aegis query "SELECT * FROM csv('data.csv')"
```

---

## Querying XML Files

Inspect file structure:

```bash
aegis query "SHOW xml('data.xml')"
```

```bash
aegis query "DESCRIBE xml('data.xml')"
```

Query file contents:

```bash
aegis query "SELECT * FROM xml('data.xml')"
```

---

## Querying YAML Files

Inspect file structure:

```bash
aegis query "SHOW yaml('data.yml')"
```

```bash
aegis query "DESCRIBE yaml('data.yml')"
```

Query file contents:

```bash
aegis query "SELECT * FROM yaml('data.yml')"
```

---

## Querying Standard Input

AQL can read directly from stdin.

JSON:

```bash
cat data.json | aegis query "SELECT *"
```

```bash
cat data.json | aegis query "SELECT * FROM stdin"
```

CSV:

```bash
cat data.csv | aegis query "SELECT * FROM stdin"
```

XML:

```bash
cat data.xml | aegis query "SELECT * FROM stdin"
```

YAML:

```bash
cat data.yml | aegis query "SELECT * FROM stdin"
```

---

## Common Query Patterns

Query everything:

```sql
SELECT * FROM source
```

Select specific fields:

```sql
SELECT field1, field2
FROM source
```

Filter rows:

```sql
SELECT *
FROM source
WHERE field = value
```

Filter multiple values:

```sql
SELECT *
FROM source
WHERE field IN [1, 2, 3]
```

Inspect structure:

```sql
DESCRIBE source
```

Discover sources:

```sql
SHOW sources
```
