# Filtering

Filtering allows you to limit query results to records that match specific conditions.

In AQL, filtering is performed using the `WHERE` clause.

---

## Basic Syntax

```sql
SELECT *
FROM source
WHERE condition
```

Example:

```sql
SELECT *
FROM clusters
WHERE cluster_id = 1
```

Only records matching the condition are returned.

---

## Supported Operators

AQL supports the following filtering operators:

| Operator | Description               |
| -------- | ------------------------- |
| `=`      | Equal to                  |
| `!=`     | Not equal to              |
| `>`      | Greater than              |
| `>=`     | Greater than or equal to  |
| `<`      | Less than                 |
| `<=`     | Less than or equal to     |
| `IN`     | Match any value in a list |

---

## Equality Filters

Retrieve records where a field matches a value.

```sql
SELECT *
FROM clusters
WHERE cluster_id = 1
```

Select specific fields:

```sql
SELECT error_type
FROM clusters
WHERE cluster_id = 1
```

File sources work the same way:

```sql
SELECT *
FROM csv('data.csv')
WHERE id = 1
```

```sql
SELECT *
FROM json('data.json')
WHERE id = 1
```

---

## Not Equal Filters

Return records where a field does not match a value.

```sql
SELECT *
FROM tests
WHERE status != "passed"
```

```sql
SELECT name, status
FROM tests
WHERE status != "passed"
```

---

## Greater Than Filters

Return records with values larger than the specified value.

```sql
SELECT *
FROM failures
WHERE count > 10
```

```sql
SELECT *
FROM tests
WHERE duration_ms > 5000
```

---

## Greater Than or Equal Filters

```sql
SELECT *
FROM failures
WHERE count >= 10
```

```sql
SELECT *
FROM tests
WHERE duration_ms >= 5000
```

---

## Less Than Filters

Return records with values smaller than the specified value.

```sql
SELECT *
FROM tests
WHERE duration_ms < 1000
```

```sql
SELECT *
FROM failures
WHERE count < 5
```

---

## Less Than or Equal Filters

```sql
SELECT *
FROM tests
WHERE duration_ms <= 1000
```

```sql
SELECT *
FROM failures
WHERE count <= 5
```

---

## IN Filters

Match multiple values using the `IN` operator.

```sql
SELECT *
FROM clusters
WHERE cluster_id IN [1, 5]
```

Select specific fields:

```sql
SELECT error_type
FROM clusters
WHERE cluster_id IN [1, 5]
```

File sources:

```sql
SELECT *
FROM csv('data.csv')
WHERE id IN [1, 5]
```

```sql
SELECT *
FROM json('data.json')
WHERE id IN [1, 5]
```

---

## Filtering Standard Input

Filtering works with stdin just like any other source.

Query all matching records:

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id = 1"
```

Select specific fields:

```bash
cat data.json | aegis query "SELECT name FROM stdin WHERE id = 1"
```

Use comparison operators:

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id > 10"
```

Use IN filters:

```bash
cat data.json | aegis query "SELECT * FROM stdin WHERE id IN [1, 5]"
```

---

## Combining Projection and Filtering

Filtering is commonly used together with field selection.

Instead of returning every field:

```sql
SELECT *
FROM clusters
WHERE cluster_id = 1
```

Return only the fields you need:

```sql
SELECT cluster_id, error_type
FROM clusters
WHERE cluster_id = 1
```

This reduces output and focuses the query on relevant information.

---

## Common Workflows

### Find a Specific Cluster

```sql
SELECT *
FROM clusters
WHERE cluster_id = 1
```

---

### Find Multiple Clusters

```sql
SELECT *
FROM clusters
WHERE cluster_id IN [1, 5]
```

---

### Find Failed Tests

```sql
SELECT *
FROM tests
WHERE status != "passed"
```

---

### Find Long-Running Tests

```sql
SELECT *
FROM tests
WHERE duration_ms > 5000
```

---

### Find Small Failure Groups

```sql
SELECT *
FROM failures
WHERE count < 5
```

---

### Find Records in a CSV File

```sql
SELECT *
FROM csv('users.csv')
WHERE id = 1
```

---

### Filter JSON Data

```sql
SELECT *
FROM json('users.json')
WHERE id >= 100
```

---

### Filter Streamed Data

```bash
cat users.json | aegis query "SELECT * FROM stdin WHERE id = 1"
```

---

## Query Patterns

Filter all fields:

```sql
SELECT *
FROM source
WHERE field = value
```

Filter selected fields:

```sql
SELECT field1, field2
FROM source
WHERE field = value
```

Match multiple values:

```sql
SELECT *
FROM source
WHERE field IN [1, 2, 3]
```

Find values greater than a threshold:

```sql
SELECT *
FROM source
WHERE field > value
```

Find values less than a threshold:

```sql
SELECT *
FROM source
WHERE field < value
```

Exclude values:

```sql
SELECT *
FROM source
WHERE field != value
```

Filter streamed data:

```sql
SELECT *
FROM stdin
WHERE field = value
```

---

## Related Topics

* Projections
* Sources
* STDIN
* CSV
* JSON
* XML
* YAML

Filtering can be applied to any AQL source that returns structured records. AQL currently supports single-condition filtering using comparison operators and the `IN` operator.
