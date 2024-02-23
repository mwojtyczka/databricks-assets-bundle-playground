from databricks.connect import DatabricksSession
from pyspark.sql import SparkSession
from marcin_project import main

# Create a new Databricks Connect session. If this fails,
# check that you have configured Databricks Connect correctly.
# See https://docs.databricks.com/dev-tools/databricks-connect.html

# Take connection from .databrikcscfg file, DEFAULT profile)
# https://docs.databricks.com/dev-tools/databricks-connect-ref.html#requirements
spark = DatabricksSession.builder.getOrCreate()

#SparkSession.builder = DatabricksSession.builder.profile("profile_name")
#spark = SparkSession.builder.getOrCreate()

# spark = DatabricksSession.builder.remote(
#    host=f"https://adb-8870486534760962.2.azuredatabricks.net/?o=8870486534760962",
#    token="dapi03fec0a64fcc088adc1a27864050a598-2",
#    cluster_id="0222-221408-a9yml4v"
# ).getOrCreate()

def test_main():
    taxis = main.get_taxis(spark)
    assert taxis.count() > 5

