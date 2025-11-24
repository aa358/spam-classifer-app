# 📧 Email Spam Classifier

A Machine Learning project that detects whether an email is **Spam** or **Not Spam** using **TF-IDF** and **Logistic Regression**. The model is deployed on Streamlit for real-time classification.

🔗 Live App: https://aa358-email-spam-classifier.streamlit.app/

📁 Dataset: Complete SpamAssassin Corpus (cleaned + merged)

## 🚀 Project Overview

The goal of this project was to build a beginner-friendly NLP classifier that identifies spam emails based on their content.<br>
Using TF-IDF vectorization and Logistic Regression, the model learns patterns from thousands of real email samples and predicts the likelihood of spam.

This project helped me strengthen my understanding of:

* Text preprocessing

* TF-IDF vectorization

* Model training & evaluation

* Confusion matrices & interpretability

* Real-time ML deployment using Streamlit

## 🧠 Model Architecture

The core pipeline:
```
model = make_pipeline(
    TfidfVectorizer(ngram_range=(1,2), max_features=8000),
    LogisticRegression(max_iter=1000)
)
```
* TF-IDF Vectorizer: Converts email text into meaningful numeric features

* n-grams (1,2): Captures word pairs for better context

* Logistic Regression: Reliable baseline classifier for binary NLP tasks

## 📊 Model Performance
| Metric        | Score |
| ------------- | ----- |
| **Accuracy**  | 0.953 |
| **Precision** | 0.899 |
| **Recall**    | 0.958 |
| **F1 Score**  | 0.927 |

### 🔍 Confusion Matrix
```
[[790,  41],
 [ 16, 363]]
```
* False Positives (41): Legit emails misclassified as spam

* False Negatives (16): Spam emails missed

* Strong recall shows the model successfully catches most spam messages.

## 🛠️ Technologies Used

* Python

* scikit-learn

* pandas

* Streamlit

* TF-IDF (NLP)

## 🖥️ Deployment

The app is deployed on Streamlit Cloud and allows users to paste any email body to receive a real-time classification.

**Features:**

✔ Clean UI <br>
✔ Real-time spam prediction <br>
✔ Shows probability score <br>
✔ Secure & lightweight backend

## 📂 Project Structure
```
├── app.py                               # Streamlit application  
├── EmailSpamClassifier.ipynb            # Pipeline & training  
├── completeSpamAssassin.csv             # Dataset
├── requirements.txt  
└── .gitignore
└── email_spam_classifier.pkl
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📬 Contact

Arqam Usman Ali<br>
Software Developer<br>
[LinkedIn](https://www.linkedin.com/in/arqam-usman-ali/) <br>
[Portfolio](https://aa358.github.io/)
