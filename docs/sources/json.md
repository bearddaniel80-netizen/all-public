# CSV

The `json()` source allows AQL to query CSV files using standard SQL-inspired syntax.

CSV files are treated as tabular data sources, making them accessible through the same query interface used for Aegis data, databases, and other supported formats.

---

## Discover the Source

List all available sources:

```bash
aegis query "SHOW sources"
```

Inspect a CSV file:

```bash
aegis query "SHOW json('data.json')"
```

---

## Inspect the Schema

View available columns:

```bash
aegis query "DESCRIBE json('data.json')"
```

Example output:

```text
id
name
email
department
created_at
```

Column names are automatically derived from the CSV header row.

---

## Query a CSV File

Return all rows:

```bash
aegis query "SELECT * FROM json('data.json')"
```

---

## Select Specific Columns

Retrieve only the columns you need:

```bash
aegis query "SELECT id FROM json('data.json')"
```

```bash
aegis query "SELECT id, name FROM json('data.json')"
```

---

## Filter Rows

AQL supports the following filter operators when querying CSV files:

| Operator | Description               |
| -------- | ------------------------- |
| `=`      | Equal to                  |
| `!=`     | Not equal to              |
| `>`      | Greater than              |
| `>=`     | Greater than or equal to  |
| `<`      | Less than                 |
| `<=`     | Less than or equal to     |
| `IN`     | Match any value in a list |

### Equality

```bash
aegis query "SELECT * FROM json('data.json') WHERE id = 1"
```

### Not Equal

```bash
aegis query "SELECT * FROM json('data.json') WHERE department != 'Sales'"
```

### Greater Than

```bash
aegis query "SELECT * FROM json('data.json') WHERE id > 100"
```

### Greater Than or Equal

```bash
aegis query "SELECT * FROM json('data.json') WHERE id >= 100"
```

### Less Than

```bash
aegis query "SELECT * FROM json('data.json') WHERE id < 100"
```

### Less Than or Equal

```bash
aegis query "SELECT * FROM json('data.json') WHERE id <= 100"
```

### IN

```bash
aegis query "SELECT * FROM json('data.json') WHERE id IN [1, 5]"
```

---

## Query CSV Data from Standard Input

AQL can read CSV data directly from stdin.

Pipe a file into AQL:

```bash
cat data.json | aegis query "SELECT *"
```

Explicitly reference stdin:

```bash
cat data.json | aegis query "SELECT * FROM stdin"
```

Select specific columns:

```bash
cat data.json | aegis query "SELECT id, name FROM stdin"
```

Apply filters:

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id = 1"
```

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id > 10"
```

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id IN [1, 5]"
```

---

## Example CSV File

```json
id,name,email
1,Alice,alice@example.com
2,Bob,bob@example.com
3,Carol,carol@example.com
```

Query:

```bash
aegis query "SELECT id, name FROM json('data.json')"
```

Result:

```text
1 Alice
2 Bob
3 Carol
```

---

## Common Workflows

### Explore a New File

Inspect available columns:

```bash
aegis query "DESCRIBE json('data.json')"
```

Then query the contents:

```bash
aegis query "SELECT * FROM json('data.json')"
```

---

### Extract Specific Data

```bash
aegis query "SELECT id, email FROM json('data.json')"
```

---

### Find a Specific Record

```bash
aegis query "SELECT * FROM json('data.json') WHERE id = 1"
```

---

### Find Records Above a Threshold

```bash
aegis query "SELECT * FROM json('data.json') WHERE id > 100"
```

---

### Exclude Records

```bash
aegis query "SELECT * FROM json('data.json') WHERE department != 'Sales'"
```

---

### Find Multiple Records

```bash
aegis query "SELECT * FROM json('data.json') WHERE id IN [1, 5]"
```

---

### Process Data in a Pipeline

```bash
cat data.json | aegis query "SELECT * FROM stdin"
```

Useful when integrating AQL into shell scripts and automation workflows.

---

## Query Patterns

Select all columns:

```sql
SELECT * FROM json('data.json')
```

Select specific columns:

```sql
SELECT id, name
FROM json('data.json')
```

Filter records by equality:

```sql
SELECT *
FROM json('data.json')
WHERE id = 1
```

Filter records by inequality:

```sql
SELECT *
FROM json('data.json')
WHERE id != 1
```

Filter records above a value:

```sql
SELECT *
FROM json('data.json')
WHERE id > 100
```

Filter records at or above a value:

```sql
SELECT *
FROM json('data.json')
WHERE id >= 100
```

Filter records below a value:

```sql
SELECT *
FROM json('data.json')
WHERE id < 100
```

Filter records at or below a value:

```sql
SELECT *
FROM json('data.json')
WHERE id <= 100
```

Filter multiple values:

```sql
SELECT *
FROM json('data.json')
WHERE id IN [1, 5]
```

---

## Related Sources

* csv()
* log()
* xml()
* yaml()
* stdin

All file-based sources support the same AQL query patterns, including projection, filtering, and value matching through comparison operators and the `IN` operator.
