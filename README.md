<H1>Trump tweet generator</H1>

<H2>Dataset</H2>
We used [Trump tweet dataset](https://www.kaggle.com/austinreese/trump-tweets) that contains over 40k tweets published
by Donald Trump's official twitter profile "realDonaldTrump".

We preprocessed the dataset by applying following transformations:
* We filtered dataset to contain only tweets published after 2015
* We removed "re-tweets" (tweets from other user accounts that Donald Trump's account republished)
* We removed all user tags from from the tweet's content and replaced them with "@TAG"
* We removed all hashtags from the tweet's content and replaced them with #HASHTAG
* We removed all URLs from the tweet's content and replaced them with !URL

Resulting dataset contains 17,786 tweets and that is the version that we used to train our model. 

<H2>Models used</H2>
<H3> Tweet generation </H3>
For tweet generation we fine-tuned pretrained [GPT2 model](https://openai.com/blog/better-language-models/) from openAI.
We used [aitextgen](https://docs.aitextgen.io/) library for python to which has high level API function calls that allow easy
GPT2 model finetunning and persisting.

GPT2 is openAI's transformer based deep neural network that was pretrained on 40 GB of english text data scraped
from the internet.

<H3> Sentiment analysis </H3>
TODO: NAPISAT NESTO

<H2>Application</H2>
To run application Python version 3.7 or later is needed.
1. run following command to install requirements needed to run the program:
    "pip install -r requirements.txt"
2. run "nltk_download.py" (Python3 ntlk_download.py) to download sentiment analysis model
3. run "gui.py" to start the application (Python3 gui.py)
4. When application launches your are greeted by "THE MAN" himself. One entry textbox and two sliders are presented:
    * In textbox labeled "Topic" you enter the start of the tweet which model will finish.
    * Temperature slider is used to determine how "wild" we want our model to be. For low temperature values model will rely
more on the training data, and for higher temperature values it will be more prone to improvising.
    * Tweet length slider is used to determine how long we want to generated tweet to be (number of characters). 

5. Pressing "Trump it!" starts tweet generation. After the tweet is generated based on its sentiment analysis
one of two windows will open:
    1. Positive window - when tweet's sentiment prediction is positive
    2. Negative window - when tweet's sentiment prediction is negative
6. By pressing "Trump approves" button the sentiment window will close and you can generate another tweet.
7. To exit the program press little x button in the top right corner of the screen.