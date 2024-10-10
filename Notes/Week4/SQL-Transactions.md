# **PostgreSQL Transactions + Schemas**

## **What is a Transaction?**

A **transaction** in PostgreSQL is a unit of work that contains a sequence of one or more SQL operations executed as a single whole. The main idea behind transactions is **ensuring data integrity**: all the changes made within a transaction are either **committed** (made permanent) or **rolled back** (undone) in the case of errors or failure.

## **Why Use Transactions?**

- **Consistency and Integrity**: Ensures that a set of operations, like transferring money between bank accounts, is executed completely or not at all.
- **Isolation**: Transactions allow multiple users to interact with the database concurrently without interference, maintaining correct and predictable results.
- **Error Handling**: If something goes wrong in the middle of a series of operations (e.g., an application crash), you can undo everything that was done before the failure, ensuring the database is never left in a corrupt state.

## **Transaction Control Commands**

PostgreSQL provides several commands to control the lifecycle of a transaction:

1. **BEGIN**: Starts a new transaction.

   ```sql
   BEGIN;
   ```

2. **COMMIT**: Ends the transaction and makes all changes made during the transaction permanent.

   ```sql
   COMMIT;
   ```

3. **ROLLBACK**: Undoes all the changes made in the current transaction, reverting the database to the state before the transaction started.

   ```sql
   ROLLBACK;
   ```

### **Savepoints**

A **savepoint** allows you to partially roll back a transaction. You can set multiple savepoints within a transaction, and if an error occurs, you can rollback only to the most recent savepoint instead of rolling back the entire transaction.

- **Creating a Savepoint**:  
   You can create a savepoint within a transaction to mark a specific point that you may want to roll back to.

   ```sql
   SAVEPOINT savepoint_name;
   ```

- **Rolling Back to a Savepoint**:  
   If an error occurs, instead of rolling back the entire transaction, you can roll back to a savepoint.

   ```sql
   ROLLBACK TO savepoint_name;
   ```

- **Releasing a Savepoint**:  
   Once you are sure that a portion of a transaction is complete and no rollback is needed for that savepoint, you can release it.

   ```sql
   RELEASE SAVEPOINT savepoint_name;
   ```

#### **Example of a Transaction with Savepoints**

```sql
BEGIN;

-- First set of operations
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
SAVEPOINT sp1;

-- Second set of operations (this might fail)
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

-- Something goes wrong here, rollback to sp1
ROLLBACK TO sp1;

-- Third set of operations
UPDATE accounts SET balance = balance + 50 WHERE account_id = 3;

COMMIT;
```

## **ACID Properties of Transactions**

Transactions in PostgreSQL adhere to the **ACID** properties, which guarantee reliable and consistent database behavior.

1. **Atomicity**:  
   All operations within a transaction are either fully completed or fully undone. If any part of the transaction fails, the entire transaction is rolled back.

2. **Consistency**:  
   Ensures that a transaction brings the database from one valid state to another. Data integrity is maintained, and any constraints on the data (such as foreign key constraints) are respected.

3. **Isolation**:  
   Transactions are executed in isolation from each other. This means that the intermediate state of a transaction is not visible to other transactions, ensuring that they don't affect each other.

4. **Durability**:  
   Once a transaction has been committed, the changes are permanent. Even in case of a system failure, the data will remain stored as it was after the commit.

---

## **Schema in PostgreSQL**

A **schema** in PostgreSQL is a logical collection of database objects, such as tables, views, indexes, and functions, within a database. Schemas help organize and group objects in a way that supports both better structure and permission management within a database.

- **How Schemas Relate to a Database**:  
  A **database** in PostgreSQL can have multiple **schemas**. While a database is the top-level container that stores all data, schemas help **organize** that data. For example, within a single database, you can have separate schemas for different departments like `sales`, `hr`, and `finance`, each containing its own tables and other objects.

- **Default Schema**:  
  Every PostgreSQL database has a default schema called `public`, where all database objects are placed if no schema is specified.

- **Creating a Schema**:  
  You can create custom schemas in PostgreSQL:

  ```sql
  CREATE SCHEMA hr;
  ```

- **Accessing Objects in Schemas**:  
  To reference an object in a schema, you can prefix the object with the schema name:

  ```sql
  SELECT * FROM hr.employees;
  ```

### **Schema vs. Database**

- **Database**: A full collection of all data, tables, schemas, and objects. It can hold multiple schemas and defines the entire storage of data.
- **Schema**: A logical grouping within the database that allows objects to be managed and referenced separately from other groups of objects.

In summary, a schema is like a folder that helps organize objects (tables, functions, etc.) within the broader scope of a database.
