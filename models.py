from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import  relationship, validates

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)


class Hero(db.Model, SerializerMixin):

    __tablename__ = "heros"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    # defines relationship between heros and hero_powers tables
    hero_powers = relationship("HeroPower", back_populates="hero", cascade="all, delete-orphan")

    # defines association proxy beween heros and powers tables
    powers = association_proxy("hero_powers", "power")

    # serilization rules to avoid reccursion errors
    serialize_rules = ("-hero_powers.hero",)

class Power(db.Model, SerializerMixin):

    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    # defines relationship between powers and hero_powers tables
    hero_powers = relationship("HeroPower", back_populates="power", cascade="all, delete-orphan")

    # defines association proxy beween heros and powers tables
    heroes = association_proxy("hero_powers", "hero")

    # serilization rules to avoid reccursion errors
    serialize_rules = ("-hero_powers.power",)

    # Validation for description characters; should be more than 20
    @validates('description')
    def validate_description(self, key, value):
        if not value:
            raise ValueError("Description must be present")
        if len(value)<20:
            raise ValueError("Description must be 20 characters or longer")
        return value

class HeroPower(db.Model, SerializerMixin):

    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey("heros.id"))
    power_id =  db.Column(db.Integer, db.ForeignKey("powers.id"))

    # defines population relationship between her0_powers and all other tables
    hero = relationship("Hero", back_populates='hero_powers')
    power = relationship("Power", back_populates='hero_powers')

    # serilization rules to avoid reccursion errors
    serialize_rules = ("-hero.hero_powers", "-power.hero_powers", )

    # validation for strength input; validates if strength is one of the 3 options(weak, average, strong)
    @validates('strength')
    def validate_strength(self, key, value):
        if value not in ('Strong', 'Weak', 'Average'):
            raise ValueError('Invalid! strength must be; Strong, Weak or Average')
        return value




    
    