from setuptools import setup

setup(
  name = 'kafka-helper',
  version = '0.1',
  description = 'Makes it easy to use the kafka-python library with Apache Kafka on Heroku',
  py_modules=['kafka_helper'],
  author = 'Arthur Louie',
  author_email = 'alouie@heroku.com',
  url = 'https://github.com/heroku/kafka-helper',
  download_url = 'https://github.com/heroku/kafka-helper/tarball/0.1',
  keywords = ['kafka', 'heroku', 'kafka-python'],
  classifiers = [],
)
