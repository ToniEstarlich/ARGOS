from argos.projects.asset import Asset


class AssetManager:

    def __init__(self):
        self.assets: list[Asset] = []

    def add_asset(
        self,
        name: str,
        category: str,
        description: str,
        value: float = 0.0,
        tags: list[str] | None = None,
    ) -> Asset:

        asset = Asset(
            name=name,
            category=category,
            description=description,
            value=value,
            tags=tags or [],
        )

        self.assets.append(asset)
        return asset

    def list_assets(self) -> list[Asset]:
        return self.assets