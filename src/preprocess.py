from pyspark.sql.functions import col, when

def preprocess(df, limit_rows=200000):
    df = df.limit(limit_rows)
    ratings = df.withColumn(
        "rating",
        when(col("event") == "view", 1)
        .when(col("event") == "addtocart", 2)
        .when(col("event") == "transaction", 3)
    )
    ratings = ratings.select(
        col("visitorid").alias("userId"),
        col("itemid").alias("itemId"),
        col("rating")
    ).dropna()

    ratings = ratings.withColumn("userId", col("userId").cast("int")) \
                     .withColumn("itemId", col("itemId").cast("int")) \
                     .withColumn("rating", col("rating").cast("int"))

    return ratings
