# marcin_project

The 'marcin_project' project was generated by using the default-python template.

## Getting started

1. Install the Databricks CLI from https://docs.databricks.com/dev-tools/cli/databricks-cli.html

2. Authenticate to your Databricks workspace:
    ```
    $ databricks configure
    ```

3. To deploy a development copy of this project, type:
    ```
    $ databricks bundle deploy --target dev
    ```
    (Note that "dev" is the default target, so the `--target` parameter
    is optional here.)

    This deploys everything that's defined for this project.
    For example, the default template would deploy a job called
    `[dev yourname] marcin_project_job` to your workspace.
    You can find that job by opening your workpace and clicking on **Workflows**.

4. Similarly, to deploy a production copy, type:
   ```
   $ databricks bundle deploy --target prod
   ```

5. To run a job or pipeline, use the "run" command:
   ```
   $ databricks bundle run
   ```

6. Optionally, install developer tools such as the Databricks extension for Visual Studio Code from
   https://docs.databricks.com/dev-tools/vscode-ext.html. Or read the "getting started" documentation for
   **Databricks Connect** for instructions on running the included Python code from a different IDE.

7. For documentation on the Databricks asset bundles format used
   for this project, and for CI/CD configuration, see
   https://docs.databricks.com/dev-tools/bundles/index.html.

8. Update the project to use Poetry:
   https://learn.microsoft.com/en-us/azure/databricks/dev-tools/bundles/python-wheel#step-4-update-the-projects-bundle-to-use-poetry

## Local Development

### Installing project requirements

```bash
poetry install
```

### Updating project requirements

```bash
poetry update
```

### Setup IDE - get virtual env path

```bash
echo $(poetry env info --path)/bin
```

You can also activate environment:

```bash
source $(poetry env info --path)/bin/activate
```

### Building

```sh
poetry build
```

### Testing

For local unit testing, please use `pytest`:

```
source $(poetry env info --path)/bin/activate
pytest tests/unit --cov
```

For integration testing, please use `pytest`:
```
source $(poetry env info --path)/bin/activate
pytest tests/integration --cov
```

### Reinstalling virtual env

Install env for unit testing and e2e
```
poetry env list
poetry env remove marcin-project-4eO9IBzv-py3.10
poetry install --only test
```

Install env for integration testing
```
poetry env list
poetry env remove marcin-project-4eO9IBzv-py3.10
poetry install --only int_test
```