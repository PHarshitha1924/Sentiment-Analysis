# Sentiment-Analysis

📝 **Description:**

This project is a **basic sentiment analysis tool** that takes a sentence as input and tells whether the sentiment expressed is **positive**, **negative**, or **neutral**.

It uses the **TextBlob** library, which is built on top of NLTK and provides a simple API to perform common NLP tasks such as sentiment analysis.

---

⚙️ **What It Does:**

* Takes a **sentence** from the user.
* Analyzes the **polarity** of the sentence:

  * **Positive** if polarity > 0
  * **Negative** if polarity < 0
  * **Neutral** if polarity = 0
* Displays the **original sentence**, the **polarity score**, and the **sentiment category**.

---

🖥️ **Sample Input:**

```
I love this product, it's amazing!
```

🖨️ **Sample Output:**

```
Input Text: I love this product, it's amazing!
Sentiment Polarity: 0.6125
Detected Sentiment: Positive 😊
```

---

### 🧰 **Tech Stack:**

* **Python**
* **TextBlob** (`pip install textblob`)

