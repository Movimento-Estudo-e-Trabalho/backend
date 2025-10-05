### How the migrations' version works

Alembic manages database schema versioning through migration files that represent incremental changes. Each file has a unique identifier (`revision`) and a reference to the immediately preceding migration (`down_revision`), forming a dependency chain. When running `alembic upgrade`, Alembic traverses this chain and applies the migrations in the correct order until it reaches the `head` (last available version), updating the `alembic_version` table in the database to reflect the current version. This allows precise control of schema upgrades and downgrades, facilitating the tracking, replication, and rollback of changes across different environments.
The table' version will be specified by `alembic_version` table in the db.

To see the current structure, run `alembic history --verbose`.

### Creating a new migration version

- You can make the modifications in the table schemas and then run the command to generate a new migration file to automatically write upgrade and downgrade functions.
- To create a new file to host a new migration, run  
   `alembic revision --autogenerate -m "MESSAGE"`
  This command will generate a file `YYYY_MM_DD` with the following important lines:

```python
revision: str = "ffda02860ac1" # the ID of this version
down_revision = None # the ID of the last version

branch_labels: Union[str, Sequence[str], None] = None # The branch of this version (None for now - just 1 branch)
depends_on: Union[str, Sequence[str], None] = None # create dependences betwen branches

def upgrade() -> None: # The code of your up migration
"""your code here"""

def downgrade() -> None: # The code of your down migration
"""your code here"""

```

### Util commands

1. Display the current revision for a database: `alembic current`.
2. View migrations history: `alembic history --verbose`.
3. Revert all migrations: `alembic downgrade base`.
4. Revert migrations one by one: `alembic downgrade -1`.
5. Apply all migrations:`alembic upgrade head`.
6. Apply migrations one by one: `alembic upgrade +1`.
7. Start the alembic in your repository: `alembic init alembic`.

### Resources

- [Migrations in Python using Alembic](https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a).
