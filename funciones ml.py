
def get_class_metrics(y_test, y_pred):
  
    acc = round(accuracy_score(y_test, y_pred), 3)
    f1 = round(f1_score(y_test, y_pred), 3)
    precision = round(precision_score(y_pred,y_test),3)
    recall = round(recall_score(y_pred,y_test),3)
    
    scores = [acc, f1, precision, recall]
    # Get confusion matrix
    mat = confusion_matrix(y_test, y_pred)
    
      # create confusion matrix
    sns.heatmap(mat, annot=True, fmt='d')
    plt.xlabel('Predicted', fontsize=13)
    plt.ylabel('True', fontsize=13)
    plt.title('Confusion Matrix', fontsize=14)
    
    return scores, plt, mat



def fit_predict(X_train, X_test, y_train, model, parameters_grid):
    
    # define grid search
    grid_search = GridSearchCV(estimator=model, param_grid=parameters_grid, cv=10, n_jobs=-1)
  
    # fit estimator
    grid_search.fit(X_train, y_train)
    
    # get best estimator
    best = grid_search.best_estimator_
    
    # predict
    y_pred = best.predict(X_test)
    
    return y_pred, grid_search


def display_df(scores, model):
    df = pd.DataFrame(scores).T
    df = df.rename(index={0: model}, columns={0: 'Accuracy', 1: 'F1 Score',2 :"Precision", 3:"recall"})
    return(df)



xgbclassi = XGBClassifier()

parameters_gridcgboost = {
    'n_estimators': [100, 500],0
    'learning_rate': [0.01, 0.1,1],
     'max_depth': [5, 30],
}

# get predictions
y_predxgb, grid_searchxgb = fit_predict(Xtodos_train, Xtodos_test, ytodos_train, xgbclassi, parameters_gridcgboost)

# calculate metrics
scores, plt, mat = get_class_metrics(ytodos_test, y_predxgb)

resxgbt = display_df(scores,Xgbosst)
resxgbt
