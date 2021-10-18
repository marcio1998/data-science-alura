#!/usr/bin/env python
# coding: utf-8

# # Analisando as Notas Em geral 

# In[ ]:


#pandas cria um dataframe.
import pandas as pd
notas = pd.read_csv('../DATA/ratings.csv') #leitura do arquivo csv.
#mostrar as 5 primeiras notas.
notas.head()


# In[ ]:


notas.shape #mostra total de linhas e colunas.


# In[ ]:


#renomear colunas.
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]


# In[ ]:


notas.head()


# In[ ]:


notas["nota"].unique()


# In[ ]:


notas["nota"].value_counts()


# In[ ]:


notas["nota"].mean()


# In[ ]:


#explorar de maneira visual.
notas.nota.plot(kind="hist")


# In[ ]:


#uso da median
print("Média",notas.nota.mean())
print("Mediana",notas.nota.median())


# In[ ]:


notas.nota.describe()


# In[ ]:


import seaborn as sns
sns.boxplot(notas.nota)


# # Analisando Notas Por Filmes

# In[ ]:


filmes = pd.read_csv("../DATA/movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]
filmes.head()


# In[ ]:


notas.head()


# In[ ]:


notas.query("filmeId==1").nota.mean() #faz um filtro


# In[ ]:


notas.query("filmeId==2").nota.mean()


# In[ ]:


notas.groupby("filmeId").head() #agrupa por filme id


# In[ ]:


notas.groupby("filmeId").nota.mean().head()
media_por_filme = notas.groupby("filmeId").nota.mean()


# In[ ]:


media_por_filme.head()


# In[ ]:


sns.boxplot(media_por_filme)


# In[ ]:


media_por_filme.plot(kind="hist")


# In[ ]:


media_por_filme.describe()


# In[ ]:


sns.distplot(media_por_filme, bins=20)


# In[ ]:


import matplotlib.pyplot as plt #usa em baixo nível para plotar um gráfico
plt.hist(media_por_filme)
plt.title("Histograma Das Médias dos Filmes")


# In[ ]:





# # Movies TMDB 5000 Movies 

# In[ ]:


tmdb = pd.read_csv('../DATA/tmdb_5000_movies.csv')
tmdb.head()


# In[ ]:


tmdb.original_language.unique()


# In[ ]:


contagem_de_linguas = tmdb["original_language"].value_counts().to_frame().reset_index() #criar dataframe com to_frame() reset_index cria duas colunas
contagem_de_linguas.columns= ["original_languages", "total"]
contagem_de_linguas


# In[ ]:


sns.catplot(x = "original_language", kind = "count", data = tmdb)


# In[ ]:


plt.pie(contagem_de_linguas.total, labels = contagem_de_linguas.original_languages)


# In[ ]:


total_por_lingua = tmdb["original_language"].value_counts()
total_geral = total_por_lingua.sum()
print(total_geral)
total_de_ingles = total_por_lingua.loc["en"]
total_do_resto = total_geral - total_de_ingles
print(total_de_ingles, total_do_resto)


# In[ ]:


dados = {
    'lingua' : ["ingles", "outros"],
    'total': [total_de_ingles, total_do_resto]
}
dados = pd.DataFrame(dados)
sns.barplot(x="lingua", y="total", data=dados)


# In[ ]:


plt.pie(dados["total"], labels = dados["lingua"])


# In[ ]:


tmdb.query("original_language != 'en'").original_language.value_counts()
#linguas_sem_ingles = tmdb.query("original_language != 'en'").original_language
#print(linguas_sem_ingles)


# In[ ]:


linguas_sem_ingles = tmdb.query("original_language != 'en'")
linguas_sem_ingles_contagem =  tmdb.query("original_language != 'en'").original_language.value_counts()
sns.catplot(x='original_language', data=linguas_sem_ingles, kind="count", aspect = 2, order = linguas_sem_ingles_contagem.index, palette="GnBu_d")


# In[ ]:


filmes.head(2)


# In[ ]:


notas.head()


# In[ ]:


notas_toy_story = notas.query("filmeId==1")
notas_jumanji = notas.query("filmeId==2")
print(len(notas_toy_story), len(notas_jumanji))


# In[ ]:


print("Notas toy story: %.2f" %notas_toy_story.nota.mean())
print("Notas jumaji: %.2f" %notas_jumanji.nota.mean())


# In[ ]:


print("Notas toy story: %.2f" %notas_toy_story.nota.median())
print("Notas jumaji: %.2f" %notas_jumanji.nota.median())


# In[ ]:


import numpy as np
np.array([2.5] * 10)
np.array([3.5] * 10)
filme1 = np.append(np.array([2.5] * 10), np.array([3.5] * 10))
np.array([5] * 10 )
np.array([1] * 10)
filme2 = np.append(np.array([5] * 10 ), np.array([1] * 10))
print(filme1.mean(), filme2.mean())
print(np.median(filme1), np.median(filme2))


# In[ ]:


plt.hist(filme1)
plt.hist(filme2)


# In[ ]:


plt.boxplot([filme1, filme2])


# In[ ]:


sns.boxplot(notas_toy_story.nota)
sns.boxplot(notas_jumanji.nota)


# In[ ]:


plt.boxplot([notas_toy_story.nota, notas_jumanji.nota])


# In[ ]:


sns.boxplot(x="filmeId", y = nota, data = notas.query("filmeId in [1,2]"))

