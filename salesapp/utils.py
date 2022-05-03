import seaborn as sns
import pandas
from matplotlib import pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Sales of items')
    #sns.barplot(x,y)
    plt.bar(x,y,color ='grey',width = 0.2)
    plt.xticks(rotation=45)
    plt.xlabel('Item')
    plt.ylabel('Price')
    plt.tight_layout()
    graph=get_graph()
    return graph


def get_bargraph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_barplot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Covid rates')
    sns.barplot(x,y)
    #plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('States')
    plt.ylabel('Covid rates')
    plt.tight_layout()
    graph=get_bargraph()
    return graph

