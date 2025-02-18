# Databricks Assets Bundle Example Project

The project was generated by using the default-python asset bundle template with additional improvements:
* added examples for unit, integration and end-to-end tests
* managing python dependencies using poetry.

## Getting started

1. Install the Databricks CLI from https://docs.databricks.com/dev-tools/cli/databricks-cli.html

2. Authenticate to your Databricks workspace:
    ```bash
    databricks configure
    ```

3. To deploy a development copy of this project, type:
    ```bash
    databricks bundle deploy --target dev
    ```
    (Note that "dev" is the default target, so the `--target` parameter
    is optional here.)
    
    Set optional variable: 
    ```bash
    databricks bundle deploy --target dev --var="cluster_policy_id=E05E27B13F0003A2"
    ```    

    This deploys everything that's defined for this project.
    For example, the default template would deploy a job called
    `[dev yourname] marcin_project_job` to your workspace.
    You can find that job by opening your workpace and clicking on **Workflows**.

4. Similarly, to deploy a production copy, type:
   ```bash
   $ databricks bundle deploy --target prod
   ```

5. To run a job or pipeline, use the "run" command:
   ```bash
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

### Setup IDE - get path to poetry virtual env

```bash
echo $(poetry env info --path)/bin
```

Activate poetry virtual environment:

```bash
source $(poetry env info --path)/bin/activate
```

### Building

```bash
poetry build
```

### Testing

* Unit testing:

```bash
pytest tests/unit --cov
```

* Integration testing:
```bash
pytest tests/integration --cov
```

* End to End testing:
```bash
pytest tests/e2e --cov
```

### Reinstalling poetry virtual env

```
poetry env list
poetry env remove marcin-project-4eO9IBzv-py3.10
poetry install
```
