from pyspark.sql import SparkSession
from marcin_project.functions import filter_taxis


def get_taxis():
  spark = SparkSession.builder.getOrCreate()
  return filter_taxis(spark.read.table("samples.nyctaxi.trips"))

def main():
  get_taxis().show(5)


if __name__ == '__main__':
  main()
