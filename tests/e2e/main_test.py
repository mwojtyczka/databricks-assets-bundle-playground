# this test run the already deployed job

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.compute import Language
from databricks.sdk.core import Config

# needs to run before: databricks bundle deploy --target dev
def test_main():
    w = WorkspaceClient()  # use DEFAULT profile
    config = Config()
    job_id = get_job_id(w)

    w.jobs.run_now_and_wait(job_id)

    ctx = w.command_execution.create(cluster_id=config.cluster_id, language=Language.SQL).result()
    command = "SELECT * FROM samples.nyctaxi.trips LIMIT 5;"
    results = w.command_execution.execute(cluster_id=config.cluster_id, command=command, context_id=ctx.id, language=Language.SQL).result()
    assert len(results.results.data) == 5


def get_job_id(w):
    job_id = None
    for job in w.jobs.list():
        if job.as_dict()['settings']['name'].endswith("marcin_project_job_qa"):
            job_id = job.job_id
            break
    return job_id
