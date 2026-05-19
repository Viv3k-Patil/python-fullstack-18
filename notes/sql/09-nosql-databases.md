# Day 9: NoSQL — MongoDB Foundations

---

## Start Here: A Different Way to Think About Data

Everything you have learned so far — tables, rows, columns, joins, schemas — is the relational model. It has been the dominant way to store data for decades, and it is excellent at what it does.

But not all data fits neatly into tables.

Imagine you are building a social media platform. One user's profile might have:
- A name and email
- 3 phone numbers
- A bio
- A list of 200 followers
- A list of 15 posts, each with its own likes, comments, and tags
- Preferences: dark mode on, notifications off, language English

Try to put this in a relational schema. You would need at least 6 or 7 tables, complex joins for every read, and the schema would need to change every time a new type of preference is added.

Now imagine a product catalogue for an e-commerce site. A laptop has: processor, RAM, storage, display size, GPU, battery life. A t-shirt has: size, colour, fabric, gender. A book has: author, ISBN, publisher, page count. None of these products share the same set of attributes — yet in a relational database, they would all have to live in the same table structure.

These are the kinds of problems that motivated **NoSQL** databases — databases that store data differently, without the rigid table-and-row structure.

---

## What is NoSQL?

**NoSQL** stands for "Not Only SQL." It is a category of databases that use data models other than the relational model.

NoSQL does not mean "no SQL language." It means the underlying data model is different. Some NoSQL databases even have their own query languages that look similar to SQL.

### Types of NoSQL Databases

| Type | Stores data as | Example Databases | Best for |
|---|---|---|---|
| **Document** | JSON-like documents | MongoDB, CouchDB, Firestore | User profiles, product catalogues, content |
| **Key-Value** | Simple key → value pairs | Redis, DynamoDB | Sessions, caching, leaderboards |
| **Column-Family** | Rows with flexible columns | Cassandra, HBase | Time-series data, analytics at scale |
| **Graph** | Nodes and edges | Neo4j, Amazon Neptune | Social networks, recommendation engines, fraud detection |

Today we focus on **document databases** — specifically **MongoDB** — because they are the most widely used NoSQL type and the closest conceptually to what you already know.

---

## MongoDB — The Core Idea

MongoDB stores data as **documents**. A document is a JSON-like object — a collection of key-value pairs that can be nested and can contain arrays.

```json
{
  "_id": "64a1f2b3c8e7d12345678901",
  "name": "Riya Sharma",
  "email": "riya@email.com",
  "age": 21,
  "city": "Pune",
  "is_active": true,
  "skills": ["Python", "SQL", "MongoDB"],
  "address": {
    "street": "12 MG Road",
    "pincode": "411001"
  }
}
```

This one document holds what would require multiple tables and joins in a relational database. Everything about Riya — including her skills list and her nested address — lives together in one place.

### Key terminology

| MongoDB term | SQL equivalent |
|---|---|
| Database | Database |
| Collection | Table |
| Document | Row |
| Field | Column |
| `_id` | Primary Key |
| Embedded document | Related row (via join) |
| Array field | Related rows in another table |

A **collection** is a group of documents. Like a table, but without a fixed schema — different documents in the same collection can have different fields.

A **database** contains collections. You can have multiple databases in one MongoDB server.

---

## BSON — What MongoDB Actually Stores

MongoDB documents look like JSON but are stored internally as **BSON** (Binary JSON). BSON supports a few extra data types that plain JSON does not:

| BSON Type | Example |
|---|---|
| `ObjectId` | `ObjectId("64a1f2b3c8e7d12345678901")` — auto-generated unique ID |
| `Date` | `ISODate("2024-01-15T10:30:00Z")` |
| `Int32` / `Int64` | `21`, `9000000000` |
| `Decimal128` | `Decimal128("45000.50")` — for precise money values |
| `Boolean` | `true` / `false` |
| `Null` | `null` |
| `Array` | `["Python", "SQL"]` |
| `Object` | `{ "street": "12 MG Road" }` |

In practice, when you write MongoDB queries you write them as JSON. MongoDB translates internally.

---

## The `_id` Field

Every document in MongoDB must have an `_id` field. It is the unique identifier — equivalent to a primary key.

If you do not provide `_id` when inserting, MongoDB automatically generates an `ObjectId` — a 12-byte value that encodes a timestamp, machine identifier, and a random component. It is guaranteed to be unique.

```json
{ "_id": ObjectId("64a1f2b3c8e7d12345678901") }
```

You can also provide your own `_id`:

```json
{ "_id": "riya-sharma-2024" }
{ "_id": 1001 }
```

As long as it is unique within the collection, any value works.

---

## Setting Up — MongoDB Shell Basics

MongoDB has a shell (`mongosh`) where you type commands interactively, similar to how you type SQL in a MySQL client.

### Select or create a database

```javascript
use school
```

If the database `school` does not exist, MongoDB creates it the moment you first insert data. Just using `use school` does not create it yet.

### See which database you are in

```javascript
db
```

### See all databases

```javascript
show dbs
```

### See all collections in the current database

```javascript
show collections
```

### Create a collection explicitly

```javascript
db.createCollection("students")
```

Or just start inserting — MongoDB creates the collection automatically on first insert.

---

## CRUD — Create, Read, Update, Delete

MongoDB's four fundamental operations. Every application you build will use these.

---

### CREATE — Inserting Documents

#### Insert one document

```javascript
db.students.insertOne({
  name: "Riya Sharma",
  email: "riya@email.com",
  age: 21,
  city: "Pune",
  marks: 88,
  skills: ["Python", "SQL"]
})
```

MongoDB returns:

```json
{
  "acknowledged": true,
  "insertedId": ObjectId("64a1f2b3c8e7d12345678901")
}
```

The `_id` was auto-generated. The document is now in the `students` collection.

#### Insert many documents

```javascript
db.students.insertMany([
  {
    name: "Arjun Mehta",
    email: "arjun@email.com",
    age: 23,
    city: "Mumbai",
    marks: 74,
    skills: ["Java", "Spring"]
  },
  {
    name: "Sara Khan",
    email: "sara@email.com",
    age: 22,
    city: "Delhi",
    marks: 91,
    skills: ["React", "Node.js", "MongoDB"]
  },
  {
    name: "Karan Joshi",
    email: "karan@email.com",
    age: 20,
    city: "Pune",
    marks: 65
    // no skills field — that is fine in MongoDB
  },
  {
    name: "Meera Nair",
    email: "meera@email.com",
    age: 24,
    city: "Bangalore",
    marks: 79,
    skills: ["Python", "Data Science", "SQL"],
    profile: {
      github: "github.com/meeranair",
      linkedin: "linkedin.com/in/meera"
    }
  }
])
```

Notice: Karan has no `skills` field. Meera has a nested `profile` object. This is perfectly valid. MongoDB does not enforce a schema — each document can have its own shape.

---

### READ — Querying Documents

#### Find all documents

```javascript
db.students.find()
```

Returns every document in the collection. Equivalent to `SELECT * FROM students`.

#### Find with a filter

```javascript
db.students.find({ city: "Pune" })
```

Returns only students from Pune. The filter `{ city: "Pune" }` is called a **query document**. Equivalent to `WHERE city = 'Pune'`.

#### Find one document

```javascript
db.students.findOne({ city: "Pune" })
```

Returns only the first matching document. Useful when you know there is only one match, or when you just need a sample.

#### Find by `_id`

```javascript
db.students.findOne({ _id: ObjectId("64a1f2b3c8e7d12345678901") })
```

#### Projection — selecting specific fields

The second argument to `find()` controls which fields to return. `1` means include, `0` means exclude.

```javascript
// Show only name and city (include _id by default)
db.students.find({}, { name: 1, city: 1 })

// Show name and city, exclude _id
db.students.find({}, { name: 1, city: 1, _id: 0 })

// Exclude marks only, show everything else
db.students.find({}, { marks: 0 })
```

You cannot mix include and exclude in the same projection (except for `_id`). Either list what you want to include, or list what you want to exclude.

#### Comparison operators

MongoDB query operators start with `$`. They go inside the filter document.

| Operator | Meaning | SQL equivalent |
|---|---|---|
| `$eq` | Equal | `=` |
| `$ne` | Not equal | `!=` |
| `$gt` | Greater than | `>` |
| `$gte` | Greater than or equal | `>=` |
| `$lt` | Less than | `<` |
| `$lte` | Less than or equal | `<=` |
| `$in` | Matches any value in array | `IN (...)` |
| `$nin` | Matches none in array | `NOT IN (...)` |

```javascript
// Students with marks greater than 80
db.students.find({ marks: { $gt: 80 } })

// Students aged between 20 and 22 (inclusive)
db.students.find({ age: { $gte: 20, $lte: 22 } })

// Students from Pune or Delhi
db.students.find({ city: { $in: ["Pune", "Delhi"] } })

// Students not from Mumbai
db.students.find({ city: { $ne: "Mumbai" } })
```

#### Logical operators

```javascript
// AND: students from Pune AND marks > 70
db.students.find({
  $and: [
    { city: "Pune" },
    { marks: { $gt: 70 } }
  ]
})

// Shorthand AND: same result (when conditions are on different fields, just list them)
db.students.find({ city: "Pune", marks: { $gt: 70 } })

// OR: students from Pune OR Bangalore
db.students.find({
  $or: [
    { city: "Pune" },
    { city: "Bangalore" }
  ]
})

// NOT: students who are NOT from Mumbai
db.students.find({ city: { $not: { $eq: "Mumbai" } } })

// NOR: students who are neither from Mumbai nor Delhi
db.students.find({
  $nor: [
    { city: "Mumbai" },
    { city: "Delhi" }
  ]
})
```

#### Querying nested fields

Use **dot notation** to query inside embedded documents.

```javascript
// Find students whose GitHub profile contains 'meera'
db.students.find({ "profile.github": "github.com/meeranair" })
```

The field path `"profile.github"` must be in quotes when using dot notation.

#### Querying array fields

```javascript
// Find students who have Python as a skill
db.students.find({ skills: "Python" })
```

MongoDB automatically checks if `"Python"` is an element of the `skills` array. You do not need a special operator.

```javascript
// Find students who have BOTH Python AND SQL
db.students.find({ skills: { $all: ["Python", "SQL"] } })

// Find students whose skills array has exactly 3 elements
db.students.find({ skills: { $size: 3 } })
```

#### Checking if a field exists

```javascript
// Find students who have a skills field
db.students.find({ skills: { $exists: true } })

// Find students who do NOT have a skills field
db.students.find({ skills: { $exists: false } })
```

#### Sorting results

```javascript
// Sort by marks descending (highest first)
db.students.find().sort({ marks: -1 })

// Sort by city ascending, then marks descending
db.students.find().sort({ city: 1, marks: -1 })
```

`1` = ascending. `-1` = descending.

#### Limiting and skipping results

```javascript
// Get only the top 3 students by marks
db.students.find().sort({ marks: -1 }).limit(3)

// Skip first 2, then get next 3 (page 2)
db.students.find().sort({ marks: -1 }).skip(2).limit(3)
```

#### Counting documents

```javascript
// Count all students
db.students.countDocuments()

// Count students from Pune
db.students.countDocuments({ city: "Pune" })
```

---

### UPDATE — Modifying Documents

MongoDB update operations use **update operators** — `$set`, `$unset`, `$inc`, `$push`, and more. This is important: you do not rewrite the whole document, you describe what to change.

#### Update one document

```javascript
// Update Riya's marks to 92
db.students.updateOne(
  { name: "Riya Sharma" },       // filter: which document
  { $set: { marks: 92 } }        // update: what to change
)
```

`$set` updates specific fields. Fields not mentioned are left exactly as they are.

#### Update many documents

```javascript
// Set all Pune students as active
db.students.updateMany(
  { city: "Pune" },
  { $set: { is_active: true } }
)
```

#### Common update operators

| Operator | What it does | Example |
|---|---|---|
| `$set` | Set a field to a value | `{ $set: { marks: 92 } }` |
| `$unset` | Remove a field | `{ $unset: { phone: "" } }` |
| `$inc` | Increment a numeric field | `{ $inc: { marks: 5 } }` |
| `$rename` | Rename a field | `{ $rename: { "city": "location" } }` |
| `$push` | Add an element to an array | `{ $push: { skills: "Docker" } }` |
| `$pull` | Remove an element from an array | `{ $pull: { skills: "Java" } }` |
| `$addToSet` | Add to array only if not already present | `{ $addToSet: { skills: "Python" } }` |
| `$pop` | Remove first or last element of array | `{ $pop: { skills: 1 } }` |

```javascript
// Give all students 5 bonus marks
db.students.updateMany(
  {},                              // empty filter = all documents
  { $inc: { marks: 5 } }
)

// Add "MongoDB" to Riya's skills
db.students.updateOne(
  { name: "Riya Sharma" },
  { $push: { skills: "MongoDB" } }
)

// Add "SQL" only if it's not already in the array
db.students.updateOne(
  { name: "Arjun Mehta" },
  { $addToSet: { skills: "SQL" } }
)

// Remove a field entirely
db.students.updateOne(
  { name: "Karan Joshi" },
  { $unset: { phone: "" } }
)
```

#### replaceOne — replacing the entire document

Unlike `updateOne` (which changes specific fields), `replaceOne` replaces the entire document with a new one. Only `_id` is preserved.

```javascript
db.students.replaceOne(
  { name: "Karan Joshi" },
  {
    name: "Karan Joshi",
    email: "karan.new@email.com",
    age: 21,
    city: "Mumbai",
    marks: 70
  }
)
```

Use `replaceOne` carefully — any fields not included in the new document will be gone.

#### upsert — update or insert

`upsert: true` means: if the filter finds a document, update it. If no document matches, insert a new one.

```javascript
db.students.updateOne(
  { email: "new.student@email.com" },
  { $set: { name: "New Student", city: "Pune", marks: 80 } },
  { upsert: true }
)
```

If no student has that email, a new document is created.

---

### DELETE — Removing Documents

#### Delete one document

```javascript
db.students.deleteOne({ name: "Karan Joshi" })
```

Deletes the first document matching the filter.

#### Delete many documents

```javascript
// Delete all students from Delhi
db.students.deleteMany({ city: "Delhi" })

// Delete all documents in the collection (but keep the collection)
db.students.deleteMany({})
```

#### Drop the entire collection

```javascript
db.students.drop()
```

This removes the collection and all its documents permanently. Equivalent to `DROP TABLE` in SQL.

#### Drop the entire database

```javascript
db.dropDatabase()
```

---

## Schema Patterns in MongoDB

MongoDB does not enforce a schema by default. But this does not mean you design without thinking. Document structure decisions have major performance and usability consequences. There are two primary patterns for modelling relationships.

### Pattern 1: Embedding (Denormalisation)

Store related data inside the same document.

```javascript
// A blog post with its comments embedded
{
  "_id": ObjectId("..."),
  "title": "Getting Started with MongoDB",
  "author": "Priya Nair",
  "published_at": ISODate("2024-01-15"),
  "tags": ["mongodb", "nosql", "databases"],
  "comments": [
    {
      "user": "Riya",
      "text": "Great article!",
      "posted_at": ISODate("2024-01-16")
    },
    {
      "user": "Arjun",
      "text": "Very helpful, thanks.",
      "posted_at": ISODate("2024-01-17")
    }
  ]
}
```

**When to embed:**
- The related data is always queried together with the parent (you always want comments when you fetch a post)
- The related data is not shared across documents (a comment belongs to one post only)
- The related data has a bounded size (a post will not have 50,000 comments)
- Read performance is the priority

**Advantages:** One read fetches everything. No joins needed.

**Disadvantages:** Document can grow very large. If the embedded data is also needed elsewhere independently, you will duplicate it.

### Pattern 2: Referencing (Normalisation)

Store a reference (the `_id`) to a document in another collection — the same concept as a foreign key.

```javascript
// orders collection
{
  "_id": ObjectId("order001"),
  "customer_id": ObjectId("cust001"),   // reference to customers collection
  "product_ids": [
    ObjectId("prod001"),
    ObjectId("prod002")
  ],
  "total": 580.00,
  "created_at": ISODate("2024-01-15")
}

// customers collection
{
  "_id": ObjectId("cust001"),
  "name": "Riya Sharma",
  "email": "riya@email.com"
}
```

To fetch the full order with customer details, you need two queries (or use MongoDB's `$lookup` aggregation — covered below).

**When to reference:**
- The related data is large and frequently updated (updating a customer's address should not require updating every order)
- The related data is shared across multiple documents (one product appears in many orders)
- The related data is queried independently (you query customers separately from orders)
- Write performance is the priority

### Choosing Between Embedding and Referencing

Ask these questions:

| Question | Embed | Reference |
|---|---|---|
| Is the data always accessed together? | Yes → Embed | No → Reference |
| Does the related data belong to only one parent? | Yes → Embed | No → Reference |
| Is the related data unbounded in size? | No → Embed | Yes → Reference |
| Is the related data updated frequently and independently? | No → Embed | Yes → Reference |

In practice, MongoDB schemas are often a **hybrid** — some things embedded, some referenced. A user profile might embed the address (always accessed together, belongs to one user) but reference their orders (large, independent).

---

## The Aggregation Pipeline

For complex queries — grouping, joining collections, computing totals — MongoDB uses an **aggregation pipeline**. You pass documents through a series of stages, each stage transforming the data.

Think of it as an assembly line: data enters, gets filtered, gets grouped, gets sorted, and comes out the other end as the result you wanted.

```javascript
db.collection.aggregate([
  { stage 1 },
  { stage 2 },
  { stage 3 }
])
```

### Common pipeline stages

| Stage | What it does | SQL equivalent |
|---|---|---|
| `$match` | Filter documents | `WHERE` |
| `$group` | Group and aggregate | `GROUP BY` + `COUNT/SUM/AVG` |
| `$sort` | Sort documents | `ORDER BY` |
| `$limit` | Limit number of documents | `LIMIT` |
| `$skip` | Skip documents | `OFFSET` |
| `$project` | Include/exclude/reshape fields | `SELECT col AS alias` |
| `$lookup` | Join with another collection | `JOIN` |
| `$unwind` | Flatten an array into separate documents | (no direct equivalent) |
| `$count` | Count documents passing through | `COUNT(*)` |

### Example 1: Count students per city

```javascript
db.students.aggregate([
  {
    $group: {
      _id: "$city",              // group by city
      count: { $sum: 1 },        // count documents in each group
      avg_marks: { $avg: "$marks" }
    }
  },
  {
    $sort: { count: -1 }         // sort by count descending
  }
])
```

Result:

```json
[
  { "_id": "Pune",      "count": 2, "avg_marks": 78.5 },
  { "_id": "Mumbai",    "count": 1, "avg_marks": 74 },
  { "_id": "Delhi",     "count": 1, "avg_marks": 91 },
  { "_id": "Bangalore", "count": 1, "avg_marks": 79 }
]
```

### Example 2: Filter then group

```javascript
// Average marks per city, only for students scoring above 70
db.students.aggregate([
  { $match: { marks: { $gt: 70 } } },        // step 1: filter
  { $group: {
      _id: "$city",
      avg_marks: { $avg: "$marks" },
      student_count: { $sum: 1 }
  }},
  { $sort: { avg_marks: -1 } }               // step 3: sort
])
```

### Example 3: $lookup — joining collections

`$lookup` is MongoDB's equivalent of a SQL JOIN. It joins documents from another collection.

```javascript
// orders collection joined with customers collection
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",           // the collection to join
      localField: "customer_id",   // field in orders
      foreignField: "_id",         // field in customers
      as: "customer_info"          // name for the joined data
    }
  },
  {
    $project: {
      total: 1,
      created_at: 1,
      "customer_info.name": 1,
      "customer_info.email": 1
    }
  }
])
```

Result:

```json
{
  "_id": ObjectId("order001"),
  "total": 580.00,
  "created_at": ISODate("2024-01-15"),
  "customer_info": [
    {
      "name": "Riya Sharma",
      "email": "riya@email.com"
    }
  ]
}
```

`customer_info` is an array (even when there is only one match). Use `$unwind` to flatten it.

### Example 4: $unwind — flattening arrays

```javascript
// Flatten the skills array so each skill becomes its own document
db.students.aggregate([
  { $unwind: "$skills" },
  { $group: {
      _id: "$skills",
      student_count: { $sum: 1 }
  }},
  { $sort: { student_count: -1 } }
])
```

This tells you how many students have each skill. `$unwind` turns one document with a 3-element array into 3 separate documents, one per skill element.

### Aggregation operators for $group

| Operator | What it computes |
|---|---|
| `$sum: 1` | Count of documents |
| `$sum: "$field"` | Total of a field |
| `$avg: "$field"` | Average of a field |
| `$min: "$field"` | Minimum value |
| `$max: "$field"` | Maximum value |
| `$push: "$field"` | Collect all values into an array |
| `$addToSet: "$field"` | Collect unique values into an array |
| `$first: "$field"` | First value in the group |
| `$last: "$field"` | Last value in the group |

---

## Indexes in MongoDB

Just like in SQL, indexes make queries faster by letting MongoDB jump directly to matching documents instead of scanning every document in a collection.

```javascript
// Create a single field index
db.students.createIndex({ email: 1 })        // ascending
db.students.createIndex({ marks: -1 })       // descending

// Create a unique index
db.students.createIndex({ email: 1 }, { unique: true })

// Create a compound index
db.students.createIndex({ city: 1, marks: -1 })

// See all indexes on a collection
db.students.getIndexes()

// Drop an index
db.students.dropIndex({ email: 1 })
```

The `_id` field is always indexed automatically.

---

## When to Use NoSQL vs SQL

This is one of the most important judgment calls in engineering. Neither is universally better. The right choice depends on your data and your use case.

### Use a Relational Database (SQL) when:

- Your data is structured and consistent — all records of the same type have the same fields
- You have complex relationships between many entities
- Data integrity is critical — banking, healthcare, legal records
- You need complex multi-table queries with joins and aggregations
- You need ACID transactions — operations that must fully succeed or fully fail
- Your schema is stable and not changing frequently

### Use a Document Database (MongoDB) when:

- Your data has a variable or evolving structure — different records have different fields
- You need to store hierarchical or nested data naturally
- You are building with fast-changing requirements and need schema flexibility
- Read performance is critical and data is naturally grouped together
- You are building at massive scale across distributed servers (horizontal scaling)
- Your data is document-like: user profiles, product catalogues, content, event logs

### The grey area

Many modern applications use **both**. User authentication and billing might be in PostgreSQL (strict integrity, ACID). The product catalogue and user activity feed might be in MongoDB (flexible, high read volume). This is called **polyglot persistence** — using different databases for different parts of the same system.

---

## SQL vs MongoDB — Side by Side

| Concept | SQL | MongoDB |
|---|---|---|
| Store data | `INSERT INTO table VALUES (...)` | `db.collection.insertOne({...})` |
| Read all | `SELECT * FROM table` | `db.collection.find()` |
| Filter | `WHERE city = 'Pune'` | `{ city: "Pune" }` |
| Update | `UPDATE table SET col = val WHERE ...` | `db.collection.updateOne({filter}, {$set: {field: val}})` |
| Delete | `DELETE FROM table WHERE ...` | `db.collection.deleteOne({filter})` |
| Count | `SELECT COUNT(*) FROM table` | `db.collection.countDocuments()` |
| Group by | `GROUP BY col` | `$group: { _id: "$col" }` |
| Join | `JOIN table ON ...` | `$lookup` in aggregation pipeline |
| Sort | `ORDER BY col DESC` | `.sort({ col: -1 })` |
| Limit | `LIMIT 10` | `.limit(10)` |

---

## Quick Reference

### CRUD

```javascript
// Insert
db.col.insertOne({...})
db.col.insertMany([{...}, {...}])

// Read
db.col.find()
db.col.find({ filter })
db.col.find({ filter }, { projection })
db.col.findOne({ filter })
db.col.countDocuments({ filter })

// Update
db.col.updateOne({ filter }, { $set: { field: val } })
db.col.updateMany({ filter }, { $set: { field: val } })
db.col.replaceOne({ filter }, { new_document })

// Delete
db.col.deleteOne({ filter })
db.col.deleteMany({ filter })
db.col.drop()
```

### Query Operators

```javascript
$eq, $ne, $gt, $gte, $lt, $lte
$in: [val1, val2]
$nin: [val1, val2]
$and: [{...}, {...}]
$or: [{...}, {...}]
$exists: true/false
$all: [val1, val2]       // array contains all
$size: n                 // array has exactly n elements
```

### Update Operators

```javascript
$set, $unset, $inc, $rename
$push, $pull, $addToSet, $pop
```

---

## Exercises

Set up a `school` database in MongoDB. Use `use school` and then create the collections by inserting data.

**Setup — insert this data before starting:**

```javascript
db.students.insertMany([
  { name: "Ananya Sharma", age: 21, city: "Pune",      marks: 88, department: "Engineering", skills: ["Python", "SQL", "Git"],          is_active: true  },
  { name: "Rohan Mehta",   age: 23, city: "Mumbai",    marks: 74, department: "Marketing",   skills: ["Excel", "Photoshop"],             is_active: true  },
  { name: "Priya Nair",    age: 22, city: "Bangalore", marks: 91, department: "Engineering", skills: ["Java", "Spring", "SQL"],          is_active: true  },
  { name: "Kiran Joshi",   age: 20, city: "Pune",      marks: 55, department: "HR",          skills: [],                                 is_active: false },
  { name: "Siddharth Rao", age: 25, city: "Mumbai",    marks: 82, department: "Engineering", skills: ["Python", "Django", "MongoDB"],    is_active: true  },
  { name: "Neha Kulkarni", age: 22, city: "Pune",      marks: 67, department: "Marketing",   skills: ["SEO", "Content Writing"],         is_active: true  },
  { name: "Aditya Verma",  age: 21, city: "Delhi",     marks: 79, department: "Finance",     skills: ["Excel", "Tally", "SQL"],          is_active: true  },
  { name: "Swati Patil",   age: 24, city: "Pune",      marks: 93, department: "Engineering", skills: ["C++", "Python", "ML"],            is_active: false },
  { name: "Manish Gupta",  age: 23, city: "Mumbai",    marks: 61, department: "Finance",     skills: ["Python", "Power BI"],             is_active: true  },
  { name: "Divya Reddy",   age: 22, city: "Hyderabad", marks: 85, department: "Engineering", skills: ["React", "Node.js", "MongoDB"],    is_active: true  }
])
```

**1.** Find all students in the collection.

**2.** Find all students from Pune.

**3.** Find all active students (`is_active: true`).

**4.** Find all students with marks greater than 80.

**5.** Find all students from Pune with marks greater than 70.

**6.** Find all students from either Pune or Bangalore.

**7.** Find all students who have `"Python"` as a skill.

**8.** Find all students who have both `"Python"` and `"SQL"` as skills.

**9.** Find all students who do NOT have a `skills` field, or whose skills array is empty. (Hint: try `$size: 0` and `$exists`.)

**10.** Find all students whose marks are between 70 and 90 (inclusive).

**11.** Show only the `name` and `marks` of all students, sorted by marks descending. Exclude `_id`.

**12.** Get the top 3 students by marks.

**13.** Get students ranked 4th to 6th by marks.

**14.** Count how many students are in the `Engineering` department.

**15.** Count how many distinct cities students are from. (Hint: use `distinct`.)

**16.** Update Kiran Joshi's marks to 68.

**17.** Add `"MongoDB"` to Ananya Sharma's skills. Make sure it is not added again if she already has it.

**18.** Give all inactive students 10 bonus marks using `$inc`.

**19.** Remove the `is_active` field from all students who are active.

**20.** Delete all students from Delhi.

**21.** Using the aggregation pipeline, count how many students are in each department.

**22.** Using the aggregation pipeline, find the average marks per city. Sort by average marks descending.

**23.** Using the aggregation pipeline, find the total number of skills across all students. (Hint: `$unwind` the skills array, then `$count`.)

**24.** Using `$unwind` and `$group`, find how many students have each individual skill (e.g. Python: 4, SQL: 3, ...).

**25.** A product catalogue for an e-commerce site needs to store laptops, t-shirts, and books — each with completely different attributes. Design two MongoDB documents for two different product types and explain why MongoDB is a better choice than a relational database for this use case.

**26.** Explain in your own words the difference between **embedding** and **referencing** in MongoDB. Give a real-world example of when you would choose each, and why.

**27.** You have been asked to design the database for a blogging platform where users write posts and other users can comment on them. Posts can have tags. Design the MongoDB schema. For each collection, write a sample document. Justify every embedding and referencing decision.
