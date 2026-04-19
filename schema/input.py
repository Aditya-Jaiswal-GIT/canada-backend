from pydantic import BaseModel,Field
class Input(BaseModel):
    year : int = Field(...,description="Year to find the per capita income")