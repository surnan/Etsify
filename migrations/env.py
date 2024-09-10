from __future__ import with_statement
import logging
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os

# Environment variables
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# Alembic Config object, which provides access to values within the .ini file in use
config = context.config

# Interpret the config file for Python logging
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

# Import the Flask app and set up the application context
from your_flask_app import create_app  # Replace 'your_flask_app' with your actual app module

# Create an instance of the app
app = create_app()

# Set up the application context
with app.app_context():
    # Set the SQLAlchemy URL from the current app's configuration
    config.set_main_option(
        'sqlalchemy.url',
        str(current_app.extensions['migrate'].db.engine.url).replace('%', '%%')
    )
    # Set the target metadata for migrations
    target_metadata = current_app.extensions['migrate'].db.metadata

    def run_migrations_offline():
        """Run migrations in 'offline' mode."""
        url = config.get_main_option("sqlalchemy.url")
        context.configure(
            url=url, target_metadata=target_metadata, literal_binds=True
        )

        with context.begin_transaction():
            context.run_migrations()

    def run_migrations_online():
        """Run migrations in 'online' mode."""

        def process_revision_directives(context, revision, directives):
            if getattr(config.cmd_opts, 'autogenerate', False):
                script = directives[0]
                if script.upgrade_ops.is_empty():
                    directives[:] = []
                    logger.info('No changes in schema detected.')

        connectable = engine_from_config(
            config.get_section(config.config_ini_section),
            prefix='sqlalchemy.',
            poolclass=pool.NullPool,
        )

        with connectable.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=target_metadata,
                process_revision_directives=process_revision_directives,
                **current_app.extensions['migrate'].configure_args
            )

            # Create a schema if in production
            if environment == "production":
                connection.execute(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA}")

            # Set the search path to the schema if in production
            with context.begin_transaction():
                if environment == "production":
                    context.execute(f"SET search_path TO {SCHEMA}")
                context.run_migrations()

    # Check if Alembic is running in offline mode
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        run_migrations_online()
