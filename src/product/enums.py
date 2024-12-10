from sqlalchemy.types import Enum
import enum

class SeasonEnum(enum.Enum):
    spring = "spring"
    summer = "summer"
    autumn = "autumn"
    winter = "winter"