# kafka_helper

`kafka_helper` makes it easy to use the [kafka-python](https://github.com/dpkp/kafka-python) library with [Apache Kafka on Heroku](https://www.heroku.com/kafka). It takes care of parsing the Kafka config vars and establishing an SSL context.

## Usage

```
producer = kafka_adapter.get_kafka_producer()
producer.send('my-topic', key='my key', value={'k': 'v'})
```

```
consumer = kafka_adapter.get_kafka_consumer(topic='my-topic')
for message in consumer:
    print message
```
