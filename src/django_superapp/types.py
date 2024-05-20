from dataclasses import dataclass
from typing import Dict, Optional

from pydantic import BaseModel


@dataclass
class SuperAppProjectTemplate:
    name: str
    description: str
    repo: str
    branch: str
    kwargs: Optional[Dict] = None
    default: Optional[bool] = False


@dataclass
class SuperAppAppTemplate:
    name: str
    description: str
    repo: str
    branch: str
    kwargs: Optional[Dict] = None


@dataclass
class SuperAppTemplate(BaseModel):
    projects: Dict[str, SuperAppProjectTemplate]
    apps: Dict[str, SuperAppAppTemplate]
