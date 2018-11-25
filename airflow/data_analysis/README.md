# Sentiment Analysis and Aspect classification for Hotel Reviews

This is the source code of MonkeyLearn's series of posts related to analyzing sentiment and aspects from hotel reviews using machine learning models.

### Code organization

The project itself is a Scrapy project that is used to gather training and testing data from different sites like TripAdvisor and Booking. Besides, there are a series of Python scripts and Jupyter notebooks that implement some necessary scripts.

### [Creating a sentiment analysis model with Scrapy and MonkeyLearn](https://blog.monkeylearn.com/creating-sentiment-analysis-model-with-scrapy-and-monkeylearn/)

The TripAdvisor (extraction_data/spider/tripadvisor_spider.py) spider is used to gather data to train a sentiment analysis classifier in MonkeyLearn. Reviews texts are used as the sample content and reviews stars are used as the category (1 and 2 stars = Negative, 4 and 5 stars = Positive).

To crawl ~15000 items from tripadvisor, from some zone, use:
```sh
scrapy crawl tripadvisor -o itemsTripadvisor.csv -s CLOSESPIDER_ITEMCOUNT=15000
```
To crawl from single hotel, restaurant, etc., in tripadvisor use:

```sh
scrapy crawl tripadvisor_singlehotel -o itemsTripadvisor.csv -s CLOSESPIDER_ITEMCOUNT=15000
```

You can check out the generated machine learning sentiment analysis model [here](https://app.monkeylearn.com/categorizer/projects/cl_rZ2P7hbs/tab/main-tab).

### [Aspect Analysis from reviews using Machine Learning](https://blog.monkeylearn.com/aspect-analysis-from-reviews-using-machine-learning/)

The Booking spider (extraction_data/spider/booking_spider.py) is used to gather data to train an aspect classifier in MonkeyLearn. The data obtained with this spider can be manually tagged with each aspect (eg: cleanliness, comfort & facilities, food, internet, location, staff, value for money) using MonkeyLearn's Sample tab or an external crowd sourcing service like Mechanical Turk.

To crawl from booking use:
```sh
scrapy crawl booking -o itemsBooking.csv
```

You first have to add the url of a starting zone. To crawl from a single hotel in booking use:

```sh
scrapy crawl booking_singlehotel -o <hotel name>.csv
```

The Booking listHotels and Tripdavisor listHotels spiders generate a list of hotels that it will be used to Booking and Tripadvisor spiders

Booking:
```sh
scrapy crawl booking_listHotels -o <list name>.csv 
```

Tripadvisor:
```sh
scrapy crawl tripadvisor_listHotels -o <list name>.csv  
```


- ```opinionTokenizer.py``` is a simple script to obtain the "opinion units" from each review.
- ```classify_and_plot_reviews.ipynb``` is a simple script that uses the generated model to classify new reviews and then plot the results in a graph using Plotly.

You can check out the generated machine learning aspect classifier [here](https://app.monkeylearn.com/categorizer/projects/cl_TKb7XmdG/tab/main-tab).

### [Machine Learning over 1M hotel reviews finds interesting insights](https://blog.monkeylearn.com/machine-learning-1m-hotel-reviews-finds-interesting-insights/)

To crawl from Tripadvisor use:
```sh
scrapy crawl tripadvisor_more -a start_url="http://some_url" -o <hotel_name>.csv -s CLOSESPIDER_ITEMCOUNT=20000
```

### Extract data from Facebook

You can extract data of Facebook pages: posts, comments or insigths. To extract data from Facebook go to extraction_data/oauth/ and use one of them: 

```sh
python facebook_postandcomments.py 
```
```sh
python facebook_insigths.py
```


The scripts and notebooks necessary to replicate the post are in the ```classify_elastic``` folder:

- ```classify_elastic/generate_files_for_indexing.py``` will take the csv file produced by scrapy and generate two files that other scripts will use.
- ```classify_elastic/classify_pipe.py``` will open the ```opinion_units``` file and classify it with MonkeyLearn according to topic and sentiment, and save the results to a new csv file.
- ```classify_elastic/index_reviews_tripadvisor.py``` will index into your ElasticSearch tripadvisor instance the reviews generated by ```generate_files_for_indexing.py```.
- ```classify_elastic/index_reviews_booking.py``` will index into your ElasticSearch booking instance the reviews generated by ```generate_files_for_indexing.py```.
- ```classify_elastic/index_list_hotelsBooking.py ``` will index into your ElasticSearch booking instance the list of hotels generated by ```generate_files_for_indexing.py```.
- ```classify_elastic/index_list_hotelsBooking.py ``` will index into your ElasticSearch tripadvisor instance the list of hotels generated by ```generate_files_for_indexing.py```.
- ```classify_elastic/inndex_comment_facebook.py ``` will index into your ElasticSearch facebook instance the comments generated by ```generate_files_for_indexing.py```.
- ```classify_elastic/inndex_post_facebook.py ``` will index into your ElasticSearch facebook instance the posts generated by ```generate_files_for_indexing.py```.
- ```classify_elastic/inndex_insights_facebook.py ``` will index into your ElasticSearch facebook instance the insights generated by ```generate_files_for_indexing.py```.
- ```classify_elastic/Extract keywords.ipynb``` shows how to extract keywords from the indexed data.

Finally, the ```queries``` folder contains some queries that were used to power the Kibana visualization.