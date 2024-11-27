from databricks.sdk import WorkspaceClient


def test_main(ws, spark):  # use pytester fixtures
    """This end-to-end test run the deployed job and verifies the output
    Needs to run deployment before executing the test: databricks bundle deploy --target qa"""
    job_name_suffix = "marcin_project_job_qa"
    job_id = get_job_id(ws, job_name_suffix)

    ws.jobs.run_now_and_wait(job_id)

    taxis = spark.table("samples.nyctaxi.trips")
    assert taxis.count() > 5


def get_job_id(w: WorkspaceClient, job_name_suffix: str) -> int | None:
    job_id = None
    for job in w.jobs.list():
        if job.as_dict()['settings']['name'].endswith(job_name_suffix):
            job_id = job.job_id
            break
    return job_id
