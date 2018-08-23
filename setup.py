from setuptools import setup

setup(
  name = 'kafka-helper',
  version = '0.2',
  description = 'Makes it easy to use the kafka-python library with Apache Kafka on Heroku',
  py_modules=['kafka_helper'],
  author = 'Arthur Louie',
  author_email = 'alouie@heroku.com',
  url = 'https://github.com/heroku/kafka-helper',
  download_url = 'https://github.com/heroku/kafka-helper/tarball/0.1',
  keywords = ['kafka', 'heroku', 'kafka-python'],
  install_requires=[
      'cryptography',
  ],
  license='MIT',
  classifiers = [
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Development Status :: 4 - Beta',
      'Topic :: Text Processing :: Linguistic',
  ],

)
