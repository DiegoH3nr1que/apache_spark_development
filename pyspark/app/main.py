from pyspark.sql import SparkSession

# Criar uma sessão do Spark
spark = (
    SparkSession.builder
    .master("spark://spark-master:7077")
    .appName("TestePyspark")
    .getOrCreate()
)

# Criar um RDD de números de 1 a 100
rdd = spark.sparkContext.parallelize(range(1, 101))

# Coletar os valores do RDD
valores = rdd.collect()

# Mostrar cada valor
print("contagem de 1 a 100:")

for valor in valores:
    print(valor)

# Parar a sessão do Spark
spark.stop()