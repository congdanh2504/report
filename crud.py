from sqlalchemy.orm import Session
import models

def get_assets(db: Session):
    return db.query(models.Asset).all()