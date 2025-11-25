from pyspark.ml.recommendation import ALS

def train_als(train_df):
    als = ALS(
        maxIter=5,
        rank=10,
        regParam=0.1,
        userCol="userId",
        itemCol="itemId",
        ratingCol="rating",
        coldStartStrategy="drop"
    )
    model = als.fit(train_df)
    return model
