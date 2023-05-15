def plot_roc (roc_auc):
    plt.figure (figsize = (7,7))
    plt.title ("Receiver Operating Characteristics")
    plt.plot(fpr, tpr, color="b", label = "AUC")
    plt.legend(loc="lower right")
    plt.plot ([0,1], [0,1], linestyle = "--")
    plt.axis("tight")
    plt.ylabel("True positve rate")
    plt.xlabel("false positive rate")
  
  
  
  def plot_data (hue, data):
    for i, col in enumerate(data.columns):
      plt.figure(i)
      ax = sns.countplot(x=data[col], hue=hue, data=data)
        
        


def plot_stock_prices_with_labels(dates, prices, labels):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(dates, prices, '-b', label='Stock Prices')
    
    for date, price, label in zip(dates, prices, labels):
        ax.annotate(label, xy=(date, price), xytext=(-20, 20),
                    textcoords='offset points', arrowprops=dict(arrowstyle="->", color='black'))
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title('Stock Prices with Labels')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
