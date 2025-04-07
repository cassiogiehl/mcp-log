from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Criação de uma Spark session
spark = SparkSession.builder.appName("ErrorAnalysisExample").getOrCreate()

# Exemplo de DataFrame com duas colunas
data = [("Alice", 34), ("Bob", 45), ("Charlie", 29)]
columns = ["name", "age"]

# Criação do DataFrame
df = spark.createDataFrame(data, columns)

df.select(col("salary")).show()

# Fechamento da Spark session
spark.stop()