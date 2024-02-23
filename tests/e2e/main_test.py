# this test should relay on already deployed jobs

import os

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.compute import Language


CLUSTER_ID = os.getenv('DATABRICKS_TEST_CLUSTER_ID')


# needs to run before: databricks bundle deploy --target dev
def test_main():
    w = WorkspaceClient()  # use DEFAULT profile
    jobs = w.jobs.list(name="marcin_project_job")
    job_id = next(job for job in jobs).job_id
    w.jobs.run_now_and_wait(job_id)

    ctx = w.command_execution.create(cluster_id=CLUSTER_ID, language=Language.SQL).result()
    command = "SELECT * FROM samples.nyctaxi.trips LIMIT 5;"
    results = w.command_execution.execute(cluster_id=CLUSTER_ID, command=command, context_id=ctx.id, language=Language.SQL).result()
    assert len(results.results.data) == 5
