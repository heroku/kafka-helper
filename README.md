# kafka_helper

`kafka_helper` makes it easy to use the [kafka-python](https://github.com/dpkp/kafka-python) library with [Apache Kafka on Heroku](https://www.heroku.com/kafka). It takes care of parsing the Kafka config vars and establishing an SSL context.

**NOTE**: The `kafka_helper` library is not officially supported by Heroku.

## Installation
```
pip install kafka-helper
```

## Usage

```
import kafka_helper
```

To get a producer and write some values to a topic:
```
producer = kafka_helper.get_kafka_producer()
producer.send('my-topic', key='my key', value={'k': 'v'})
```

To get a consumer of a topic and iterate over its stream:

```
consumer = kafka_helper.get_kafka_consumer(topic='my-topic')
for message in consumer:
    print message
```
