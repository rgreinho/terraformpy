from pathlib import Path

import nox

# Behavior's options.
nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["venv"]

# Configuration values.
nox_file = Path()
project_name = "terraformpy"


@nox.session()
def ci(session):
    """Run all the CI tasks."""
    session.install("-rrequirements-dev.txt")
    session.install("-e", ".")
    run_sphinx(session)
    run_black(session, True)
    run_all_linters(session)
    run_pytest_units(session)


@nox.session()
def dist(session):
    """Package the application."""
    session.install("-rrequirements-dev.txt")
    session.install("-e", ".")
    session.run("python", "setup.py", "bdist_wheel")


@nox.session()
def dist_upload(session):
    """Package the application."""
    session.install("-rrequirements-dev.txt")
    session.run("twine", "upload", "dist/*")


@nox.session()
def docs(session):
    """Ensure the documentation builds."""
    session.install("-rrequirements-dev.txt")
    session.install("-e", ".")
    run_sphinx(session)


@nox.session()
def format(session):
    """Format the codebase using YAPF."""
    session.install("black")
    run_black(session)


@nox.session()
def lint(session):
    """Run all the linters."""
    session.install("-rrequirements-dev.txt")
    session.install("-e", ".")
    run_all_linters(session)


@nox.session(name="lint-format")
def lint_format(session):
    """Check the formatting of the codebase using YAPF."""
    session.install("black")
    run_black(session, True)


@nox.session()
def pydocstyle(session):
    """Check the docstrings."""
    session.install("-rrequirements-dev.txt")
    session.install("-e", ".")
    run_pydocstyle(session)


@nox.session()
def pylint(session):
    """Run the pylint linter."""
    session.install("-rrequirements-dev.txt")
    session.install("-e", ".")
    run_pylint(session)


@nox.session(python=["3.7", "3.8"])
def test(session):
    """Run all the tests."""
    session.install("-rrequirements-dev.txt")
    session.install("-e", ".")
    run_pytest(session)


@nox.session(python=["3.7", "3.8"], name="test-units")
def test_units(session):
    """Run the unit tests."""
    session.install("-rrequirements-dev.txt")
    session.install("-e", ".")
    run_pytest_units(session)


@nox.session(python=["3.7", "3.8"], name="test-integrations")
def test_integrations(session):
    """Run the integration tests."""
    session.install("-rrequirements-dev.txt")
    session.install("-e", ".")
    run_pytest_integrations(session)


@nox.session()
def venv(session):
    """Setup the developper environment."""
    # Install dependencies.
    session.install("--upgrade", "pip", "setuptools")
    session.install("-r", "requirements-dev.txt")
    session.install("-e", ".")

    # Customize the venv.
    env_dir = Path(session.bin)
    activate = env_dir / "activate"
    with activate.open("a") as f:
        f.write(
            f"\n[ -f {activate.resolve()}/postactivate ] && . {activate.resolve()}/postactivate\n"
        )

    postactivate = env_dir / "postactivate"
    with postactivate.open("a") as f:
        f.write("export PYTHONBREAKPOINT=bpdb.set_trace\n")

    predeactivate = env_dir / "predeactivate"
    with predeactivate.open("a") as f:
        f.write("unset PYTHONBREAKPOINT\n")


def run_all_linters(session):
    run_flake8(session)
    run_pydocstyle(session)
    run_pylint(session)


def run_flake8(session):
    session.run("flake8", f"{project_name}")


def run_pydocstyle(session):
    session.run("pydocstyle", f"{project_name}")


def run_pylint(session):
    session.run("pylint", "--ignore=tests", f"{project_name}")


def run_pytest(session, *posargs):
    session.run(
        "pytest",
        "-x",
        "--junitxml=/tmp/pytest/junit-py37.xml",
        "--cov-report",
        "term-missing",
        "--cov-report",
        "html",
        f"--cov={project_name}",
        *posargs,
        f'{(nox_file / "tests").resolve()}',
    )


def run_pytest_units(session):
    run_pytest(session, "-m", "'not integrations'")


def run_pytest_integrations(session):
    run_pytest(
        session, "-m", "integrations", "--reruns", "3", "--reruns-delay", "5", "-r", "R"
    )


def run_sphinx(session):
    session.run("python", "setup.py", "build_sphinx")


def run_black(session, check=False):
    opts = ["."]
    if check:
        opts.insert(0, "--check")
    session.run("black", *opts)
