from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

accounts = [
    {"name": "Acme Corp", "industry": "Manufacturing", "segment": "Enterprise", "region": "Northeast", "activity_score": 87.5, "status": "Active"},
    {"name": "Globex Inc", "industry": "Technology", "segment": "Mid-Market", "region": "West", "activity_score": 62.3, "status": "At Risk"},
    {"name": "Initech", "industry": "Financial Services", "segment": "Enterprise", "region": "Southeast", "activity_score": 91.0, "status": "Active"},
    {"name": "Umbrella Ltd", "industry": "Healthcare", "segment": "SMB", "region": "Midwest", "activity_score": 44.1, "status": "Churned"},
    {"name": "Hooli", "industry": "Technology", "segment": "Enterprise", "region": "West", "activity_score": 78.9, "status": "Active"},
    {"name": "Pied Piper", "industry": "Technology", "segment": "SMB", "region": "West", "activity_score": 55.2, "status": "At Risk"},
    {"name": "Massive Dynamic", "industry": "Manufacturing", "segment": "Enterprise", "region": "Northeast", "activity_score": 83.7, "status": "Active"},
    {"name": "Soylent Corp", "industry": "Healthcare", "segment": "Mid-Market", "region": "South", "activity_score": 39.8, "status": "Churned"},
    {"name": "Vandelay Industries", "industry": "Financial Services", "segment": "SMB", "region": "Midwest", "activity_score": 67.4, "status": "Active"},
    {"name": "Dunder Mifflin", "industry": "Manufacturing", "segment": "Mid-Market", "region": "Northeast", "activity_score": 72.1, "status": "Active"},
    {"name": "Sterling Cooper", "industry": "Financial Services", "segment": "Enterprise", "region": "Northeast", "activity_score": 88.3, "status": "Active"},
    {"name": "Bluth Company", "industry": "Real Estate", "segment": "SMB", "region": "West", "activity_score": 31.5, "status": "At Risk"},
    {"name": "Wonka Industries", "industry": "Manufacturing", "segment": "Mid-Market", "region": "Midwest", "activity_score": 59.6, "status": "Active"},
    {"name": "Cyberdyne Systems", "industry": "Technology", "segment": "Enterprise", "region": "West", "activity_score": 94.2, "status": "Active"},
    {"name": "Nakatomi Corp", "industry": "Financial Services", "segment": "Mid-Market", "region": "West", "activity_score": 48.7, "status": "At Risk"},
]

db = SessionLocal()

for account in accounts:
    db_account = models.Account(**account)
    db.add(db_account)

db.commit()
db.close()

print(f"Seeded {len(accounts)} accounts successfully.")