from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient

es_client = Elasticsearch("http://localhost:9200")
print(es_client.info().body)

es_index_client = IndicesClient(es_client)


configurations = {
    "settings": {
        "index": {"number_of_replicas": 2},
        "analysis": {
            "filter": {
                "ngram_filter": {
                    "type": "edge_ngram",
                    "min_gram": 2,
                    "max_gram": 15,
                },
            },
            "analyzer": {
                "ngram_analyzer": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "ngram_filter"],
                },
            },
        },
    }
}

es_index_client.create(index="recipes", body=configurations)
