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