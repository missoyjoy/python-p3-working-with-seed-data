from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game, Base

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    
    session.query(Game).delete()
    session.commit()
    
    print("Seeding games...")

    games = [
        Game(
            title=fake.name(),
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(0, 60)
        )
        for i in range(50)
    ]

    session.bulk_save_objects(games)
    session.commit()

    print("Seeding complete.")
