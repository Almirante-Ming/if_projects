from sqlalchemy.orm import registry, Mapped, mapped_column
from sqlalchemy.sql import func
from datetime import datetime

table_registry = registry()

@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    passphase: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
