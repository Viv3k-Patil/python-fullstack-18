from pydantic import BaseModel, Field

# team schema
class Team(BaseModel):
    id: int
    name: str = Field(example="My dream team", description="Enter team name", min_length=3, max_length=20)
    player: str