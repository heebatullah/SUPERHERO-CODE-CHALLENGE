from app import app
from models import db, Hero, Power, HeroPower

with app.app_context():
    # Clear existing data
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()
    db.session.commit()

    # Add Heroes
    hero1 = Hero(name="Peter Parker", super_name="Spider-Man")
    hero2 = Hero(name="Tony Stark", super_name="Iron Man")
    db.session.add_all([hero1, hero2])
    db.session.commit()

    # Add Powers
    power1 = Power(description="Wall-Crawling")
    power2 = Power(description="Super Intelligence")
    db.session.add_all([power1, power2])
    db.session.commit()

    # Link Heroes and Powers
    hp1 = HeroPower(strength="Strong", hero_id=hero1.id, power_id=power1.id)
    hp2 = HeroPower(strength="Average", hero_id=hero2.id, power_id=power2.id)
    db.session.add_all([hp1, hp2])
    db.session.commit()

    print("Database seeded successfully!")