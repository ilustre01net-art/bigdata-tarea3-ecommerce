cat << 'EOF' > spark_batch_ventas.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count, when

spark = SparkSession.builder \
    .appName("EcommerceBatchAnalysis") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print("--- 1. CARGA DEL DATASET DE VENTAS ---")
df = spark.read.option("header", "true").option("inferSchema", "true").csv("ventas_ecommerce_batch.csv")
print(f"Total de registros cargados: {df.count()}")
df.show(5)

print("--- 2. LIMPIEZA Y TRANSFORMACIÓN (EDA) ---")
cleaned_df = df.filter(col("amount") > 0.0)

processed_df = cleaned_df.withColumn(
    "tipo_venta",
    when(col("amount") > 1000.0, "Premium").when(col("amount") > 300.0, "Regular").otherwise("Baja")
)

print("Muestra de datos limpios y transformados:")
processed_df.show(5)

print("--- 3. ANÁLISIS ESTADÍSTICO POR CATEGORÍA DE PRODUCTO ---")
summary_df = processed_df.groupBy("product_category").agg(
    count("transaction_id").alias("total_transacciones"),
    sum("amount").alias("ingresos_totales"),
    avg("amount").alias("monto_promedio")
).orderBy(col("ingresos_totales").desc())

summary_df.show()

spark.stop()
EOF
