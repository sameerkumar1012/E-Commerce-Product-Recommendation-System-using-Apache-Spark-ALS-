from pyspark.sql.functions import explode, col

def user_recommend(model, n=5):
    userRecs = model.recommendForAllUsers(n)
    user_recs_exploded = userRecs.select(
        col("userId"),
        explode(col("recommendations")).alias("rec")
    ).select(
        "userId",
        col("rec.itemId").alias("itemId"),
        col("rec.rating").alias("pred_rating")
    )
    return user_recs_exploded
