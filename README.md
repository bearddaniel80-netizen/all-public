# AQL (Aegis Query Language)

## AQL and Aegis

AQL powers the data layer of the Aegis ecosystem.

It enables Aegis to:

- Query test results
- Analyze failures
- Correlate system events
- Explore infrastructure state
- Retrieve application telemetry
- Build intelligent debugging workflows

While AQL can be used independently, it serves as a foundational technology within Aegis Prime.
---
## 📦 Installation

Build:

```bash
docker build \
    --target runtime \
    -t aql .
```

Run:

```bash
docker run -ti --rm \
    -v ./data:/app/data \
    aql bash
```
---

## One Query Language. Any Data Source.

AQL (Aegis Query Language) is a universal query language designed to query databases, APIs, files, streams, infrastructure, and application data through a single consistent interface.

Modern systems scatter information across dozens of technologies:

- PostgreSQL
- MySQL
- MongoDB
- Elasticsearch
- Kafka
- REST APIs
- GraphQL
- CSV files
- JSON documents
- Cloud services
- Log platforms

Every source introduces its own query language, tooling, authentication model, and operational complexity.

AQL provides a unified abstraction layer that allows engineers to query heterogeneous systems using a familiar SQL-inspired syntax.

---

## Table of Contents

- [AQL and Aegis](#aql-and-aegis)
- [Why AQL Exists](#why-aql-exists)
- [Core Principles](#core-principles)
- [Getting Started](./doc/getting-started.md)
- [Example Queries](#example-queries)
- [Beyond Traditional SQL](#beyond-traditional-sql)
- [Documentation](./doc/query-language.md)
- [AQL Compliance Testing](#aql-compliance-testing)
- [Architecture](#architecture)
- [Current Focus](#current-focus)
- [Vision](#vision)

---

## Why AQL Exists

Engineering teams spend enormous amounts of time switching contexts:

```text
SQL for databases
DSLs for search engines
HTTP for APIs
CLI commands for infrastructure
Custom scripts for files
```

The result is fragmented tooling, duplicated logic, and increased operational complexity.

AQL was created to answer a simple question:

> What if every system could be queried through a common language?

Instead of learning dozens of query interfaces, engineers can focus on the data itself.

---

## Core Principles

### Universal Access

Query any supported source using the same language.

```sql
SELECT * FROM postgres.users;
SELECT * FROM mongodb.users;
SELECT * FROM api('https://service/users');
SELECT * FROM csv('users.csv');
```

### Source Independence

Applications should not need to care where data originates.

```sql
SELECT id, name
FROM customers;
```

Whether the source is PostgreSQL today or MongoDB tomorrow should not require rewriting business logic.

### Federated Queries

Join data across technologies.

```sql
SELECT
    u.id,
    u.name,
    o.total
FROM postgres.users u
JOIN mongodb.orders o
ON u.id = o.user_id;
```

### Extensible Architecture

New sources can be added through adapters and dialects without changing the language itself.

---

## Example Queries

### Query a Database

```sql
SELECT *
FROM postgres.users
WHERE active = true;
```

### Query a REST API

```sql
SELECT *
FROM api('https://service.example.com/users');
```

### Query a CSV File

```sql
SELECT *
FROM csv('users.csv')
WHERE country = 'US';
```

### Query Kafka

```sql
SELECT *
FROM kafka.orders
LIMIT 100;
```

### Join Across Systems

```sql
SELECT
    u.name,
    o.total
FROM postgres.users u
JOIN mongodb.orders o
ON u.id = o.user_id;
```

---

## Beyond Traditional SQL

AQL is not intended to replace SQL.

Instead, AQL extends SQL concepts into environments where SQL traditionally does not exist.

Examples include:

- APIs
- Message queues
- Configuration files
- Infrastructure resources
- Log streams
- Binary formats
- Test artifacts
- Cloud platforms

This allows engineers to treat operational data the same way they treat relational data.

---


## AQL Compliance Testing

AQL includes a compliance testing framework designed to validate language behavior across supported features, sources, and execution paths.

The compliance suite helps ensure that queries produce consistent and predictable results as AQL evolves.

Run the compliance suite:

```bash
aql-test --cases ./tests
```

The framework executes a collection of test cases covering areas such as:

* Source discovery (`SHOW`)
* Schema inspection (`DESCRIBE`)
* Query execution (`SELECT`)
* Filtering (`WHERE`)
* Collection matching (`IN`)
* File-based sources
* Standard input (`stdin`)
* Aegis-native sources

Compliance coverage is continuously expanded as new language features and data sources are introduced.

### Why Compliance Matters

As AQL grows to support additional databases, files, APIs, streams, and infrastructure sources, a standardized compliance suite helps verify that behavior remains consistent regardless of where data originates.

The goal is simple:

> A query should behave the same way across all supported AQL sources.

### Contributing

New language features and source adapters should include compliance tests whenever possible.

This ensures behavior remains stable and helps prevent regressions as AQL continues to evolve.

---

## Architecture

```text
             AQL Query

                  │
                  ▼

          Query Planner
                  │

      ┌───────────┼───────────┐
      │           │           │

 PostgreSQL   MongoDB      Kafka
      │           │           │

      └───────────┼───────────┘
                  │

           Unified Result
```

AQL separates query execution from source implementation, allowing a single query to operate across many technologies.

---

## Current Focus

AQL is being developed to support:

- Relational databases
- Document databases
- Graph databases
- Search engines
- APIs
- Files
- Message queues
- Cloud services
- Infrastructure platforms

Additional adapters are added through an extensible dialect system.

---

## Vision

The long-term vision of AQL is simple:

> Query anything.

Data should be accessible regardless of where it lives, how it is stored, or which vendor created it.

AQL aims to provide a consistent, extensible, and developer-friendly way to interact with modern systems at scale.