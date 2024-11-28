from marcin_project import main

# You can use pytester or create the Databricks session manually as below.
# This will take auth details from the DEFAULT profile from .databrikcscfg file:
# https://docs.databricks.com/dev-tools/databricks-connect-ref.html#requirements
#spark = DatabricksSession.builder.getOrCreate()
# You can also provide auth credentials using .sdkConfig(config)

# Or build explicitly
# spark = DatabricksSession.builder.remote(
#    host=f"XXX",
#    token="xxx",
#    cluster_id="xxx"
# ).getOrCreate()

def test_main(spark):  # use pytester fixture
    taxis = main.get_taxis(spark)
    assert taxis.count() > 5
