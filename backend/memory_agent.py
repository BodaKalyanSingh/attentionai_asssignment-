from neo4j import GraphDatabase

class MemoryAgent:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def store_memory(self, user, relationship, preference):
        with self.driver.session() as session:
            session.run(
                "MERGE (u:User {name: $user}) "
                "MERGE (p:Preference {name: $preference}) "
                "MERGE (u)-[:LIKES]->(p)",
                user=user, preference=preference
            )
