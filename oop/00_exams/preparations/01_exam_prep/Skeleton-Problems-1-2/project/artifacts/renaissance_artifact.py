from project.artifacts.base_artifact import BaseArtifact

class RenaissanceArtifact(BaseArtifact):
    def __init__(self, name: str, price: float, space_required: int):
        super().__init__(name, price, space_required)

    def __str__(self):
        return "Renaissance Artifact"