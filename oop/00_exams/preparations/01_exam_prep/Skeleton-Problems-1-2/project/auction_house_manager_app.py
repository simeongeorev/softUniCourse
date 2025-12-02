from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    ARTIFACT_TYPES = {
        "RenaissanceArtifact": RenaissanceArtifact,
        "ContemporaryArtifact": ContemporaryArtifact
    }

    COLLECTOR_TYPES = {
        "Museum": Museum,
        "PrivateCollector": PrivateCollector
    }

    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    @staticmethod
    def get_object_by_name(search_name: str, collection: list) -> BaseArtifact | BaseCollector | None:
        return next((x for x in collection if x.name == search_name), None)

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self.ARTIFACT_TYPES.keys():
            raise ValueError("Unknown artifact type!")

        if self.get_object_by_name(artifact_name, self.artifacts):
            raise ValueError(f"{artifact_name} has been already registered!")

        artifact = self.ARTIFACT_TYPES[artifact_type](artifact_name, artifact_price, artifact_space)

        self.artifacts.append(artifact)

        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.COLLECTOR_TYPES.keys():
            raise ValueError("Unknown collector type!")

        if self.get_object_by_name(collector_name, self.collectors):
            raise ValueError(f"{collector_name} has been already registered!")

        collector = self.COLLECTOR_TYPES[collector_type](collector_name)

        self.collectors.append(collector)

        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector: BaseCollector | None = self.get_object_by_name(collector_name, self.collectors)
        if not collector:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        artifact: BaseArtifact | None = self.get_object_by_name(artifact_name, self.artifacts)
        if not artifact:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required

        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

    def remove_artifact(self, artifact_name: str):
        artifact = self.get_object_by_name(artifact_name, self.artifacts)
        if not artifact:
            return "No such artifact."

        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        collectors_for_fundraising: list[BaseCollector] = [c for c in self.collectors if c.available_money <= max_money]
        for c in collectors_for_fundraising:
            c.increase_money()
        return f"{len(collectors_for_fundraising)} collector/s increased their available money."

    def get_auction_report(self):
        sold_artifacts_total = sum([len(a.purchased_artifacts) for a in self.collectors])
        available_artifacts_counts = len(self.artifacts)

        result = f"**Auction statistics**\nTotal number of sold artifacts: {sold_artifacts_total}\nAvailable artifacts for sale: {available_artifacts_counts}\n***\n"

        sorted_collectors = sorted(self.collectors, key=lambda x: (-len(x.purchased_artifacts), x.name))

        result += "\n".join([x.__str__() for x in sorted_collectors])
        return result
