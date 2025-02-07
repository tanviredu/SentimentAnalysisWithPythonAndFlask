from flask import Flask, request, jsonify
from textblob import TextBlob


app = Flask(__name__)

@app.route('/Welcome', methods=['GET'])
def welcome():
    return jsonify({'message': 'Welcome to the Sentiment Analysis API'})

@app.route('/analyse', methods=['POST'])
def analyse():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No data found'})
        
        raw_text = data['text']
        blob = TextBlob(raw_text)
        sentiment_polarity = blob.sentiment.polarity
        sentiment_subjectivity = blob.sentiment.subjectivity
        Adj = []
        for word, tag in blob.tags:
            len_of_nouns = len(word)
            if tag in ["JJ", "JJR", "JJS"]:
                Adj.append(word)
                
        return jsonify({
            "text" : raw_text,
            "Total Tokens": len_of_nouns,
            "Adj used": Adj,
            "polarity" : sentiment_polarity,
            "subjectivity" : sentiment_subjectivity
            
        })
    except Exception as e:
        return jsonify({'error': str(e)})
    
    


if __name__ == '__main__':
    app.run()