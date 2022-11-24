from invoke import task


@task
def test(c):
    c.run("env PYTHONPATH='.' pytest -s")
