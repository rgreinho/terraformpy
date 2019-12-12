from pathlib import Path

from invoke import task

# Configuration values.
VENV = "venv"
project_name = "terraformpy"


@task
def clean(c):
    """Remove unwanted files and artifacts in this project (!DESTRUCTIVE!)."""
    clean_repo(c)


@task
def clean_repo(c):
    """Remove unwanted files in project (!DESTRUCTIVE!)."""
    c.run("git clean -ffdx")
    c.run("git reset --hard")


@task
def nox(c, s=""):
    """Wrapper for the nox tasks (`inv nox list` for details)."""
    if not s:
        c.run("nox --list")
    else:
        c.run(f"nox -s {s}")


@task(default=True)
def setup(c):
    """Setup the developper environment."""
    c.run("nox --envdir .")
