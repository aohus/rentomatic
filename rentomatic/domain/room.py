import dataclasses
import uuid


@dataclasses.dataclass
class Room:
    code: uuid.UUID
    size: int
    price: int
    longitude: float
    latitude: float

    @classmethod
    def from_dict(cls, init_dict: dict) -> "Room":
        return cls(**init_dict)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
