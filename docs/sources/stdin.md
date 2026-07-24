# STDIN

The `stdin` source allows AQL to query data streamed through standard input.

Unlike file-based sources such as `json()`, `csv()`, `log()`, `xml()`, and `yaml()`, the `stdin` source reads data directly from a Unix pipeline.

Supported formats include:

* JSON
* CSV
* LOG
* XML
* YAML

AQL automatically detects and parses supported input formats.

---

## When to Use STDIN

Use `stdin` when data is being streamed from another command or when integrating AQL into shell scripts, automation workflows, and command-line pipelines.

Examples:

```bash
cat data.json | aegis query "SELECT *"
```

```bash
curl https://example.com/data.json | aegis query "SELECT *"
```

```bash
echo '{"id":1,"name":"Alice"}' | aegis query "SELECT *"
```

---

## Supported Query Patterns

### Discover Available Fields

```bash
cat data.json | aegis query "SHOW stdin"
```

### Inspect the Schema

```bash
cat data.json | aegis query "DESCRIBE stdin"
```

### Query All Data

```bash
cat data.json | aegis query "SELECT *"
```

```bash
cat data.json | aegis query "SELECT * FROM stdin"
```

### Select Specific Fields

```bash
cat data.json | aegis query "SELECT id, name"
```

```bash
cat data.json | aegis query "SELECT id, name FROM stdin"
```

---

## Filter Results

AQL supports the following filtering operators when querying stdin:

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
cat data.json | aegis query "SELECT * FROM stdin WHERE id = 1"
```

### Not Equal

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id != 1"
```

### Greater Than

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id > 10"
```

### Greater Than or Equal

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id >= 10"
```

### Less Than

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id < 10"
```

### Less Than or Equal

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id <= 10"
```

### IN

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id IN [1, 5]"
```

---

## Select and Filter

Retrieve specific fields from matching records:

```bash
cat data.json | aegis query "SELECT name FROM stdin WHERE id = 1"
```

```bash
cat data.json | aegis query "SELECT name FROM stdin WHERE id > 10"
```

```bash
cat data.json | aegis query "SELECT name FROM stdin WHERE id IN [1, 5]"
```

---

## Query Grammar

The following query patterns are supported:

```sql
SHOW stdin
```

```sql
DESCRIBE stdin
```

```sql
SELECT *
```

```sql
SELECT * FROM stdin
```

```sql
SELECT field1, field2
```

```sql
SELECT field1, field2 FROM stdin
```

```sql
SELECT *
FROM stdin
WHERE field = value
```

```sql
SELECT *
FROM stdin
WHERE field != value
```

```sql
SELECT *
FROM stdin
WHERE field > value
```

```sql
SELECT *
FROM stdin
WHERE field >= value
```

```sql
SELECT *
FROM stdin
WHERE field < value
```

```sql
SELECT *
FROM stdin
WHERE field <= value
```

```sql
SELECT *
FROM stdin
WHERE field IN [value1, value2]
```

```sql
SELECT field1, field2
FROM stdin
WHERE condition
```

---

## JSON Example

Input:

```json
[
  {
    "id": 1,
    "name": "Alice"
  },
  {
    "id": 2,
    "name": "Bob"
  }
]
```

Query:

```bash
cat users.json | aegis query "SELECT id, name"
```

Result:

```text
1 Alice
2 Bob
```

Filter results:

```bash
cat users.json | aegis query "SELECT * FROM stdin WHERE id > 1"
```

---

## CSV Example

Input:

```csv
id,name
1,Alice
2,Bob
```

Query:

```bash
cat users.csv | aegis query "SELECT *"
```

Filter results:

```bash
cat users.csv | aegis query "SELECT * FROM stdin WHERE id = 1"
```

---

## XML Example

Query:

```bash
cat users.xml | aegis query "SELECT *"
```

---

## YAML Example

Query:

```bash
cat users.yml | aegis query "SELECT *"
```

---

## Using Echo

AQL can query inline data streamed directly from the shell.

JSON:

```bash
echo '{"id":1,"name":"Alice"}' | aegis query "SELECT *"
```

CSV:

```bash
echo 'id,name
1,Alice' | aegis query "SELECT *"
```

YAML:

```bash
echo 'id: 1
name: Alice' | aegis query "SELECT *"
```

Filter inline data:

```bash
echo '{"id":1,"name":"Alice"}' | aegis query "SELECT * WHERE id = 1"
```

---

## Common Workflows

### Inspect Incoming Data

```bash
cat data.json | aegis query "DESCRIBE stdin"
```

Useful when exploring an unfamiliar dataset.

---

### Filter Streamed Data

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id = 1"
```

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id > 100"
```

Useful for extracting specific records from larger datasets.

---

### Select Only Required Fields

```bash
cat data.json | aegis query "SELECT id, name FROM stdin"
```

Useful for reducing output and focusing on relevant data.

---

### Find Multiple Records

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id IN [1, 5]"
```

Useful for retrieving a specific set of records.

---

### Use AQL in Shell Pipelines

```bash
curl https://example.com/users.json \
| aegis query "SELECT id, name FROM stdin"
```

Useful for automation and command-line workflows.

---

## Query Patterns

Select all records:

```sql
SELECT *
FROM stdin
```

Select specific fields:

```sql
SELECT id, name
FROM stdin
```

Filter by equality:

```sql
SELECT *
FROM stdin
WHERE id = 1
```

Filter by inequality:

```sql
SELECT *
FROM stdin
WHERE id != 1
```

Filter values above a threshold:

```sql
SELECT *
FROM stdin
WHERE id > 100
```

Filter values at or above a threshold:

```sql
SELECT *
FROM stdin
WHERE id >= 100
```

Filter values below a threshold:

```sql
SELECT *
FROM stdin
WHERE id < 100
```

Filter values at or below a threshold:

```sql
SELECT *
FROM stdin
WHERE id <= 100
```

Filter multiple values:

```sql
SELECT *
FROM stdin
WHERE id IN [1, 5]
```

---

## Related Sources

* json()
* csv()
* log()
* xml()
* yaml()

Use file-based sources when querying data stored on disk, and use `stdin` when data is streamed from another command or pipeline. All filtering operators supported by file-based sources are also supported by `stdin`.
