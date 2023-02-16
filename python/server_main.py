import elastic_manager
from elastic_manager import Elastic_Manager

def main():
    """main method"""
    port = "http://localhost:9200"
    manager = Elastic_Manager(port)
    manager.insertDocument("")

if __name__ == "__main__":
     main()
