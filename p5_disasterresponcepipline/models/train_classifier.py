import sys
# import libraries
import pandas as pd
from sqlalchemy import create_engine
import pickle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
import nltk
nltk.download(['punkt', 'wordnet','stopwords'])
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


def load_data(database_filepath):
    db='sqlite:///'+ database_filepath
    engine =create_engine(db)
    df = pd.read_sql_table("disaster_response",engine)
    X =df['message'].values
    Y =df.iloc[:,4:].values 
    category_names=  df.iloc[:,4:].columns
    return X, Y, category_names


def tokenize(text):
    text = re.sub(r'[^a-zA-Z0-9]',' ',text.lower())
    #split the words
    tokens = word_tokenize(text)
    #remove stop words
    tokens = [w for w in tokens if w not in stopwords.words("english")]
     #sterm and convert to the base
    lemmatizer = WordNetLemmatizer()
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    pipeline =Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))])
    #tunning
    parameters = {'clf__estimator__max_depth': [10,15],'clf__estimator__min_samples_split': [2,3]}

    cv = GridSearchCV(pipeline, param_grid=parameters,n_jobs=-1)
   
    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    y_pred = model.predict(X_test)
    for i, col in enumerate(category_names):
        print(col,classification_report(Y_test[i],y_pred[i]))


def save_model(model, model_filepath):
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()