import elastic_manager
from elastic_manager import ElasticManager

def main():
    """main method"""
    port = "http://localhost:9200"
    manager = ElasticManager(port)
    manager.insertDocument("")

if __name__ == "__main__":
    main()
