## Problem description
Tweets are short texts (sequence of words) sent at specific times by specific individuals. The collection of terms that a tweet contains is collectively describing a message. Appearance of
a term in many tweets makes the term popular.  
A topic is a set of terms. A popular topic is a set of terms that appear together in many tweets. Identifying a popular topic can be done by finding highly frequent combinations of
terms. Tweets have a time in which they are published, and by taking this into consideration, one can see that the popularity of terms is changing over time. Some term that is popular today
may not have been popular 4 days ago but may have been popular the week before that. 

The goal of this work is to identify consistent topics in time, i.e., set of terms that become
frequent together throughout time. For instance, the terms “hurricane” is becoming often
popular, but is not continuously like this. It becomes popular when some hurricane hits a
country, e.g., when it was hitting the US south eastern coasts. The same applies for the term
“nuclear”. It becomes clear when there is interest due to some accord or some disarming
efforts. However, there is no correlation between nuclear and hurricane popularity. On the
other hand, the terms “hurricane” and “emergency” become popular together, meaning
that whenever hurricane is mentioned frequently in tweets, so does the word emergency.​ 1
This leads us to decide that a popular consistent topic is the {“hurricane”, “emergency”}.
Intuitively, we are looking for frequently correlated terms in time.

### Dataset
The dataset chosen is the twitter dataset on COVID from [Kaggle](https://www.kaggle.com/gpreda/covid19-tweets). Some preprocessing of the text of each tweet has been applied, in order to turn it into a sequence of terms (terms can be
words or hashtags)


## Results
A deeper explanation of the problem, the methodologies applied and the results are contained in the pdf file called `consistentTopics.pdf`

