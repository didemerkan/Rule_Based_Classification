#GOREV 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("persona.csv")
df

df.head()

# persona.csv dosyasını okutalım ve veri seti ile ilgili genel bilgileri gösterelim.
df.info()

# Kaç unique SOURCE vardır, Frekansları nedir, bunları bulalım:
# android ve ios olmaz üzere 2 tane.
df["SOURCE"].unique()

# Kaç unique PRICE olduğunu bulalım:
# 6 Tane
df["PRICE"].nunique()

# Hangi PRICE'dan kaçar tane satış gerçekleşmiş olduguna bakalım:
# (1305, 1260, 1031, 992, 212, 200)
df["PRICE"].value_counts()

# Hangi ülkeden kaçar tane satış olduguna bakalım:
df["PRICE"].groupby(df["COUNTRY"]).value_counts()

# Ülkelere göre satışlardan toplam ne kadar kazanılmış olacagına bakalım:
df["PRICE"].groupby(df["COUNTRY"]).agg("sum")

#  SOURCE türlerine göre göre satış sayıları:
df["PRICE"].groupby(df["SOURCE"]).value_counts()

#  Ülkelere göre PRICE ortalamaları:
df["PRICE"].groupby(df["COUNTRY"]).agg("mean")

# SOURCE'lara göre PRICE ortalamaları:
df["PRICE"].groupby(df["SOURCE"]).agg("mean")

#  COUNTRY-SOURCE kırılımında PRICE ortalamaları:
df.groupby(["SOURCE","COUNTRY"]).agg({"PRICE":"mean"})

# COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir bulalım:

df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg("mean")

# Çıktıyı PRICE’a göre sıralayalım:

agg_df = df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg("mean")
agg_df = agg_df.sort_values(by="PRICE",ascending=False)
agg_df

#  Index’te yer alan isimleri değişken ismine çevirelim:

agg_df = agg_df.reset_index()
agg_df


# age değişkenini kategorik değişkene çevirelim ve agg_df’e ekleyelim.



bins = [0, 18, 23, 30, 40, 70]

lab = ["0_18", "19_23", "24_30", "31_40", "41_70"]

agg_df.head()

agg_df["AGE_CAT"] = pd.cut(x = agg_df["AGE"],  bins = bins, labels= lab)
agg_df.head()


# Yeni seviye tabanlı müşterileri (persona) tanımlayalım:


agg_df.head()


agg_df["customer_level_based"] = [col[0].upper() +"_" + col[1].upper() +"_"+ col[2].upper() + "_" +col[5].upper() for col in agg_df.values]
agg_df.head()

persona = agg_df.groupby("customer_level_based").agg("mean")

persona.head()


# Yeni müşterileri (personaları) segmentlere ayıralım:


agg_df["segment"] = pd.qcut(agg_df["PRICE"], 4, labels=["D","C","B","A"])

agg_df.groupby("segment").agg(["sum", "max", "mean"])

agg_df.head()

CSegment = agg_df[agg_df["segment"]=="C"]

CSegment.head()
CSegment.describe().T
CSegment.min()
CSegment.groupby("SEX").agg("mean")
CSegment.groupby("AGE").agg("mean")


# Yeni gelen müşterileri segmentlerine göre sınıflandıralım ve ne kadar gelir getirebileceğini tahmin edelim :)

agg_df.groupby("segment").agg(["sum","max","mean"])
new_cust = "tur_android_female_31_40".upper()

new_cust

agg_df.groupby("customer_level_based").agg("mean")
#dd[dd["customer_level_based"]== new_cust]
#agg_df[agg_df["customer_level_based"] = new_cust

agg_df[agg_df["customer_level_based"]== new_cust]

new_cust2 = "fra_ios_female_31_40".upper()

agg_df[agg_df["customer_level_based"]== new_cust2]

