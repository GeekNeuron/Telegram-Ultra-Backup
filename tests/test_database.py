from bot.database import BackupFile, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def test_database_insertion():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    file = BackupFile(user_id=123, file_name="test.txt", file_id="abc123")
    session.add(file)
    session.commit()

    result = session.query(BackupFile).first()
    assert result.file_name == "test.txt"
    assert result.user_id == 123
