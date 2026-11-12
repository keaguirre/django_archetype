# 12/11/26
- Fixed products_api.Producto model (duplicated max_length, invalid max_digits) that prevented Django from starting.
- settings.py: DATABASE_URL (SSL, configurable with DATABASE_SSLMODE) or POSTGRES_* variables for the local container.
- docker-compose: unified variable names, named volume (works on Windows), db healthcheck, migrations on start.
- Dockerfile: valid base image tag, copies local code instead of cloning the repo.
- SendGrid is now optional: without SENDGRID_API_KEY the email is skipped.

# 14/12/24
- Rollback from use email instead of username for registration cause, the userCreationForm needs an username field wich takes the priority over the email field.
- changed to use the username as the email field and repeat the same value for the username field. to get satisfy the required fields for the userCreationForm for default user model.
