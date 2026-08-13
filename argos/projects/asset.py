from dataclasses import dataclass, field


@dataclass
class Asset:
    name: str
    category: str
    description: str
    value: float = 0.0
    tags: list[str] = field(default_factory=list)

    def summary(self) -> str:
        return (
            f"{self.name} [{self.category}] - "
            f"{self.description}"
        )