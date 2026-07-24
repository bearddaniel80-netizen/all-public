# CSV

The `yaml()` source allows AQL to query CSV files using standard SQL-inspired syntax.

CSV files are treated as tabular data sources, making them accessible through the same query interface used for Aegis data, databases, and other supported formats.

---

## Discover the Source

List all available sources:

```bash
aegis query "SHOW sources"
```

Inspect a CSV file:

```bash
aegis query "SHOW yaml('data.yaml')"
```

---

## Inspect the Schema

View available columns:

```bash
aegis query "DESCRIBE yaml('data.yaml')"
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
aegis query "SELECT * FROM yaml('data.yaml')"
```

---

## Select Specific Columns

Retrieve only the columns you need:

```bash
aegis query "SELECT id FROM yaml('data.yaml')"
```

```bash
aegis query "SELECT id, name FROM yaml('data.yaml')"
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
aegis query "SELECT * FROM yaml('data.yaml') WHERE id = 1"
```

### Not Equal

```bash
aegis query "SELECT * FROM yaml('data.yaml') WHERE department != 'Sales'"
```

### Greater Than

```bash
aegis query "SELECT * FROM yaml('data.yaml') WHERE id > 100"
```

### Greater Than or Equal

```bash
aegis query "SELECT * FROM yaml('data.yaml') WHERE id >= 100"
```

### Less Than

```bash
aegis query "SELECT * FROM yaml('data.yaml') WHERE id < 100"
```

### Less Than or Equal

```bash
aegis query "SELECT * FROM yaml('data.yaml') WHERE id <= 100"
```

### IN

```bash
aegis query "SELECT * FROM yaml('data.yaml') WHERE id IN [1, 5]"
```

---

## Query CSV Data from Standard Input

AQL can read CSV data directly from stdin.

Pipe a file into AQL:

```bash
cat data.yaml | aegis query "SELECT *"
```

Explicitly reference stdin:

```bash
cat data.yaml | aegis query "SELECT * FROM stdin"
```

Select specific columns:

```bash
cat data.yaml | aegis query "SELECT id, name FROM stdin"
```

Apply filters:

```bash
cat data.yaml | aegis query "SELECT * FROM stdin WHERE id = 1"
```

```bash
cat data.yaml | aegis query "SELECT * FROM stdin WHERE id > 10"
```

```bash
cat data.yaml | aegis query "SELECT * FROM stdin WHERE id IN [1, 5]"
```

---

## Example CSV File

```yaml
id,name,email
1,Alice,alice@example.com
2,Bob,bob@example.com
3,Carol,carol@example.com
```

Query:

```bash
aegis query "SELECT id, name FROM yaml('data.yaml')"
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
aegis query "DESCRIBE yaml('data.yaml')"
```

Then query the contents:

```bash
aegis query "SELECT * FROM yaml('data.yaml')"
```

---

### Extract Specific Data

```bash
aegis query "SELECT id, email FROM yaml('data.yaml')"
```

---

### Find a Specific Record

```bash
aegis query "SELECT * FROM yaml('data.yaml') WHERE id = 1"
```

---

### Find Records Above a Threshold

```bash
aegis query "SELECT * FROM yaml('data.yaml') WHERE id > 100"
```

---

### Exclude Records

```bash
aegis query "SELECT * FROM yaml('data.yaml') WHERE department != 'Sales'"
```

---

### Find Multiple Records

```bash
aegis query "SELECT * FROM yaml('data.yaml') WHERE id IN [1, 5]"
```

---

### Process Data in a Pipeline

```bash
cat data.yaml | aegis query "SELECT * FROM stdin"
```

Useful when integrating AQL into shell scripts and automation workflows.

---

## Query Patterns

Select all columns:

```sql
SELECT * FROM yaml('data.yaml')
```

Select specific columns:

```sql
SELECT id, name
FROM yaml('data.yaml')
```

Filter records by equality:

```sql
SELECT *
FROM yaml('data.yaml')
WHERE id = 1
```

Filter records by inequality:

```sql
SELECT *
FROM yaml('data.yaml')
WHERE id != 1
```

Filter records above a value:

```sql
SELECT *
FROM yaml('data.yaml')
WHERE id > 100
```

Filter records at or above a value:

```sql
SELECT *
FROM yaml('data.yaml')
WHERE id >= 100
```

Filter records below a value:

```sql
SELECT *
FROM yaml('data.yaml')
WHERE id < 100
```

Filter records at or below a value:

```sql
SELECT *
FROM yaml('data.yaml')
WHERE id <= 100
```

Filter multiple values:

```sql
SELECT *
FROM yaml('data.yaml')
WHERE id IN [1, 5]
```

---

## Related Sources

* json()
* csv()
* log()
* xml()
* stdin

All file-based sources support the same AQL query patterns, including projection, filtering, and value matching through comparison operators and the `IN` operator.
