from dataclasses import dataclass


@dataclass
class Metadata:
    material: str
    moisture_content: int
    cutting_direction: str
    feed_speed: float
    cutting_speed: float
    cutting_depth: float
    tool_id: str
    inserts: bool
    n_cutting_edges: int
    comments: str
    stats_id: int


@dataclass
class Stats:
    min: float
    max: float
    mean: float
    median: float
    rms: float
    std: float
