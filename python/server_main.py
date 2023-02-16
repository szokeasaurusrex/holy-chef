from elastic_manager import ElasticManager

def main():
    """main method"""
    port = "http://localhost:9200"
    manager = ElasticManager(port)
    manager.insert_document("recipe", "filler")

if __name__ == "__main__":
    main()
